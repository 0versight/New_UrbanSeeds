import streamlit as st
import backend_Chatbot as demo

st.title("Hi, This is UrbanSeeds for you all")

# Initialize session state variables if they don't exist
if "memory" not in st.session_state:
    st.session_state.memory = demo.demo_memory()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Input text from user
input_text = st.chat_input("What is up?")
if input_text:
    # Display user message
    with st.chat_message("user"):
        st.markdown(input_text)
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Get chat response from the backend
    chat_response = demo.demo_conversation(input_text=input_text, memory=st.session_state.memory)

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(chat_response)
    
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
