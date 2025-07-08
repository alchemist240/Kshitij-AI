import streamlit as st
import json
import difflib
import os
from openai import OpenAI
import time
from components.speech_to_text import record_and_transcribe

# -----------------------------
# ✅ Streamlit Page Settings
# -----------------------------
st.set_page_config(page_title="Kshitij AI", layout="centered")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    h1, h2, h3, h4, h5, h6, .stTextInput label {
        font-family: 'Poppins', sans-serif;
    }

    .chat-entry {
        font-family: 'Poppins', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)
st.title("🤖 Kshitij AI")
st.markdown("Welcome to **KshitijGPT** – your brutally honest, funny, and gym-pumped assistant 😎")
st.markdown("### 💬 Ask KshitijGPT")

# -----------------------------
# ✅ Load OpenAI API Key
# -----------------------------
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# -----------------------------
# ✅ Load Personality JSON
# -----------------------------
with open("data/kshitij_profile.json", "r", encoding="utf-8") as f:
    persona_data = json.load(f)

# -----------------------------
# ✅ Load Chat History
# -----------------------------
chat_file = "data/chat_history.json"
if "chat" not in st.session_state:
    if os.path.exists(chat_file):
        with open(chat_file, "r", encoding="utf-8") as f:
            st.session_state.chat = json.load(f)
    else:
        st.session_state.chat = []

# -----------------------------
# ✅ Semantic Retrieval
# -----------------------------
def get_semantic_context(user_question):
    inputs = [item['input'] for item in persona_data]
    closest_matches = difflib.get_close_matches(user_question, inputs, n=5, cutoff=0.3)
    matched_qas = [item for item in persona_data if item['input'] in closest_matches]
    return matched_qas

# -----------------------------
# ✅ Prompt Builder
# -----------------------------
def build_prompt(user_question):
    matched_examples = get_semantic_context(user_question)
    examples = ""
    for item in matched_examples:
        examples += f"Q: {item['input']}\nA: {item['output']}\n\n"

    prompt = f"""
You are KshitijGPT — an AI that answers questions exactly like Kshitij would.
Respond in his style: honest, witty, gym bro meets AI nerd, and always in English unless the user explicitly requests another language.
Dont give gym references everywhere.Give them just when necessary.
Use clear numbered steps only if the question truly requires it (like how-tos or processes).  
Otherwise, respond in a natural paragraph format.  
Include relevant emojis to add flavor and energy to the tone!

Here are some known Q&A examples:
{examples}
Now answer this new question as Kshitij would:

Q: {user_question}
A:
"""
    return prompt

# -----------------------------
# ✅ Format Response for Clean Output
# -----------------------------
def format_response(text):
    for i in range(1, 6):
        text = text.replace(f"Step {i}", f"\n\n👉 **Step {i}**")
    text = text.strip() + "\n\n---\n"

    emoji_replacements = {
        "gym": "🏋️",
        "coding": "💻",
        "code": "💻",
        "game": "🎮",
        "fitness": "💪",
        "food": "🍔",
        "sleep": "😴",
        "natural": "🌱",
        "AI": "🧠",
        "Kshitij": "😎"
    }
    for word, emoji in emoji_replacements.items():
        text = text.replace(word, f"{word} {emoji}")

    return text

# -----------------------------
# ✅ Ask GPT
# -----------------------------
def ask_gpt(user_input):
    prompt = build_prompt(user_input)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a brutally honest, funny, humorous, sometimes philosophical, and sophisticated AI assistant named KshitijGPT."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=200
    )
    return response.choices[0].message.content.strip()

# -----------------------------
# ✅ Chat Layout: Top = History, Bottom = Input + Mic
# -----------------------------
chat_container = st.container()  # for messages above input bar

# Bottom input + mic
with st.container():
    cols = st.columns([4, 1])
    with cols[0]:
        typed_input = st.chat_input("Ask me anything about Kshitij...")  # No key used!
    with cols[1]:
        record_and_transcribe()

# Decide input source
user_input = None
if typed_input:
    user_input = typed_input
elif st.session_state.get("transcribed_text"):
    user_input = st.session_state["transcribed_text"]
    st.session_state["transcribed_text"] = ""  # Reset after using voice input

# -----------------------------
# ✅ Handle New Message
# -----------------------------
if user_input:
    st.session_state.chat.append(("user", user_input))

    with st.spinner("Thinking like LORD Kshitij..."):
        try:
            answer = ask_gpt(user_input)
        except Exception as e:
            answer = f"Oops! Something went wrong: {e}"

    st.session_state.chat.append(("ai", answer))

    # Save chat
    with open(chat_file, "w", encoding="utf-8") as f:
        json.dump(st.session_state.chat, f, indent=2, ensure_ascii=False)

# -----------------------------
# ✅ Render Chat Above Input
# -----------------------------
with chat_container:
    for speaker, msg in st.session_state.chat:
        if speaker == "user":
            st.chat_message("user").write(msg)
        else:
            formatted_msg = format_response(msg)
            st.chat_message("assistant").markdown(formatted_msg, unsafe_allow_html=True)
