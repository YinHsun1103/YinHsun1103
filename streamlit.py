import streamlit as st  # 匯入 Streamlit 庫，用於創建網頁應用
import random  # 匯入 random 庫，提供隨機數生成功能
import pandas as pd  # 匯入 Pandas 庫，用於資料處理與分析
import numpy as np  # 匯入 NumPy 庫，用於數值計算
from PIL import Image  # 從 PIL 庫匯入 Image 模組，用於處理圖像
import datetime  # 匯入 datetime 庫，用於時間和日期的操作
import openai  # 匯入 OpenAI 庫，用於與 OpenAI 的 API 進行互動，例如 GPT 模型的使用
import os      # 匯入 os 庫，用於操作系統層級的功能，例如環境變數管理、文件路徑操作等

# 設置頁面配置
st.set_page_config(page_title="ChatGPT-like clone")

# 定義頁籤選項
tabs = ["Steamlit練習", "HomeWork1", "HomeWork2"]

# 初始化 session state
if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = tabs[0]

selected_tab = st.sidebar.radio("選擇頁面", tabs)

st.session_state.selected_tab = selected_tab


st.session_state.selected_tab == "HomeWork2":
    st.title("HomeWork2 之 連接Chat GPT")

    # 設置 API 金鑰
    openai.api_key = "sk-svcacct-fb_-GzpFTmE6wtv222EkZdGrZrVUnZdTIP-AkvTvtcxO8n7D-tZvHHAL6ChEGT3BlbkFJCwdg-PbyzjyhbVo99UJNUKYTHayGD-I0QpeVibX_K7x6F8UE9Q7j0flr-VmAA"
    openai.api_base = "https://api.openai.com/v1"  # 設定 OpenAI API base URL

    # 呼叫 OpenAI API ChatCompletion，使用 gpt-4o-mini 模型
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # 使用 gpt-4o-mini 模型
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    )

    assistant_reply = response['choices'][0]['message']['content']  # 取得助手的回應內容
    st.write(assistant_reply)

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o-mini"  # 使用 gpt-4o-mini 作為預設模型

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 顯示所有聊天記錄
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 用戶輸入新的訊息
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = openai.ChatCompletion.create(
                    model=st.session_state["openai_model"],
                    messages=st.session_state.messages
                )
                assistant_reply = response['choices'][0]['message']['content']
                st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
                st.markdown(assistant_reply)

            except Exception as e:
                st.error(f"An error occurred: {e}")

    # 聊天記錄上限提示
    if len(st.session_state.messages) >= 20:
        st.info(
            """Notice: The maximum message limit for this demo version has been reached. 
            We encourage you to build your own application using Streamlit's tutorial."""
        )
