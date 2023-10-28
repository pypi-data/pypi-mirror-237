import openai
import streamlit as st


def WebUI(llm=None):
    with st.sidebar:
        st.write("menu")

    st.title("💬 Chatbot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = llm(prompt)
        msg = {"role": "assistant", "content": response}
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])


