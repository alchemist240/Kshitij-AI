# 🤖 Kshitij AI

Kshitij AI is a personalized GPT-powered assistant designed to behave and respond like a real individual using a structured JSON profile. Inspired by the vision of building your own digital twin, this app lets you create an AI that mimics your personality, interests, style of speaking, and memory — all without training any ML models.

---

## 🧠 What It Does

Kshitij AI reads a custom-built `profile.json` which contains key details about a person — their tone, language, hobbies, education, FAQs, and more. It uses OpenAI’s GPT API to simulate intelligent responses based on that profile.

It's like building your own ChatGPT — but with your memories, values, and unique way of speaking.

---

## ✨ Features

- 💬 Personalized responses using your JSON profile
- 🎯 Context-aware chat that respects tone, goals, and speaking style
- 🔐 Secure secret management via `secrets.toml` (excluded from Git)
- ⚡ Fast response rendering using Streamlit
- 📂 Lightweight structure — easy to modify and deploy

---

## 🖼 Demo

Here’s how Kshitij AI looks in action:

### 🧪 Interface Sample

![Demo 1](assets/demo1.png)

### 🧠 AI Response Flow

![Demo 2](assets/demo2.png)

---

## 🛠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **Backend**: OpenAI GPT API (`openai` Python SDK)
- **Profile Format**: JSON (`profile.json`)
- **Language**: Python 3.x

---

## 📁 Folder Structure

