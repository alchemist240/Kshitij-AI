# 🤖 Kshitij AI

Kshitij AI is a personalized GPT-powered assistant designed to behave and respond like me using a structured JSON profile. Inspired by the vision of building my own digital twin and somewhat inspired from DONNA AI of SUITS, this app connects you with an AI chatbot that mimics my personality, interests, style of speaking, and memory — all without training any ML models.


> 🧠 *"DONNA from Suits would be proud of me."*  
> — Just a developer building their own personal AI assistant 😉

---

## 🧠 What It Does

Kshitij AI reads a custom-built `profile.json` which contains key details about a person — their tone, language, hobbies, education, FAQs, and more. It uses OpenAI’s GPT API to simulate intelligent responses based on that profile.

It's like building your own ChatGPT — but with your memories, values, and unique way of speaking.

---

## ✨ Features

- 💬 Personalized responses using your JSON profile
- 🗣️ Speech-to-text support using microphone input (via Streamlit)
- 🗣️ Integrates FFmpeg for efficient speech-to-text processing from audio input
- 🌐 Multilingual output — supports English, Hindi, and more (powered by OpenAI)
- 🧠 Semantic understanding of questions — not just keyword matching
- 🎯 Context-aware chat that respects tone, goals, and speaking style
- 🔐 Secure secret management via `secrets.toml` (excluded from Git)
- ⚡ Fast response rendering using Streamlit
- 📂 Lightweight structure — easy to modify and deploy


---

## 🖼 Demo

Here’s how Kshitij AI looks in action:

### 🧪 Interface Sample

![Demo 1](https://github.com/alchemist240/Kshitij-AI/raw/main/assets/Demo1.png)

### 🧠 AI Response Flow

![Demo 2](https://github.com/alchemist240/Kshitij-AI/raw/main/assets/Demo2.png)

---

## 🛠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **Backend**: OpenAI GPT API (`openai` Python SDK)
- **Profile Format**: JSON (`profile.json`)
- **Language**: Python 3.11

---

## 📬 Note

This project is purely for fun and learning purposes. It is **not hosted publicly**, and both the `profile.json` and OpenAI API key are kept private.This same prototype can't be recreted.

However, the code is open for everyone — so you’re welcome to recreate your **own personal AI** just like I did. If you'd like to see Kshitij AI in action or just chat about how it works, feel free to reach out to me directly. 🙂
