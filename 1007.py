import streamlit as st 
# 設置頁面配置 - 這行必須是程式碼中的第一個 Streamlit 指令
st.set_page_config(page_title="ChatGPT-like clone")

import openai
import os
import random
import pandas as pd
import numpy as np
from PIL import Image

client = openai
api_key = st.secrets["OPENAI_API_KEY"]

# 初始化狀態信息
state = st.session_state
if "selected_tab" not in state:
    state.selected_tab = "Steamlit練習"

# 建立選項卡
tabs = ["Steamlit練習", "HomeWork1"]
state.selected_tab = st.sidebar.radio("選擇頁面", tabs, index=tabs.index(state.selected_tab))

# 檢查並加載圖片的函數
def load_image(file_path, caption):
    if os.path.exists(file_path):
        image = Image.open(file_path)
        st.image(image, caption=caption)
    else:
        st.write(f"Image not found: {file_path}")

# 頁面內容
if state.selected_tab == "Steamlit練習":
    st.title("Steamlit練習")

    # 顯示訊息
    st.title('Hello, streamlit！我的第一支web應用程式開發!!!')
    st.write('我是一個字串')
    K = 9999
    st.write(K)

    dataframe = pd.DataFrame(np.random.randn(10, 20), columns=[f"col_{i}" for i in range(20)])
    st.write(dataframe)

    # MarkDown 樣式
    st.markdown("# 這是一個示例 Streamlit 網頁")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash; #:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    # 各種標題
    st.title("歡迎來到我的網站")
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    st.header("這是一個標頭")
    st.subheader("這是一個子標頭")

    # 顯示程式碼
    st.code("print('Hello, Streamlit!')")
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, line_numbers=True)

    # 數學公式
    st.latex(r"e^{i\pi} + 1 = 0")

    # 分隔線
    st.divider()
    st.write("慘了，我被夾在分隔線中間！")
    st.divider()

    # 隨機 DataFrame
    df = pd.DataFrame(np.random.randn(10, 10), columns=("col %d" % i for i in range(10)))
    st.dataframe(df)
    st.dataframe(df.style.highlight_max(axis=0))

    # 高階 DataFrame 設定
    df = pd.DataFrame({
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    })
    st.dataframe(df)

    # 顯示指標
    st.metric(label="溫度", value="30 °C", delta="1.2 °C")

    # JSON 格式
    data = {
        '姓名': '王小明',
        '年齡': 30,
        '地址': '台北市',
        '學歷': {'學士學位': '資訊科學', '碩士學位': '資訊管理'},
        '興趣': ['運動', '讀書', '旅遊'],
    }
    st.json(data)

    # 顯示圖片 (檢查檔案是否存在)
    load_image('S__24829963.jpg', '這是一隻阿拉斯加的照片')

    # 各種圖表
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)
    st.bar_chart(chart_data)
    st.line_chart(chart_data)
    st.scatter_chart(chart_data)

    # 散點圖加上不同大小
    chart_data['col4'] = np.random.choice(['A', 'B', 'C'], 20)
    st.scatter_chart(chart_data, x='col1', y='col2', color='col4', size='col3')

    # 地圖顯示
    df_map = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(df_map)

    # 按鈕
    if st.button(":100:我是一個按鈕"):
        st.write("現在按下的是「我是一個按鈕」！！！")

    # 連結按鈕
    st.button("前往奇摩首頁", on_click=lambda: st.write("Redirecting to Yahoo"))

    # 下載按鈕 (使用 Cache 加速)
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    data = {'Column1': [1, 2, 3, 4, 5], 'Column2': ['A', 'B', 'C', 'D', 'E']}
    my_large_df = pd.DataFrame(data)
    csv = convert_df(my_large_df)
    st.download_button(label="下載資料框成 CSV", data=csv, file_name='large_df.csv', mime='text/csv')

    # 文字下載成 TXT
    text_contents = '''這就是單純的將文字下載，並存成txt檔'''
    st.download_button('下載文字', text_contents)

# HomeWork1 頁面
elif state.selected_tab == "HomeWork1":
    st.title("HomeWork1")
    st.write("請上傳您的 CSV 文件.")

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
