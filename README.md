# 🤖 Kshitij AI

**Kshitij AI** is a personalized GPT-powered assistant designed to behave and respond like me — using a structured JSON profile and cutting-edge semantic search. Inspired by the vision of building my own digital twin (*and let’s be honest, who doesn't want one ?*), this app connects you with an AI chatbot that mimics my tone, memory, humor, and style .

> 🧠 *"DONNA from Suits would be proud of me."*  
> — Just a dev building his own AI twin 😉

---

## 🧠 What It Does

Kshitij AI loads a custom-built `profile.json` file that contains everything about me — how I speak, how I think, and what I’ve said in the past (FAQs). On top of that, it uses **RAG (Retrieval-Augmented Generation)** powered by FAISS and Sentence Transformers to deeply understand your question and generate highly relevant answers — even if your question isn’t word-for-word from the profile.

It’s like building your own ChatGPT — but with your *memories, tone, and unique brainwaves*.

---

## ✨ Features

- 💬 Personalized responses using your JSON-based personality  
- 🧠 **RAG-powered semantic search** using FAISS + Sentence Transformers  
- 📥 Dynamic vector indexing of your custom Q&A profile  
- 🗣️ Speech-to-text input using microphone (Streamlit + FFmpeg)  
- 🔁 Real-time voice transcription using OpenAI Whisper API  
- ⚡ Smooth, animated chat UI using Streamlit containers  
- 📜 Chat history persists across sessions  
- 🌐 Multilingual support (GPT can reply in any language on request)  
- 🔐 Secure secrets handling via `secrets.toml`  
- 🛡️ Fully offline RAG engine — no need to re-train models  
- 🧱 Lightweight codebase — easy to clone, tweak, and personalize  

---
### 🧠 How RAG Works in This Project

1. **Profile Vectorization**  
   - All questions from `kshitij_profile.json` are converted into vectors using `SentenceTransformer` (`all-MiniLM-L6-v2`).  
   - These embeddings are stored in a FAISS index (local vector DB).

2. **Query Embedding**  
   - When a user types a question, it is also embedded into a vector.

3. **Semantic Search**  
   - FAISS compares the query vector with all stored vectors to find the most similar ones — **even if your wording is different**.

4. **Prompt Augmentation**  
   - The top matched Q&As are added as context to the GPT prompt.  
   - GPT now responds more accurately and *personally*, even on unseen questions.

5. **Answer Generation**  
   - GPT-4o generates a response based on the context + your query in Kshitij’s tone.

## 🖼 Demo

Here’s how Kshitij AI looks in action:

### 🧪 Interface Sample

![Demo 1](https://github.com/alchemist240/Kshitij-AI/raw/main/assets/Demo1.png)

### 🧠 AI Response Flow

![Demo 2](https://github.com/alchemist240/Kshitij-AI/raw/main/assets/Demo2.png)

---

## 🛠 Tech Stack

| Component         | Tool/Library                          |
|------------------|----------------------------------------|
| UI                | [Streamlit](https://streamlit.io)     |
| LLM               | OpenAI GPT-4o API                     |
| Voice Input       | FFmpeg + Whisper + Streamlit Recorder |
| Semantic Search   | FAISS + SentenceTransformer (MiniLM) |
| Personal Data     | `kshitij_profile.json` (custom)       |
| Vector Embedding  | `all-MiniLM-L6-v2` via `sentence-transformers` |
| Code Structure    | Python 3.11, Modular folders           |

---

## 📬 Final Note

This project is a personal experiment, a creative outlet, and a chance to build something truly *mine*. While it’s not hosted publicly, the code is open for anyone to fork and personalize.

If you’re a dev, a student, or just someone dreaming of building their own AI twin — clone this repo, add your own profile, and go wild.

> Wanna see it live or need help building yours? Just ping me 😉  
> — *Kshitij 🧠💬💪*
