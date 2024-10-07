import streamlit as st
import openai
import os

st.set_page_config(page_title="ChatGPT-like clone")

api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key  # 設置 API 金鑰

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = openai.Completion.create(
                model=st.session_state["openai_model"],
                prompt=prompt,
                max_tokens=100
            )
            assistant_reply = response['choices'][0]['text']
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
            st.markdown(assistant_reply)

        except Exception as e:
            st.error(f"An error occurred: {e}")
