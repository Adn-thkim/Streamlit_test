import streamlit as st

text = st.text_input('label_visibility: defulat')
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_input(
    label = "**굵은 텍스트**, _기울인 텍스트_, ~~취소선~~, 인라인 코드: $x + y$ ,🙌 이모지 :+1: ,[링크](https://example.com)")
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_input('label_visibility: hidden',
              label_visibility = 'hidden')
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_input('label_visibility: collapsed',
              label_visibility = 'collapsed')
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_input('value',
                     'value')
st.write('필드에 입력된 값은 ', text, '입니다')

test_value = st.text_input('value', 1)
# 필드에 입력한 값이 str 타입으로 변환되어 test_value에 저장됨
# test_value * 2의 결과값은 test_value를 반복 출력하는 형태
st.write(test_value * 2)

text = st.text_input('이메일 주소를 입력해주세요.',
			  placeholder = 'likelion@likelion.org')
st.write('필드에 입력된 값은 ', text, '입니다')

name = st.text_input('당신의 이름은 무엇입니까?', help="성을 포함한 이름 전체를 입력해주세요")
st.write('입력된 이름은 ', name, '입니다')

text = st.text_input('text_input', max_chars = 30)
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_input('type: password', '', type = 'password')
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_input('disabled: True', '', disabled = True)
st.write('필드에 입력된 값은 ', text, '입니다')