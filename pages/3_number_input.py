import streamlit as st

st.number_input('label')

st.number_input('min_value', min_value = 0)

st.number_input("max_value", max_value = 10)

st.number_input('value', value = 0)

st.number_input("format", format="%.2f")

st.number_input('step', step = 1)

st.number_input("Enter a number", value = 0, format="%d")


# 백분율로 표시
# value3 = st.number_input("Enter a number", format="{:.2%}")


# st.balloons()