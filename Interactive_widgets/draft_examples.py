import streamlit as st

color = st.color_picker("색을 선택해주세요!", "#FFFFFF")
st.write("현재 색은", color, "입니다")
st.markdown(f"<p style='color:{color}'>색이 적용된 텍스트입니다.</p>", 
						unsafe_allow_html=True)

# st.title("Text Input")

# name = st.text_input(label='이름을 입력해주세요 🙌')
# st.markdown(f'입력된 이름은 {name}입니다')
# st.write('')
# st.write('')

# def dup_check():
#     if 'email_lst' not in st.session_state:
#         st.session_state.email_lst  = ['weniv@example.com']
    
#     if st.session_state.email in st.session_state.email_lst:
#         st.session_state.email = ''
#         return display_warning()
#     else:
#         st.session_state.email_lst.append(st.session_state.email)

# st.text_input(label='이메일 주소를 입력해주세요',
#               placeholder='weniv@example.com',
#               max_chars=30,
#               key='email',
#               on_change=dup_check
#              )

# def display_warning():
#     col.markdown(':red[이미 사용중인 이메일 주소입니다]')
    
# col, _ = st.columns(2)
# st.markdown(f'입력된 이메일 주소는 {st.session_state.email}입니다')
# st.write('')
# st.write('')

# pw = st.text_input(label='비밀번호를 입력해주세요',
#                    max_chars=16,
#                    type='password')
# st.caption('영문, 한글, 특수문자 조합 16자 이하로 입력해주세요.')
# # st.write('필드에 입력된 비밀번호는 마스킹되지 않은 값으로 저장됩니다.')
# st.write(f'입력된 비밀번호는 {pw}입니다')



# st.title('Text Area')

# st.text_area(label='문의 내용을 입력해주세요', help='영업시간 외 작성된 문의에 대한 답변은 익일 영업시간에 등록될 예정입니다.', key='1')
# st.write('')
# st.write('')

# st.text_area(label='문의 내용을 입력해주세요', height=200, max_chars=1000, key='2')
# st.write('')
# st.write('')

# st.text_area(label='문의 내용을 입력해주세요', height=200, max_chars=1000,
# 			 disabled=True, placeholder='서비스 점검중입니다.', label_visibility="collapsed", key='3')



# st.title('Number Input')

# st.number_input('나이를 입력해주세요.', min_value=0, value=20, step=1, key='4')
# st.write('')
# st.write('')

# st.number_input('몸무게를 입력해주세요.', min_value=0.0, value=50.00, step=0.1, format='%.2f', key='6')
# st.write('')
# st.write('')

# import streamlit as st
# from datetime import time, timedelta
# from datetime import datetime

# step = timedelta(hours=1)  # 1시간 간격으로 슬라이더 이동

# start_time = st.slider(
#     label="언제 시작하시나요?",
#     max_value=datetime(2023, 7, 31, 23, 59),
#     value=datetime(2023, 7, 15, 12, 0),
#     format="MM/DD/YY - HH:mm",
#     step=step)

# st.write("Start time:", start_time)

# color = st.select_slider(label="무지개의 색 중 하나를 골라주세요.",
#     options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
# st.write("제가 가장 좋아하는 무지개색은 ", color,"입니다.")

# start_color, end_color = st.select_slider(
#     label="무지개 색의 범위를 선택해주세요.",
#     options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
#     value=("yellow", "blue"))
# st.write("당신이 선택한 무지개 색의 범위는", start_color, "그리고", end_color, "입니다.")
# # start_color = st.select_slider(
# #     label="무지개 색의 범위를 선택해주세요.",
# #     options=list(range(10)))
# # st.write("당신이 선택한 무지개 색의 범위는", start_color, "그리고")

# appointment = st.slider(
#     label="오늘 점심식사 시간이 몇 시부터 몇 시까지 였나요?",
#     value=(time(11), time(13)))
# st.write("오늘의 점심식사 시간:", appointment)

# import streamlit as st
# import pandas as pd
# from io import StringIO

# uploaded_file = st.file_uploader(label="abc")
# if uploaded_file is not None:
#     # 파일을 바이트로 읽는 방법:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # 문자열 기반 IO파일로 변환하는 방법:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # 파일을 문자열로 읽는 방법:
#     string_data = stringio.read()
#     st.write(string_data)

#     # "파일과 유사한" 개체가 허용되는 모든 곳에서 사용 가능:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)

