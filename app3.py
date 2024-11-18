import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(page_title="Pothole Detection", layout="centered")

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'login'  # 초기 페이지 설정

# 페이지 이동 함수
def go_to_page(page_name):
    st.session_state.page = page_name

# 이미지 URL (로고와 배경 이미지)
# background_url = "https://via.placeholder.com/1920x1080?text=Background+Image"
# logo_url = "https://via.placeholder.com/150?text=App+Logo"

# CSS 스타일 추가
def add_custom_css():
    st.markdown(f"""
        <style>
        /* 전체 배경 */
        .stApp {{
            
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Arial', sans-serif;
        }}

        /* 로고와 제목 */
        .logo {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 150px;
        }}
        .title {{
            text-align: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 20px;
        }}

        /* 버튼 스타일 */
        .stButton > button {{
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }}
        .stButton > button:hover {{
            background-color: #45a049;
        }}

        /* 입력 필드 */
        input {{
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            width: 100%;
        }}
        </style>
    """, unsafe_allow_html=True)

# 페이지 레이아웃
def login_page():
    add_custom_css()
    # st.image(logo_url, use_column_width=False, caption="", class_="logo")
    st.markdown('<div class="title">Pothole Detection</div>', unsafe_allow_html=True)

    # 로그인 폼
    st.text_input("아이디", key="login_id")
    st.text_input("비밀번호", type="password", key="login_pw")
    st.button("로그인", on_click=lambda: go_to_page('detection'))

    # 회원가입 및 소셜 로그인
    st.button("회원가입", on_click=lambda: go_to_page('signup'))
    st.markdown("---")
    st.markdown("### SNS 로그인")
    st.button("구글로 로그인")
    st.button("카카오로 로그인")
    st.button("네이버로 로그인")

# 다른 페이지 구성 (회원가입, 감지 등 추가 작업 필요)
def signup_page():
    add_custom_css()
    st.markdown('<div class="title">회원가입</div>', unsafe_allow_html=True)
    st.text_input("아이디", key="signup_id")
    st.text_input("비밀번호", type="password", key="signup_pw")
    st.text_input("비밀번호 확인", type="password", key="signup_pw_confirm")
    st.text_input("이메일", key="signup_email")
    st.button("회원가입 완료", on_click=lambda: go_to_page('login'))

def detection_page():
    add_custom_css()
    st.markdown('<div class="title">Pothole Detection</div>', unsafe_allow_html=True)
    st.button("영상 촬영하기", on_click=lambda: go_to_page('upload'))

def upload_page():
    add_custom_css()
    st.markdown('<div class="title">영상 촬영</div>', unsafe_allow_html=True)
    st.file_uploader("동영상을 업로드해주세요.", type=["mp4", "mov", "avi"])
    st.button("촬영 완료", on_click=lambda: go_to_page('review'))

# 페이지 라우팅
if st.session_state.page == 'login':
    login_page()
elif st.session_state.page == 'signup':
    signup_page()
elif st.session_state.page == 'detection':
    detection_page()
elif st.session_state.page == 'upload':
    upload_page()
