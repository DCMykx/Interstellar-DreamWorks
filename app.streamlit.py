import streamlit as st

# 设置页面配置
st.set_page_config(page_title="Interstellar DreamWorks", layout="wide")

# 初始化 session_state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# 自定义CSS样式
st.markdown(
    """
    <style>
    .centered-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .centered-text {
        text-align: center;
    }
    .centered-input {
        margin: 0 auto;
        width: 50%;
    }
    .centered-button {
        display: flex;
        justify-content: center;
    }
    .main-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .header-title {
        font-size: 2rem;
        font-weight: bold;
    }
    .header-menu {
        display: flex;
        gap: 2rem;
    }
    .header-menu a {
        text-decoration: none;
        color: #333;
        font-size: 1.2rem;
    }
    .header-menu input {
        margin-left: 2rem;
    }
    .main-content {
        margin-top: 5rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .buttons-container {
        display: flex;
        justify-content: space-around;
        width: 60%;
        margin-top: 2rem;
    }
    .buttons-container button {
        width: 20%;
        padding: 1rem;
        font-size: 1.2rem;
        border: none;
        border-radius: 5px;
        background-color: #4CAF50;
        color: white;
        cursor: pointer;
    }
    .buttons-container button:hover {
        background-color: #45a049;
    }
    .cards-container {
        display: flex;
        justify-content: space-around;
        margin-top: 2rem;
    }
    .card {
        width: 20%;
        padding: 1rem;
        text-align: center;
        border: 1px solid #ddd;
        border-radius: 10px;
    }
    .footer {
        display: flex;
        justify-content: space-around;
        margin-top: 2rem;
        padding: 2rem 0;
        background-color: #f1f1f1;
    }
    .footer div {
        text-align: center;
    }
    .footer img {
        width: 100px;
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 使用 HTML 和 CSS 居中标题
st.markdown('''
    <h1 style="text-align: center;">🤖 Interstellar DreamWorks</h1>
''', unsafe_allow_html=True)

# 页面跳转逻辑
page = st.experimental_get_query_params().get('page', ['home'])[0]
# 更新 session_state 的页面状态
st.session_state.page = page


# 主页面函数
def home_page():
    # 中间内容
    st.image("/home/aistudio/Interstellar_DreamWorks/star.jpg", use_column_width=True)

    # 按钮
    st.markdown('<div class="buttons-container">', unsafe_allow_html=True)

    button_clicked = False
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button('知识学习'):
            button_clicked = "knowledge"
    with col2:
        if st.button('故事生成'):
            button_clicked = "story"
    with col3:
        if st.button('绘本生成'):
            button_clicked = "picture_book"
    with col4:
        if st.button('视频生成'):
            button_clicked = "video"

    # 按钮点击后显示网页内容
    if button_clicked == "knowledge":
        st.markdown('''
                <iframe
                src="https://udify.app/chatbot/hzX6sM1wR2VHgpeZ"
                style="width: 100%; height: 100%; min-height: 700px"
                frameborder="0"
                allow="microphone">
                </iframe>
            ''', unsafe_allow_html=True)
    elif button_clicked == "story":
        st.markdown('''
                <iframe
                src="https://udify.app/workflow/gQWLpy8mg1i1kmVB"
                style="width: 100%; height: 100%; min-height: 700px"
                frameborder="0"
                allow="*">
                </iframe>
            ''', unsafe_allow_html=True)
    elif button_clicked == "picture_book":
        st.markdown('''
                <iframe
                src="https://udify.app/workflow/HtmuPlBYeRV52sZ4"
                style="width: 100%; height: 100%; min-height: 700px"
                frameborder="0"
                allow="*">
                </iframe>
            ''', unsafe_allow_html=True)
    elif button_clicked == "video":
        st.markdown('''
                <iframe
                src="https://example.com/video"
                style="width: 100%; height: 100%; min-height: 700px"
                frameborder="0"
                allow="*">
                </iframe>
            ''', unsafe_allow_html=True)

    # 卡片内容
    st.markdown('''
        <div class="main-content">
            <h3>课程学习</h3>
            <p>Underway...</p>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('''
        <div class="footer">
            <div>
                <p>合作链接</p>
                <p><a href="https://cloud.baidu.com/" target="_blank">百度智能云</a></p>
                <p><a href="http://www.jcph.com/" target="_blank">《十万个为什么》出版社</a></p>
                <p><a href="https://ai.baidu.com/" target="_blank">百度AI开放平台</a></p>
            </div>
            <div>
                <p>关于我们</p>
                <p>加入我们</p>
                <p>联系我们: 15119604921</p>
            </div>
        </div>
    ''', unsafe_allow_html=True)


if st.session_state.page == 'home':
    home_page()
