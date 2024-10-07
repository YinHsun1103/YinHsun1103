import streamlit as st
import openai
import os
import random
import pandas as pd
import numpy as np
from PIL import Image

# 設置頁面配置 - 這行必須是程式碼中的第一個 Streamlit 指令
st.set_page_config(page_title="ChatGPT-like clone")

# 初始化 API 客戶端
client = openai
api_key = st.secrets["OPENAI_API_KEY"]

# 初始化狀態資訊
state = st.session_state
if "selected_tab" not in state:
    state.selected_tab = "Steamlit練習"

# 建立選項卡
tabs = ["Steamlit練習", "HomeWork1"]
state.selected_tab = st.sidebar.radio("選擇頁面", tabs, index=tabs.index(state.selected_tab))

# 檢查圖片是否存在的函數
def load_image(file_path, caption):
    if os.path.exists(file_path):
        image = Image.open(file_path)
        st.image(image, caption=caption)
    else:
        st.write(f"Image not found: {file_path}")

# 頁面內容
if state.selected_tab == "Steamlit練習":
    st.title("Steamlit練習")

    # 顯示基本訊息
    st.title('Hello, streamlit！我的第一支 web 應用程式開發!!!')
    st.write('我是一個字串')
    K = 9999
    st.write(K)

    # 建立並顯示一個 DataFrame
    dataframe = pd.DataFrame(np.random.randn(10, 20), columns=[f"col_{i}" for i in range(20)])
    st.write(dataframe)

    # 標題與樣式
    st.markdown("# 這是一個示例 Streamlit 網頁")
    st.markdown(":red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in] :gray[pretty] :rainbow[colors].")
    st.title("歡迎來到我的網站")

    # 顯示數學公式
    st.latex(r"e^{i\pi} + 1 = 0")

    # 分隔線
    st.divider()
    st.write("慘了，我被夾在分隔線中間！")
    st.divider()

    # 進階的 DataFrame 顯示
    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )
    st.dataframe(df)

    # 顯示指標
    st.metric(label="溫度", value="30 °C", delta="1.2 °C")

    # JSON 格式的顯示
    data = {
        '姓名': '王小明',
        '年齡': 30,
        '地址': '台北市',
        '學歷': {'學士學位': '資訊科學', '碩士學位': '資訊管理'},
        '興趣': ['運動', '讀書', '旅遊'],
    }
    st.json(data)

    # 顯示圖片（檢查路徑）
    load_image('S__24829963.jpg', '這是一隻阿拉斯加的照片')

    # 圖表展示
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

    # 測試按鈕功能
    if st.button(":100:我是一個按鈕"):
        st.write("現在按下的是「我是一個按鈕」！！！")

    # 下載功能
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    data = {'Column1': [1, 2, 3, 4, 5], 'Column2': ['A', 'B', 'C', 'D', 'E']}
    my_large_df = pd.DataFrame(data)
    csv = convert_df(my_large_df)
    st.download_button(label="下載成 CSV", data=csv, file_name='large_df.csv', mime='text/csv')

elif state.selected_tab == "HomeWork1":
    # HomeWork1 頁面
    st.title("HomeWork1")
    st.write("請上傳您的 CSV 文件。")

    file = st.file_uploader("選擇文件", type=['csv'])
    if file is not None:
        df = pd.read_csv(file)
        st.write(df)

        selected_column = st.selectbox("選擇要繪製的列", df.columns)

        # 繪製圖表
        st.subheader("折線圖")
        st.line_chart(df[selected_column])

        st.subheader("面積圖")
        st.area_chart(df[selected_column])
        
        st.subheader("長條圖")
        st.bar_chart(df[selected_column])

        st.subheader("散點圖")
        st.scatter_chart(df[selected_column])
