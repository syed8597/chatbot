import streamlit as st
from main import get_answer  # Import function from backend script

st.title('KGE Chatbot 🤖')
st.write("Ask me anything related to Gilgit-Baltistan!")

# Chatbot interface
user_input = st.text_input('Ask a question:')
if user_input:
    answer = get_answer(user_input)
    st.write(f'**Answer:** {answer}')
