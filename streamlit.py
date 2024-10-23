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

if st.session_state.selected_tab == "Steamlit練習":
    st.title("Steamlit練習")
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
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    st.header("這是一個標頭", divider='rainbow')
    st.header('_Streamlit_ is :blue[cool] :sunglasses:')
    st.subheader("這是一個子標頭", divider='rainbow')
    st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
    st.caption("這是一張美麗的圖片")
    st.caption('A caption with italics :blue[colors] and emojis :sunglasses:')
    st.code("print('Hello, Streamlit!')")
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, line_numbers=True)    
    st.code(code, language='python')
    st.text("這是一些純文字內容。")
    st.latex(r"e^{i\pi} + 1 = 0")
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

    st.divider()
    st.write("慘了，我被夾在分隔線中間！")
    st.divider()
    df = pd.DataFrame(np.random.randn(10, 10), columns=("col %d" % i for i in range(10)))
    st.dataframe(df)
    st.dataframe(df.style.highlight_max(axis=0))

    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )

    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn("App URL"),
            "views_history": st.column_config.LineChartColumn(
                "Views (past 30 days)", y_min=0, y_max=5000
            ),
        },
        hide_index=True
    )
    use_container_width = True

    st.metric(label="溫度", value="30 °C", delta="1.2 °C")
    col1, col2, col3 = st.columns(3)
    col1.metric("溫度", "30 °C", "1.2 °C")
    col2.metric("風力", "9 mph", "-8%")
    col3.metric("濕度", "86%", "4%")
    st.metric(label="金價", value=3580, delta=-250, delta_color="inverse")
    st.metric(label="聯發科", value=1100, delta=80, delta_color="inverse")
    st.metric(label="台積電", value=512, delta=0, delta_color="off")

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

    image = Image.open('S__24829963.jpg')
    st.image(image, caption='這是一隻阿拉斯加的照片')

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)
    st.bar_chart(chart_data)
    st.line_chart(chart_data)
    st.scatter_chart(chart_data)

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    chart_data['col4'] = np.random.choice(['A', 'B', 'C'], 20)
    st.scatter_chart(chart_data, x='col1', y='col2', color='col4', size='col3')

    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(df)

    st.button("重設", type="primary")
    if st.button(":100:我是一個按鈕"):
        st.write("現在按下的是「我是一個按鈕」！！！")
    if st.button("這是第二個按鈕"):
        st.write("現在按下的是「第二個按鈕」！！！")
    if st.button(":dart:這是第二個按鈕"):
        st.write("現在按下的是，帶有圖示的「第二個按鈕」！！！")

    st.link_button("前往奇摩首頁", "https://tw.yahoo.com", type="primary", help="hello my friend")
    st.link_button("前往台中科大首頁", "https://www.nutc.edu.tw/", disabled=True)

    data = {
        'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E']
    }
    my_large_df = pd.DataFrame(data)

    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(my_large_df)

    st.download_button(
        label="dataframe下載成csv",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv'
    )

    text_contents = '''這就是單純的將文字下載，並存成txt檔'''
    st.download_button('將文字下載', text_contents)

    with open("S__24829963.jpg", "rb") as file:
        btn = st.download_button(
            label="下載圖片",
            data=file,
            file_name="阿拉斯加.jpg",
            mime="image/png"
        )

    st.title('電影標題輸入應用')
    st.write('請在下方輸入電影標題，然後按下確認按鈕。')
    movie_title = st.text_input('輸入電影標題', '今夜作學也會笑', max_chars=15)
    if st.button('確認電影標題'):
        st.write('您選擇的電影標題是：', movie_title)

    st.title('密碼輸入應用')
    st.write('請在下方輸入您的密碼，然後按下確認按鈕。')
    password = st.text_input('輸入密碼', type='password')
    if st.button('確認密碼'):
        if password == '88888888':
            st.write('密碼正確！歡迎您進入系統。')
        else:
            st.write('密碼錯誤，請檢查後重新輸入。')

    st.title('創意文字分析應用')
    st.write('在下方的文字區域中，輸入您的奇幻故事，然後按下確認按鈕。')
    story_text = st.text_area('輸入您的奇幻故事', max_chars=100)
    if st.button("確認"):
        if story_text:
            words = story_text.split(" ")
            word_count = len(words)
            st.write(f'您的故事中包含了 {word_count} 段文字！')
        else:
            st.write('請先輸入您的奇幻故事再按下確認按鈕。')

    number = st.number_input('輸入一個數字', value=None, placeholder='請在這裡輸入...', min_value=0, max_value=100)
    st.write('您輸入的是:', number)

    st.title('生日輸入應用')
    st.write('請輸入您的生日日期，然後按下確認按鈕。')
    birthday = st.date_input("您的生日日期", datetime.date(1990, 1, 1))
    if st.button('確認生日'):
        st.write('您的生日是：', birthday.strftime('%Y年%m月%d日'))

    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)
    d = st.date_input(
        "選擇明年要休假的期間",
        (jan_1, datetime.date(next_year, 1, 7)),
        min_value=jan_1,
        max_value=dec_31,
        format="YYYY-MM-DD"
    )
    d

    t = st.time_input('設定自動發信的時間', value=None, step=3600)
    st.write('自動發信時間', t)

    col1, col2, col3 = st.columns(3)

    with col1:
       st.header("阿拉斯加")
       st.image("S__24829963.jpg")

    with col2:
       st.header("邊境牧羊犬")
       st.image("images.jpg")

    with col3:
       st.header("柴犬")
       st.image("1a0ec01465964e9fa986689864e47f3d_th.jpg.crdownload")

    tab1, tab2, tab3 = st.tabs(["阿拉斯加", "邊境牧羊犬", "柴犬"])

    with tab1:
        st.header("阿拉斯加")
        st.image("S__24829963.jpg")

    with tab2:
        st.header("邊境牧羊犬")
        st.image("images.jpg")

    with tab3:
        st.header("柴犬")
        st.image("1a0ec01465964e9fa986689864e47f3d_th.jpg.crdownload")

# ---------------------------------------------------------------------------------------------------------------
elif st.session_state.selected_tab == "HomeWork1":
        st.title("HomeWork1  之  可上傳CSV檔")
        st.write("請上傳您的CSV文件.")

        file = st.file_uploader("選擇文件", type=['csv'])
    
        if file is not None:
            df = pd.read_csv(file)
            st.write("以下是您上傳的數據：")
            st.write(df)

            selected_column = st.selectbox("選擇要繪製的列", df.columns)

            st.subheader("折線圖")
            st.write("以下是", selected_column, "的折線圖：")
            st.line_chart(df[selected_column])

            st.subheader("面積圖")
            st.write("以下是", selected_column, "的面積圖：")
            st.area_chart(df[selected_column])

            st.subheader("長條圖")
            st.write("以下是", selected_column, "的長條圖：")
            st.bar_chart(df[selected_column])

            st.subheader("散點圖")
            st.write("以下是", selected_column, "的散點圖：")
            st.scatter_chart(df[selected_column])

#-----------------------------------------------------------------------------------------------------------------------------------------
elif st.session_state.selected_tab == "HomeWork2":
    st.title("HomeWork2 之 連接Chat GPT")

    # 設置 API 金鑰
    openai.api_key = "sk-svcacct-fb_-GzpFTmE6wtv222EkZdGrZrVUnZdTIP-AkvTvtcxO8n7D-tZvHHAL6ChEGT3BlbkFJCwdg-PbyzjyhbVo99UJNUKYTHayGD-I0QpeVibX_K7x6F8UE9Q7j0flr-VmAA"
    openai.api_base = "https://api.openai.com/v1"  # 設定 OpenAI API base URL

    # 呼叫 OpenAI API ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # 使用你指定的模型
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
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

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

    if len(st.session_state.messages) >= 20:
        st.info(
            """Notice: The maximum message limit for this demo version has been reached. 
            We encourage you to build your own application using Streamlit's tutorial."""
        )
