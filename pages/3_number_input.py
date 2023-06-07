import streamlit as st

st.header('Number Input')

st.subheader('label')

st.number_input('label')

st.subheader('min_value')

st.number_input('min_value', min_value = 0)

st.subheader('max_value')

st.number_input("max_value", max_value = 10)

st.subheader('value')

st.number_input('value', value = 0)

st.subheader('format')

st.number_input("숫자를 입력해주세요.", format="%.2f")

st.subheader('step')

st.number_input('step', step = 1)


st.number_input("Enter a number", value = 0, format="%d")


# 백분율로 표시
# value3 = st.number_input("Enter a number", format="{:.2%}")


# st.balloons()