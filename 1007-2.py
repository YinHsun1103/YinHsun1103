import streamlit as st
import openai
import os

# 設置頁面配置
st.set_page_config(page_title="ChatGPT-like clone")

client = openai
api_key = st.secrets["OPENAI_API_KEY"]

# 初始化參數
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "max_messages" not in st.session_state:
    st.session_state.max_messages = 20

# 顯示聊天輸入框
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # 更新的 API 請求
            response = client.Completion.create(
                model=st.session_state["openai_model"],
                prompt=prompt,
                api_key=api_key,
                max_tokens=100
            )
            assistant_reply = response['choices'][0]['text']
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
            st.markdown(assistant_reply)

        except Exception as e:
            st.error(f"An error occurred: {e}")

# 提示用戶達到訊息上限
if len(st
