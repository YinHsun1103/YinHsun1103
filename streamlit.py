import streamlit as st
import random
import pandas as pd
import numpy as np
from PIL import Image


# Page title and initial text
st.title('Hello, streamlit！我的第一支web應用程式開發!!!')
st.write('我是一個字串')
K = 9999
st.write(K)

# Displaying a dataframe with random numbers
dataframe = np.random.randn(10, 20)
st.write(dataframe)

# Markdown examples
st.markdown("# 這是一個示例 Streamlit 網頁")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash; #:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")    

# Titles, headers, and subheaders
st.title("歡迎來到我的網站")
st.title('_Streamlit_ is :blue[cool] :sunglasses:')
st.header("這是一個標頭", divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')
st.subheader("這是一個子標頭", divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

# Captions
st.caption("這是一張美麗的圖片")
st.caption('A caption with italics :blue[colors] and emojis :sunglasses:')

# Displaying code
st.code("print('Hello, Streamlit!')")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, line_numbers=True)    
st.code(code, language='python')

# Plain text
st.text("這是一些純文字內容。")

# LaTeX expressions
st.latex(r"e^{i\pi} + 1 = 0")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# Dividers
st.divider()
st.write("慘了，我被夾在分隔線中間！")
st.divider()

#-----------------------------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------------------------


#面積圖

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

st.area_chart(
   chart_data, x="a", y=["b", "c"], color=["#FF0000", "#00FF00"]  # Optional
)
