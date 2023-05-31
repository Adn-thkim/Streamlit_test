import streamlit as st
import numpy as np
import time

text = st.text_area(label = 'label')
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_area('label_visibility: hidden',
              label_visibility = 'hidden')
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_area('label_visibility: collapsed',
              label_visibility = 'collapsed')
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_area('value',
              'value')
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_area(label = 'height', height = 200)
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_area('이메일 주소를 입력해주세요.',
			  placeholder = 'likelion@likelion.org')
st.write('필드에 입력된 값은 ', text, '입니다')

name = st.text_area('당신의 이름은 무엇입니까?', help="성을 포함한 이름 전체를 입력해주세요")
st.write('User\'s name is ', name)

text = st.text_area('max_chars', max_chars = 30)
st.write('필드에 입력된 값은 ', text, '입니다')

text = st.text_area('disabled: True', '', disabled = True)
st.write('필드에 입력된 값은 ', text, '입니다')