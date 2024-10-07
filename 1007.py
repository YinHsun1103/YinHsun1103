import streamlit as st
import random
import pandas as pd
import numpy as np
from PIL import Image
import datetime

# 初始化状态信息
state = st.session_state
if "selected_tab" not in state:
    state.selected_tab = "Steamlit练习"

# 创建选项卡
tabs = ["Steamlit练习", "HomeWork1"]
state.selected_tab = st.sidebar.radio("选择页面", tabs, index=tabs.index(state.selected_tab))

# 页面内容
if state.selected_tab == "Steamlit练习":
    st.title("Steamlit练习")

    st.title('Hello, streamlit！我的第一支web應用程式開發!!!')
    st.write('我是一個字串')
    K = 9999
    st.write(K)

    dataframe = pd.DataFrame(np.random.randn(10, 20), columns=[f"col_{i}" for i in range(20)])
    st.write(dataframe)

    st.markdown("# 這是一個示例 Streamlit 網頁")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash; #:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    st.title("歡迎來到我的網站")
    st.header("這是一個標頭")
    st.subheader("這是一個子標頭")

    st.caption("這是一張美麗的圖片")
    st.code("print('Hello, Streamlit!')")

    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, line_numbers=True)

    st.text("這是一些純文字內容。")

    st.latex(r"e^{i\pi} + 1 = 0")
    st.divider()
    st.write("慘了，我被夾在分隔線中間！")
    st.divider()

    df = pd.DataFrame(np.random.randn(10, 10), columns=("col %d" % i for i in range(10)))
    st.dataframe(df.style.highlight_max(axis=0))

    # JSON display
    data = {
        '姓名': '王小明',
        '年齡': 30,
        '地址': '台北市',
        '學歷': {
            '學士學位': '資訊科學',
            '碩士學位': '資訊管理',
        },
        '興趣': [
            '運動',
            '讀書',
            '旅遊',
        ],
    }
    st.json(data)

    # Displaying an image (make sure 'S__24829963.jpg' exists in the app's directory)
    image = Image.open('S__24829963.jpg')
    st.image(image, caption='這是一隻阿拉斯加的照片')

    # Metric example
    st.metric(label="溫度", value="30 °C", delta="1.2 °C")

    # Download button
    data = {
        'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E']
    }
    my_large_df = pd.DataFrame(data)

    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(my_large_df)
    st.download_button(label="dataframe下載成csv", data=csv, file_name='large_df.csv', mime='text/csv')

    # Password input section
    st.title('密碼輸入應用')
    password = st.text_input('輸入密碼', type='password')
    if st.button('確認密碼'):
        if password == '88888888':  
            st.write('密碼正確！歡迎您進入系統。')
        else:
            st.write('密碼錯誤，請檢查後重新輸入。')

    # Other interactive inputs
    st.title('電影標題輸入應用')
    movie_title = st.text_input('輸入電影標題', '今夜作學也會笑', max_chars=15)
    if st.button('確認電影標題'):
        st.write('您選擇的電影標題是：', movie_title)

    number = st.number_input('輸入一個數字', min_value=0, max_value=100)
    st.write('您輸入的是:', number)

    st.title('生日輸入應用')
    birthday = st.date_input("您的生日日期", datetime.date(1990, 1, 1))
    if st.button('確認生日'):
        st.write('您的生日是：', birthday.strftime('%Y年%m月%d日'))

    t = st.time_input('設定自動發信的時間', step=3600)
    st.write('自動發信時間', t)

elif state.selected_tab == "HomeWork1":
    st.title("HomeWork1")
    st.write("請上傳您的CSV文件.")

    file = st.file_uploader("選擇文件", type=['csv'])
    if file is not None:
        df = pd.read_csv(file)
        st.write("以下是您上傳的數據：")
        st.write(df)

        selected_column = st.selectbox("選擇要繪製的列", df.columns)

        st.subheader("折線圖")
        st.line_chart(df[selected_column])

        st.subheader("面積圖")
        st.area_chart(df[selected_column])

        st.subheader("長條圖")
        st.bar_chart(df[selected_column])

        st.subheader("散點圖")
        st.write("此圖僅適用於數值數據列")
