# 🤖 Local AI Chatbot (Ollama + Streamlit)

## 📌 Overview
This project is a conversational AI chatbot built using a local Large Language Model (LLM).  
It runs completely offline using Ollama and provides a simple ChatGPT-like interface with memory.

---

## 🚀 Features
- 💬 Chat-based interface
- 🧠 Conversation memory (context-aware responses)
- ⚡ Fast local inference (no API cost)
- 🧹 Clear chat functionality
- ⚠️ Error handling for stable performance
- 🎨 Clean UI using Streamlit

---

## 🛠️ Tech Stack
- Python
- Streamlit (UI)
- Ollama (local LLM - Llama 3)
- Requests (API communication)

---

## 📂 Project Structure

ai-chatbot-ollama/
│── app.py
│── requirements.txt
│── README.md
│── screenshot.png


---

## ▶️ How to Run

### 1️⃣ Install Ollama
Download and install from: https://ollama.com/

Run the model:

ollama run llama3


---

### 2️⃣ Install dependencies

pip install streamlit requests


---

### 3️⃣ Run the app

streamlit run app.py


---

### 4️⃣ Open in browser

http://localhost:8501


---

## 📷 Demo
![Chatbot Screenshot](screenshot.png)

---

## 🧠 How It Works
- User enters a message in the UI
- Chat history is stored using Streamlit session state
- Full conversation is sent to the LLM as context
- Ollama processes the prompt locally
- Response is displayed in the chat interface

---

## 💡 Future Improvements
- 📄 PDF chatbot (RAG)
- 🎤 Voice input/output
- 🌐 Deploy online
- 🧩 Multi-model support

---

## 💼 Resume Description
**AI Chatbot with Memory (Ollama + Streamlit)**  
- Built a conversational AI chatbot using a local LLM (Llama 3)  
- Implemented memory for context-aware responses  
- Designed an interactive UI using Streamlit  
- Integrated REST API for real-time AI responses  
- Managed project using Git and GitHub  

---

## 👤 Author
Kumar Kalepu