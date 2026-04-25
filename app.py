import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 Local AI Chatbot")
st.caption("Built using Ollama + Streamlit")

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box
user_input = st.chat_input("Ask something...")

if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # System instruction (improves responses)
    system_prompt = "You are a helpful AI assistant. Answer clearly and concisely."

    # Build conversation history
    history = system_prompt + "\n"
    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        history += f"{role}: {msg['content']}\n"

    prompt = history + "Assistant:"

    # Ollama API call
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    # Get response
    with st.spinner("🤔 Thinking..."):
        try:
            response = requests.post(url, json=data, timeout=60)
            result = response.json()
            bot_reply = result.get("response", "⚠️ No response from model")
        except Exception as e:
            bot_reply = f"⚠️ Error: {str(e)}"

    # Store assistant reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    with st.chat_message("assistant"):
        st.write(bot_reply)