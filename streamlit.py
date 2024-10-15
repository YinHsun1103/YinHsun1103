import streamlit as st
import random
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import openai
import os
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# 設置頁面配置
st.set_page_config(page_title="ChatGPT-like clone")

# 定義頁籤選項
tabs = ["Steamlit練習", "HomeWork1", "HomeWork2"]

# 初始化 session state
if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = tabs[0]

# 使用 sidebar 的 radio 選項讓使用者選擇頁面
selected_tab = st.sidebar.radio("選擇頁面", tabs)

# 更新 session_state 的頁籤狀態
st.session_state.selected_tab = selected_tab

# Steamlit練習分頁
if st.session_state.selected_tab == "Steamlit練習":
    st.title("Steamlit練習")

    # 展示 DataFrame 例子
    dataframe = pd.DataFrame(np.random.randn(10, 20), columns=[f"col_{i}" for i in range(20)])
    st.write(dataframe)

    # Markdown 格式化顯示
    st.markdown("# 這是一個示例 Streamlit 網頁")
    st.markdown("Hello, Streamlit! :sunglasses:")

    # 顯示圖片
    try:
        image = Image.open('S__24829963.jpg')
        st.image(image, caption='這是一隻阿拉斯加的照片')
    except FileNotFoundError:
        st.warning("圖片 'S__24829963.jpg' 找不到，請確認圖片是否存在於專案目錄中。")

    # 簡單的數學公式顯示
    st.latex(r"e^{i\pi} + 1 = 0")

    # 示例地圖
    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(df)

# HomeWork1分頁
elif st.session_state.selected_tab == "HomeWork1":
    st.title("HomeWork1  之  可上傳CSV檔")
    file = st.file_uploader("選擇文件", type=['csv'])
    
    if file is not None:
        df = pd.read_csv(file)
        st.write("以下是您上傳的數據：")
        st.write(df)

        # 繪圖
        selected_column = st.selectbox("選擇要繪製的列", df.columns)
        st.subheader(f"{selected_column} 的各種圖表")
        st.line_chart(df[selected_column])
        st.area_chart(df[selected_column])
        st.bar_chart(df[selected_column])

# HomeWork2分頁
elif st.session_state.selected_tab == "HomeWork2":
    st.title("HomeWork2 之 連接Chat GPT")

    # 設置 API 金鑰
    api_key = st.secrets["OPENAI_API_KEY"]
    openai.api_key = api_key

    # 初始化聊天模型
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 聊天輸入框
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

    # 訊息數量上限提示
    if len(st.session_state.messages) >= 20:
        st.info("Notice: The maximum message limit for this demo version has been reached.")

    # 圖表生成和上傳功能
    report_type = st.selectbox("選擇報表類型", ["日報表", "月報表"])

    def generate_chart(report_type):
        fig, ax = plt.subplots()
        data = [10, 20, 30, 40]
        ax.plot(data)
        ax.set_title(f"{report_type} 數據圖表")
        return fig

    chart = generate_chart(report_type)
    st.pyplot(chart)

    if st.button("上傳圖表"):
        buffer = BytesIO()
        chart.savefig(buffer, format="png")
        buffer.seek(0)

        upload_url = "https://your-api-url.com/upload"
        files = {"file": ("chart.png", buffer, "image/png")}
        response = requests.post(upload_url, files=files)

        if response.status_code == 200:
            st.success("圖表已成功上傳至 API！")
        else:
            st.error("圖表上傳失敗。")

    # 呼叫 OpenAI API 生成報表內容
    if st.button("產生報表"):
        report_prompt = f"請生成一份{report_type}報表的摘要和說明。"
        try:
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[{"role": "user", "content": report_prompt}]
            )
            report_content = response['choices'][0]['message']['content']
            st.markdown(report_content)
        except Exception as e:
            st.error(f"報表生成失敗：{e}")
