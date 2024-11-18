import streamlit as st

st.header("Images, Video and Audio")

# Image
from PIL import Image
img = Image.open("C:/Users/user/Desktop/pothole_logo.png")
st.image(img, width=300, caption="Pothole Image")

# Video
video_file = open("C:/Users/user/Desktop/Dashcam-Front.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

# Video from an URL
st.video("https://www.youtube.com/watch?v=q2EqJW8VzJo")

# Audio
# audio_file = open("경로", "rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes)

st.header("Widgets")

# Button
if st.button("Play"):
    st.text("Hello World!")

# Checkbox
if st.checkbox("Checkbox"):
    st.text("Checkbox selected")

# Radio Button
radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == "A":
    st.info("You selected A")
else:
    st.info("You selected B")

# Selectbox
city = st.selectbox("Your City", ['Napoli', 'Palermo', 'Catania'])

# Multiselect
occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])

# Text Input
# 단일 행 입력 : 단일 행의 텍스트를 입력받는 데 사용
# 사용자가 입력할 수 있는 텍스트 필드가 한 줄로 제한
# 주 사용 사례 : 이름, 이메일 주소, 단일 라인으로 된 짧은 텍스트 입력을 받을 때 유용
# 기본 제공 옵션 : 기본값 설정, 플레이스홀더(입력 필드에 표시될 힌트 텍스트) 설정 등이 가능
name = st.text_input("Your Name", "Write something...")
st.text(name)

name2 = st.text_input("이름을 기입하세요.", "예) 홍길동...")

# number
number = st.number_input('input number')

# text area
message = st.text_area('문자를 적어주세요', 'Write something...')

# Slider
# 정수로 입력하면 1단위 상승, 소수로 입력하면 소수 단위로 올라감
select_val = st.slider("Select a Value", 1, 10)

# Balloons
if st.button("ballons"):
    st.balloons()

st.header("Dataframes and Tables")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:/Users/user/Downloads/archive (1)/cbb.csv")
st.dataframe(df.head(10))

st.table(df.head(10))

# Plottings
st.area_chart(df[['G', 'W']])
st.bar_chart(df[['G', "W"]].head(20))
st.line_chart(df[['G', 'W']].head(20))

fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[['G', 'W']].corr(), annot=True)
st.pyplot(fig)


import datetime

today = st.date_input("Today is", datetime.datetime.now())

import time

hour = st.time_input("The time is", datetime.time(12, 30))

# Display Json Code

data = {"name" : "John", "surname" : "Wick"}
st.json(data)

# Displaying CODE
st.code("import pandas as pd")

julia_code = """
function doit(num::int)
    println(num)
end
"""

st.code(julia_code, language='julia')

st.header("Progress Bar and Spinner")

# Progress Bar
my_bar = st.progress(0)
for value in range(100):
    time.sleep(1)
    my_bar.progress(value+1)

with st.spinner("Please wait..."):
    time.sleep(3)

st.success("Done!")