import streamlit as st
import random
import pandas as pd
import numpy as np
from PIL import Image

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

    # 在这里放置页面1的内容
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
    use_container_width=True

    # Metrics
    st.metric(label="溫度", value="30 °C", delta="1.2 °C")

    col1, col2, col3 = st.columns(3)
    col1.metric("溫度", "30 °C", "1.2 °C")
    col2.metric("風力", "9 mph", "-8%")
    col3.metric("濕度", "86%", "4%")

    st.metric(label="金價", value=3580, delta=-250, delta_color="inverse")
    st.metric(label="聯發科", value=1100, delta=80, delta_color="inverse")
    st.metric(label="台積電", value=512, delta=0, delta_color="off")

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

    # Displaying an image
    image = Image.open('S__24829963.jpg')
    st.image(image, caption='這是一隻阿拉斯加的照片')

    # 面積圖
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)
    
    # 長條圖
    st.bar_chart(chart_data)

    # 折線圖
    st.line_chart(chart_data)

    # 散點圖
    st.scatter_chart(chart_data)

    # 加上size大小變化
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    chart_data['col4'] = np.random.choice(['A', 'B', 'C'], 20)
    st.scatter_chart(chart_data, x='col1', y='col2', color='col4', size='col3')

    # 地圖的說明 (移除不支援的 size 和 color)
    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(df)

    # 按鈕
    st.button("重設",type="primary")
    if (st.button(":100:我是一個按鈕")):
        st.write("現在按下的是「我是一個按鈕」！！！")
    if (st.button("這是第二個按鈕")):
        st.write("現在按下的是「第二個按鈕」！！！")
    if (st.button(":dart:這是第二個按鈕")):
        st.write("現在按下的是，帶有圖示的「第二個按鈕」！！！")

    # link button，連結按鈕
    st.link_button("前往奇摩首頁", "https://tw.yahoo.com",type="primary",help="hello my friend")
    st.link_button("前往台中科大首頁", "https://www.nutc.edu.tw/",disabled=True)

    # 下載按鈕download button
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

    # 單純的將文字下載，並存成txt檔
    text_contents = '''這就是單純的將文字下載，並存成txt檔'''
    st.download_button('將文字下載', text_contents)

    # 下載圖片
    with open("S__24829963.jpg", "rb") as file:
        btn = st.download_button(
                label="下載圖片",
                data=file,
                file_name="阿拉斯加.jpg",
                mime="image/png"
              )

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

    # Tabs展示
    tab1, tab2, tab3 = st.tabs(["阿拉斯加", "邊境牧羊犬", "柴犬"])
    with tab1:
        st.header("阿拉斯加")
        st.image("S__24829963.jpg")
    with tab2:
        st.header("邊境牧羊犬")
        st.image("images.jpg")
    with tab3:
        st.header("柴犬")
        st.image("S__24829963.jpg")

# HomeWork1 页面
elif state.selected_tab == "HomeWork1":
    st.title("HomeWork1")
    st.write("請上傳您的CSV文件.")

    file = st.file_uploader("選擇文件", type=['csv'])

    if file is not None:
        df = pd.read_csv(file)
        st.write(df)

        selected_column = st.selectbox("選擇要繪製的列", df.columns)

        # 绘制折线图
        st.subheader("折線圖")
        st.write("以下是", selected_column, "的折線圖：")
        st.line_chart(df[selected_column])

        # 绘制面积图
        st.subheader("面積圖")
        st.write("以下是", selected_column, "的面積圖：")
        st.area_chart(df[selected_column])
        
        # 绘制条形图
        st.subheader("長條圖")
        st.write("以下是", selected_column, "的長條圖：")
        st.bar_chart(df[selected_column])

        # 绘制散点图
        st.subheader("散點圖")
        st.write("以下是", selected_column, "的散點圖：")
        st.scatter_chart(df[selected_column])



#sk-proj-4m0hfrpPylVoi429S9JQT3BlbkFJe9aHwIDJzWsp62yz9mz3


import streamlit as st
import openai
import os  # Importing os to access environment variables

st.set_page_config(page_title="Chat GPT-40", page_icon=":robot:", layout="centered")

if 'chats' not in st.session_state:
    st.session_state['chats'] = []

user_input = st.text_input("問我什麼...", key="input")

if st.button("提交"):
    if user_input:  # Check if input is not empty
        st.session_state['chats'].append({"role": "user", "content": user_input})
        openai.api_key = os.getenv('sk-proj-4m0hfrpPylVoi429S9JQT3BlbkFJe9aHwIDJzWsp62yz9mz3')

        response = openai.Completion.create(
            model="gpt-4-0314",
            messages=[
                {"role": "system", "content": "你是世界上最好的社交媒體營銷專家。"},
                {"role": "user", "content": user_input}
            ]
        )

        assistant_reply = response.choices[0].message['content']
        st.session_state['chats'].append({"role": "assistant", "content": assistant_reply})

for chat in st.session_state['chats']:
    st.text_area("", value=f"{chat['role']}: {chat['content']}", height=80, key=f"{chat['role']}_{len(st.session_state['chats'])}")
