import streamlit as st

# 初始化状态信息
state = st.session_state
if "selected_tab" not in state or state.selected_tab not in ["Steamlit练习", "HomeWork1"]:
    state.selected_tab = "Steamlit练习"  # 默認設置為第一個選項

# 创建选项卡
tabs = ["Steamlit练习", "HomeWork1"]
state.selected_tab = st.sidebar.radio("选择页面", tabs, index=tabs.index(state.selected_tab))

# 页面内容
if state.selected_tab == "Steamlit练习":
    st.title("Steamlit练习")
    # 你在Steamlit练习頁面上的所有代碼...

elif state.selected_tab == "HomeWork1":
    st.title("HomeWork1")
    # 你在HomeWork1頁面上的所有代碼...
