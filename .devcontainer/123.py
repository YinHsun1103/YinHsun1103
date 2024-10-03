import streamlit as st
import pandas as pd
import numpy as np
import random
from PIL import Image

# 初始化状态信息
state = st.session_state
if "selected_tab" not in state:
    state.selected_tab = "Steamlit练习"  # 默認選項

# 创建选项卡
tabs = ["Steamlit练习", "HomeWork1"]
state.selected_tab = st.sidebar.radio("选择页面", tabs, index=tabs.index(state.selected_tab))

# 页面内容
if state.selected_tab == "Steamlit练习":
    st.title("Steamlit练习")
    
    # 示例代碼的頁面內容
    st.title('Hello, streamlit！我的第一支web應用程式開發!!!')
    st.write('我是一個字串')
    K = 9999
    st.write(K)

    dataframe = pd.DataFrame(np.random.randn(10, 20), columns=[f"col_{i}" for i in range(20)])
    st.write(dataframe)

    # Markdowns and other content
    st.markdown("# 這是一個示例 Streamlit 網頁")
    st.markdown("Here's a bouquet 🌸")

    st.title("歡迎來到我的網站")
    st.caption("這是一張美麗的圖片")
    
    # 數據表格和圖表展示
    df = pd.DataFrame(np.random.randn(10, 10), columns=[f"col {i}" for i in range(10)])
    st.dataframe(df.style.highlight_max(axis=0))

    # 地圖部分 - 去除 `size` 和 `color`
    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(df)

    # 按鈕部分
    if st.button(":100:我是一個按鈕"):
        st.write("現在按下的是「我是一個按鈕」！！！")

    # 下載圖片
    with open("S__24829963.jpg", "rb") as file:
        st.download_button(label="下載圖片", data=file, file_name="阿拉斯加.jpg", mime="image/png")

    # 圖片展示
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("阿拉斯加")
        st.image("S__24829963.jpg")
    with col2:
        st.header("邊境牧羊犬")
        st.image("images.jpg")  # 請確保這個文件路徑正確
    with col3:
        st.header("柴犬")
        st.image("S__24829963.jpg")  # 替換為有效的圖片文件

# 上傳文件部分的修正
elif state.selected_tab == "HomeWork1":
    st.title("HomeWork1")
    st.write("請上傳您的CSV文件.")
    
    file = st.file_uploader("選擇文件", type=['csv'])
    if file is not None:
        df = pd.read_csv(file)
        st.write(df)

        selected_column = st.selectbox("選擇要繪製的列", df.columns)
        st.line_chart(df[selected_column])

