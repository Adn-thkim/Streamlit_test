from st_pages import add_page_title
import streamlit as st

add_page_title()

treasure = st.radio(
    "우리나라 국보 1호는?",
    ('경복궁', '숭례문', '보신각종'))

if treasure == '숭례문':
    st.write('정답입니다!')
else:
    st.write('틀렸습니다. 다시 한번 풀어보세요.')


if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("라디오 위젯 비활성화", key="disabled")
    st.checkbox("라디오 옵션 수평 정렬", key="horizontal")

with col2:
    st.radio(
        "라벨을 설정해보세요 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )