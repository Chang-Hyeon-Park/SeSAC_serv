import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(page_title="Pothole Detection", layout="centered")

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'login'  # 초기 페이지 설정

# 페이지 이동 함수
def go_to_page(page_name):
    st.session_state.page = page_name

# 뒤로가기 버튼 표시 함수
def back_button(default_page='login'):
    if st.session_state.page != default_page:
        st.button("뒤로가기", on_click=lambda: go_to_previous_page())

# 이전 페이지 관리 (이전 페이지 스택)
if 'page_stack' not in st.session_state:
    st.session_state.page_stack = []

def go_to_previous_page():
    if st.session_state.page_stack:
        st.session_state.page = st.session_state.page_stack.pop()

def go_to_page_with_history(page_name):
    if st.session_state.page != page_name:
        st.session_state.page_stack.append(st.session_state.page)
        st.session_state.page = page_name

# 로그인 페이지
def login_page():
    st.title("Pothole Detection")
    st.subheader("로그인 페이지")
    
    # 로그인 폼
    st.text_input("아이디", key="login_id")
    st.text_input("비밀번호", type="password", key="login_pw")
    st.button("로그인", on_click=lambda: go_to_page_with_history('detection'))
    st.button("회원가입", on_click=lambda: go_to_page_with_history('signup'))

    # 로그인 버튼들 (구현은 하지 않고 버튼만 표시)
    st.markdown("---")
    st.button("구글로 로그인")
    st.button("카카오로 로그인")
    st.button("네이버로 로그인")

# 회원가입 페이지
def signup_page():
    back_button()
    st.title("회원가입")
    st.text_input("아이디", key="signup_id")
    st.text_input("비밀번호", type="password", key="signup_pw")
    st.text_input("비밀번호 확인", type="password", key="signup_pw_confirm")
    st.text_input("이메일", key="signup_email")
    st.button("회원가입 완료", on_click=lambda: go_to_page_with_history('login'))

# Pothole Detection 페이지
def detection_page():
    back_button()
    st.title("Pothole Detection")
    st.button("영상 촬영하기", on_click=lambda: go_to_page_with_history('upload'))

# 촬영 페이지
def upload_page():
    back_button()
    st.title("영상 촬영")
    st.text("촬영 화면이 여기에 표시될 예정입니다.")
    st.file_uploader("동영상을 업로드해주세요.", type=["mp4", "mov", "avi"])
    st.button("촬영 완료", on_click=lambda: go_to_page_with_history('review'))

# 리뷰 페이지
def review_page():
    back_button()
    st.title("촬영된 영상 리스트")
    st.write("아래에서 촬영한 영상들을 확인하고 업로드할 항목을 선택하세요.")
    
    # 예제 데이터 (촬영된 영상 제목)
    video_titles = ["영상1.mp4", "영상2.mp4", "영상3.mp4"]
    selected_videos = []
    
    # 체크박스 형태로 영상 리스트 표시
    for title in video_titles:
        if st.checkbox(title):
            selected_videos.append(title)
    
    # 업로드 버튼
    if selected_videos:
        if st.button("업로드 하기"):
            go_to_page_with_history('uploading')
    else:
        st.write("업로드할 영상을 선택해주세요.")

# 업로드중 페이지
def uploading_page():
    back_button()
    st.title("업로드 중...")
    st.write("선택한 영상들을 서버로 업로드하고 있습니다. 잠시만 기다려주세요...")
    st.button("완료", on_click=lambda: go_to_page_with_history('detection'))

# 페이지 라우팅
if st.session_state.page == 'login':
    login_page()
elif st.session_state.page == 'signup':
    signup_page()
elif st.session_state.page == 'detection':
    detection_page()
elif st.session_state.page == 'upload':
    upload_page()
elif st.session_state.page == 'review':
    review_page()
elif st.session_state.page == 'uploading':
    uploading_page()
