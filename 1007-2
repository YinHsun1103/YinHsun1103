import streamlit as st

# 設置頁面配置 - 這行必須是程式碼中的第一個 Streamlit 指令
st.set_page_config(page_title="ChatGPT-like clone")

import openai
import os

# 初始化 OpenAI 客戶端
client = openai
api_key = st.secrets["OPENAI_API_KEY"]

# 設定初始參數
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "max_messages" not in st.session_state:
    st.session_state.max_messages = 20

# 顯示聊天輸入框
if prompt := st.chat_input("What is up?"):
    # 添加用戶輸入的訊息到訊息列表
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 顯示助手回應的區域
    with st.chat_message("assistant"):
        try:
            # 呼叫 OpenAI API 以獲取助手回應
            response = client.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=st.session_state.messages,
                api_key=api_key
            )
            # 取得助手的回應內容
            assistant_reply = response['choices'][0]['message']['content']
            # 添加助手回應到訊息列表並顯示
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
            st.markdown(assistant_reply)

        except Exception as e:
            # 顯示詳細錯誤訊息
            st.error(f"An error occurred: {e}")

# 檢查聊天記錄是否達到上限，並顯示提示
if len(st.session_state.messages) >= st.session_state.max_messages:
    st.info(
        """Notice: The maximum message limit for this demo version has been reached. 
        We value your interest! For further interactions, consider building your own 
        application using Streamlit's tutorial. Thank you for your understanding."""
    )
