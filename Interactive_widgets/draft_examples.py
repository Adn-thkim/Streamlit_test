import streamlit as st

st.title("Text Input")

name = st.text_input(label='이름을 입력해주세요 🙌')
st.markdown(f'입력된 이름은 {name}입니다')
st.write('')
st.write('')

def dup_check():
    if 'email_lst' not in st.session_state:
        st.session_state.email_lst  = ['weniv@example.com']
    
    if st.session_state.email in st.session_state.email_lst:
        st.session_state.email = ''
        return display_warning()
    else:
        st.session_state.email_lst.append(st.session_state.email)

st.text_input(label='이메일 주소를 입력해주세요',
              placeholder='weniv@example.com',
              max_chars=30,
              key='email',
              on_change=dup_check
             )

def display_warning():
    col.markdown(':red[이미 사용중인 이메일 주소입니다]')
    
col, _ = st.columns(2)
st.markdown(f'입력된 이메일 주소는 {st.session_state.email}입니다')
st.write('')
st.write('')

pw = st.text_input(label='비밀번호를 입력해주세요',
                   max_chars=16,
                   type='password')
st.caption('영문, 한글, 특수문자 조합 16자 이하로 입력해주세요.')
# st.write('필드에 입력된 비밀번호는 마스킹되지 않은 값으로 저장됩니다.')
st.write(f'입력된 비밀번호는 {pw}입니다')



st.title('Text Area')
st.write('')
st.write('')

st.text_area(label='문의 내용을 입력해주세요', help='영업시간 외 작성된 문의에 대한 답변은 익일 영업시간에 등록될 예정입니다.', key='1')
st.text_area(label='문의 내용을 입력해주세요', height=200, max_chars=1000, key='2')
st.text_area(label='문의 내용을 입력해주세요', height=200, max_chars=1000,
			 disabled=True, placeholder='서비스 점검중입니다.', label_visibility="collapsed", key='3')



st.title('Number Input')

st.number_input('나이를 입력해주세요.', min_value=0, value=20, step=1, key='4')
st.number_input('키를 입력해주세요.', min_value=0, value=170, step=1, key='5')
st.number_input('몸무게를 입력해주세요.', min_value=0.0, value=50.00, step=0.1, format='%.2f', key='6')


