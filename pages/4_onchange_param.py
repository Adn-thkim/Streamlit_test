import streamlit as st
# session_state https://twitter.com/thedataprof/status/1479378435118026754

# It is very simple to create a web app using Streamlit nowadays, but there are limitations when building something complex.
# One of them is the lack of statefulness because variables in the code will get reinitialize every time we interact with a widget.
# The good news is Streamlit now has native support of session state and callbacks function in their 0.84 release
# https://towardsdatascience.com/advanced-streamlit-session-state-and-callbacks-for-data-labelling-tool-1e4d9ad32a3f



def proc():
    if st.session_state.text_key == 'slider':
        return slider()
    elif st.session_state.text_key == 'code':
        return display_code()
    else:
        st.write('new_value: ', st.session_state.text_key)
    # st.text_input('new_value', st.session_state.text_key)
    # st.write('Done!)

st.text_input('enter text', on_change = proc, key = 'text_key')

def slider():
    age = st.slider('나이가 어떻게 되세요?', 0, 130, 25)
    st.write('저는 ', age, '살 입니다.')


def display_code():
    st.code('''
    def proc():
    if st.session_state.text_key == 'slider':
        return slider()
    elif st.session_state.text_key == 'code':
        return display_code()
    else:
        st.write('new_value: ', st.session_state.text_key)
    # st.text_input('new_value', st.session_state.text_key)
    # st.write('Done!)

st.text_input('enter text', on_change = proc, key = 'text_key')

def slider():
    age = st.slider('나이가 어떻게 되세요?', 0, 130, 25)
    st.write('저는 ', age, '살 입니다.')


def display_code():
    
    ''')


def handle_text_input(value, additional_arg):
    st.write("Input value:", value)
    st.write("Additional argument:", additional_arg)
    # st.write("Keyword argument:", keyword_arg)

additional_arg = "Hello"
keyword_arg = "World"

# user_input = st.text_input("Enter text",callback = handle_text_input,args = additional_arg)
                           # kwargs={"keyword_arg": keyword_arg}
                          

# arg와 kwarg
# callback 함수를 통해 input_text에서 받은 user의 입력값(value)으로 어떠한 이후의 동작을 수행시킬 때,
# 입력받은 value외 callback 함수에 전달해야 하는 parameter가 있을 떄, 사용한다