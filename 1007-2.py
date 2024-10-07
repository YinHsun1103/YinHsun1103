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

# 聊天輸入框
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # 使用 ChatCompletion API 呼叫聊天模型
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=st.session_state.messages
            )
            # 提取助手回應
            assistant_reply = response['choices'][0]['message']['content']
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
