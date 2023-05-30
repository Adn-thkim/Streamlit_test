import streamlit as st

name = st.text_input('당신의 이름은 무엇입니까?', help="성을 포함한 이름 전체를 입력해주세요")
st.write('User\'s name is ', name)

st.text_input('label_visibility: defulat')

st.text_input(
    label = "**굵은 텍스트**, _기울인 텍스트_, ~~취소선~~, 인라인 코드: $x + y$ ,🙌 이모지 :+1: ,[링크](https://example.com)")

st.text_input('label_visibility: hidden',
              label_visibility = 'hidden')

st.text_input('label_visibility: collapsed',
              label_visibility = 'collapsed')

st.text_input('value',
              'value')

# test_value = st.text_input('value',
#                            1)
# st.write(type(test_value))


#adding a single-line text input widget
title = st.text_input('nothing_parameter', 'write here')



title_disabled = st.text_input('disabled: True', '', disabled = True)

title_password = st.text_input('type: password', '', type = 'password')

title_placeholder = st.text_input('placeholder', '', placeholder = "write here")