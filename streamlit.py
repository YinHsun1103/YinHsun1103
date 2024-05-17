import streamlit as st
import numpy as np
st.title('Hello,streamlit！我的第一支web應用程式開發!!!')
st.write('我是一個字串')
K = 9999
st.write(K)

dotaframe = np.random.randn(10,20)
st.write(dotaframe)


#網頁標題
st.markdown("# 這是一個示例 Streamlit 網頁")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            #:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")    

#主標題
st.title("歡迎來到我的網站")
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

#標頭
st.header("這是一個標頭", divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

#子標頭
st.subheader("這是一個子標頭", divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

#圖片說明
st.caption("這是一張美麗的圖片")
st.caption('A caption with italics :blue[colors] and emojis :sunglasses:')

#顯示程式碼, language參考 https://github.com/react-syntax-highl...
st.code("print('Hello, Streamlit!')")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, line_numbers=True)    

st.code(code, language='python')

#文字
st.text("這是一些純文字內容。")

#數學 LaTeX 表達式
st.latex(r"e^{i\pi} + 1 = 0")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

#分隔線
st.divider()
st.write("慘了，我被夾在分隔線中間！")
st.divider()

#添加中文註解
st.write("希望這些示例有助於您建立令人印象深刻的 Streamlit 網頁！")
