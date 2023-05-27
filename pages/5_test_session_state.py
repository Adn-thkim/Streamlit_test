import streamlit as st

st.session_state.projects = [
    'Boring Project', 'Interesting Project'
]
st.session_state.current_project = st.radio(
    'Select a project to work with:',
    st.session_state.projects,
)