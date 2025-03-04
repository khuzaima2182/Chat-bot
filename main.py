import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key="AIzaSyBrAvVjHduqyQpmeh0wcJ_dT4UBQ6qgEho")

# Initialize the chatbot model
model = genai.GenerativeModel("gemini-2.0-flash")

st.title("Chitral Chatbot")

# Store chat history if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    

    response = model.generate_content(user_input)
    bot_reply = response.text
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
