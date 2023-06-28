from st_pages import add_page_title
import streamlit as st

add_page_title()

check = st.checkbox("체크박스를 선택하세요!!")

if check:
    st.write("체크박스가 선택되었습니다!!")
else:
    st.write("체크박스가 선택되지 않았습니다.")



if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

column_1, column_2 = st.columns(2)

with column_1:
    st.checkbox("selectbox 위젯 비활성화", key="disabled")
    st.radio(
        "selectbox 레이블 옵션 설정하기 🧰",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with column_2:
    option = st.selectbox(
        "당신의 혈액형은 무엇입니까?",
        ("A형", "B형", "AB형","O형"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )