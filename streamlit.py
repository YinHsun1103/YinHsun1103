import streamlit as st
import random
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
# 初始化状态信息
state = st.session_state
if "selected_tab" not in state:
    state.selected_tab = "页面1"

# 创建选项卡
tabs = ["页面1", "页面2"]
if "selected_tab" not in state:
    state.selected_tab = st.sidebar.radio("选择页面", tabs)
else:
    state.selected_tab = st.sidebar.radio("选择页面", tabs, index=tabs.index(state.selected_tab))

# 页面内容
if state.selected_tab == "页面1":
    st.title("页面1")

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
    st.dataframe(df)  # Same as st.write(df)
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

    # 地圖的說明
    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(df)

    # 定義台北市

    taipei_boundaries = {
        "區域": ["中正區", "大同區", "中山區", "松山區", "大安區", "萬華區", "信義區", "士林區", "北投區", "內湖區", "南港區", "文山區"],
        "西經度": [121.506623, 121.511034, 121.527879, 121.566173, 121.552743, 121.500144, 121.578663, 121.521708, 121.667708, 121.588943, 121.618678, 121.570432],
        "東經度": [121.529235, 121.525196, 121.570859, 121.583734, 121.577419, 121.518360, 121.592992, 121.540610, 121.529424, 121.639907, 121.632538, 121.611367],
        "南緯度": [25.032883, 25.062731, 25.069360, 25.048741, 25.026515, 25.035154, 25.031934, 25.089020, 25.110381, 25.073524, 25.044769, 24.989247],
        "北緯度": [25.041144, 25.066231, 25.080802, 25.050934, 25.041457, 25.046256, 25.050930, 25.146468, 25.153252, 25.123361, 25.091840, 25.006014]
    }

    df_boundaries = pd.DataFrame(taipei_boundaries)
    
    #生成隨機數據，例如人口數
    df_boundaries['人口數'] = np.random.randint(100, 1000, len(df_boundaries))

    #創建一個包含隨機顏色的數據列
    df_boundaries['顏色'] = ['#{:02x}{:02x}{:02x}'.format(np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)) for _ in range(len(df_boundaries))]

    #顯示地圖，將台北市各區域標記在地圖上，大小和顏色表示人口數
    st.map(df_boundaries,
        latitude='南緯度',
        longitude='西經度',
        size='人口數',
        color='顏色'
    )

    st.map(df_boundaries,
        latitude='南緯度',
        longitude='西經度', size=100, color='#0044ff')

#-----------------------------------------------------------------------------------------------------------------------------------------

#按鈕
    st.button("重設",type="primary")
    if (st.button(":100:我是一個按鈕")):
        st.write("現在按下的是「我是一個按鈕」！！！")
    if (st.button("這是第二個按鈕")):
        st.write("現在按下的是「第二個按鈕」！！！")
    if (st.button(":dart:這是第二個按鈕")):
        st.write("現在按下的是，帶有圖示的「第二個按鈕」！！！")

#link button，連結按鈕
    st.link_button("前往奇摩首頁", "https://tw.yahoo.com",type="primary",help="hello my friend")
    st.link_button("前往台中科大首頁", "https://www.nutc.edu.tw/",disabled=True)


#下載按鈕download button
#dataframe下載成csv
    data = {
        'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E']
    }
    my_large_df = pd.DataFrame(data)

#下載按鈕download button
    @st.cache_data
    def convert_df(df):
        #IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(my_large_df)

    st.download_button(
        label="dataframe下載成csv",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv'
    )

#單純的將文字下載，並存成txt檔
    text_contents = '''這就是單純的將文字下載，並存成txt檔'''
    st.download_button('將文字下載', text_contents)

#下載圖片
    with open("S__24829963.jpg", "rb") as file:
        btn = st.download_button(
                label="下載圖片",
                data=file,
                file_name="阿拉斯加.jpg",
                mime="image/png"
              )

#-----------------------------------------------------------------------------------------------------------------------------------------

    st.title('電影標題輸入應用')
    st.write('請在下方輸入電影標題，然後按下確認按鈕。')
    movie_title = st.text_input('輸入電影標題', '今夜作學也會笑', max_chars=15)
    if st.button('確認電影標題'):
        st.write('您選擇的電影標題是：', movie_title)

# Password input section
    st.title('密碼輸入應用')
    st.write('請在下方輸入您的密碼，然後按下確認按鈕。')
    password = st.text_input('輸入密碼', type='password')
    if st.button('確認密碼'):
    # 檢查密碼是否正確
        if password == '88888888':  # 將'88888888'替換為您的實際密碼
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
            st.write(f'您的故事中包含了 {word_count} 3段文字！')
        else:
            st.write('請先輸入您的奇幻故事再按下確認按鈕。')



    number = st.number_input('輸入一個數字', value=None, placeholder='請在這裡輸入...',min_value=0,max_value=100)
    st.write('您輸入的是:', number)


    import datetime

    # Set application title
    st.title('生日輸入應用')

    # Add description text
    st.write('請輸入您的生日日期，然後按下確認按鈕。')

    # Create date input box
    birthday = st.date_input("您的生日日期", datetime.date(1990, 1, 1))

    # Create confirmation button with a unique ID
    if st.button('確認生日'):
        # Display the birthday date
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


    t=st.time_input('設定自動發信的時間',value=None,step=3600)
    st.write('自動發信時間',t)

#-----------------------------------------------------------------------------------------------------------------------------------------



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
        
elif state.selected_tab == "页面2":
    st.title("页面2")
    # 设置应用标题
    st.title("上傳CSV文件並繪製圖表")

    # 添加說明文本
    st.write("請上傳您的CSV文件.")

    # 文件上傳部分
    file = st.file_uploader("選擇文件", type=['csv'])

    if file is not None:
        # 讀取上傳的CSV文件
        df = pd.read_csv(file)

        # 顯示數據
        st.write("以下是您上傳的數據：")
        st.write(df)

        # 選擇要繪製的列
        selected_column = st.selectbox("選擇要繪製的列", df.columns)

        # 繪製折線圖
        st.line_chart(df[selected_column])

        # 面積圖
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.area_chart(chart_data)
        
        # 長條圖
        st.bar_chart(chart_data)

        # 折線圖
        st.line_chart(chart_data)

        # 散點圖
        st.scatter_chart(chart_data)




























