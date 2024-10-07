import streamlit as st
import openai
import os

# 設置頁面配置
st.set_page_config(page_title="ChatGPT-like clone")

# 設置 API 金鑰
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

# 初始化應用狀態
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"  # 使用聊天模型

if "messages" not in st.session_state:
    st.session_state.messages = []

# 顯示整個聊天紀錄
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 聊天輸入框
if prompt := st.chat_input("What is up?"):
    # 添加用戶輸入的訊息到訊息列表
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 呼叫 OpenAI API 以獲取助手回應
    with st.chat_message("assistant"):
        try:
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=st.session_state.messages
            )
            assistant_reply = response['choices'][0]['message']['content']
            # 添加助手的回應到訊息列表
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
            st.markdown(assistant_reply)

        except Exception as e:
            st.error(f"An error occurred: {e}")

# 聊天記錄上限提示
if len(st.session_state.messages) >= 20:  # 假設設定了 20 條訊息為上限
    st.info(
        """Notice: The maximum message limit for this demo version has been reached. 
        We encourage you to build your own application using Streamlit's tutorial."""
    )
