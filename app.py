import streamlit as st
from src.app.b_primary_model import chat_osagyefo

st.set_page_config(page_title="OSAGYEFO ESQ.")

st.title("🤖 OSAGYEFO ESQ.")
st.markdown("Welcome! Put forth your local legal challenges.")

# Store chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask your legal question here...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call your function
    response = chat_osagyefo(prompt)

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
