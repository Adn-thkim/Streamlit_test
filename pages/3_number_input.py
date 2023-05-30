import streamlit as st

st.number_input('나이를 입력해주세요.')
st.number_input('나이를 입력해주세요.', step = 1)



st.number_input('나이를 입력해주세요.2', value = 0, step = 5)

value1 = st.number_input("숫자를 입력해주세요.", format="%.2f")

value2 = st.number_input("Enter a number", value = 0, format="%d")

# 천 단위 구분 기호를 포함하여 표시
# value2 = st.number_input("Enter a number", format="{:,d}")

# 백분율로 표시
# value3 = st.number_input("Enter a number", format="{:.2%}")



age = st.number_input('나이를 입력해주세요.', min_value = 0)
age2 = st.number_input('나이를 입력해주세요2.', value = 10)
age3 = st.number_input('나이를 입력해주세요3.', step = 1)
st.write(age2)

user_input = st.number_input("Enter a number", min_value=0)
st.write(user_input)