import streamlit as st

st.code('''st.text_input(label(str),
              value = "object",
              max_chars(int or None),
              key(str or int),
              type("default" or "password"),
              help(str),
              autocomplete(str),
              on_change(callable),
              args(tuple),
              kwargs(dict),
              *, ----> ???
              placeholder(str or None),
              disabled(bool),
              label_visibility("visible", "hidden", "collapsed")''')


'''
Parameters
(참고: https://hello-bryan.tistory.com/387)

label
    A short label explaining to the user what this input is for
    사용자에게 해당 text_input의 입력이 어떤 용도로 사용되는지 설명하는 간단한 레이블입니다
    
    The label can optionally contain Markdown and supports the following elements: Bold, Italics,
    Strikethroughs, Inline Code, Emojis, and Links.
    레이블은 Markdown을 포함할 수 있으며,
    다음 요소들을 지원합니다: 굵은 텍스트, 이탤릭체(기울임), 취소선, 인라인 코드(LaTeX?), 이모지, 링크

    [Abailable label type]
    - Emoji shortcodes, such as :+1: and :sunglasses:. For a list of all supported codes, see
    (https://share.streamlit.io/streamlit/emoji-shortcodes)
    
    - Italic: "This is *italic* text" 값은 Markdown 형식으로 작성되어 있어 이탤릭체(*italic*)가 적용됩니다

    - LaTeX: by wrapping them in "$" or "$$"
    Supported LaTeX functions are listed at (https://katex.org/docs/supported.html)

    - Colored text: using the syntax : color[text to be colored], ex. violet['안녕하세요']
    where color needs to be replaced with any of the following supported colors:
    blue, green, orange, red, violet
    ------------------------------------------------------------------------------------
    !!!!주의!!!!
    //you should never set an empty label// but hide it with label_visibility if needed
    In the future, we may disallow empty labels by raising an exception
    
value
    The text value of this widget when it first renders
    처음 input 위젯이 렌더링될 때 표시하는 값입니다
    이는 내부적으로 str으로 변환될 것입니다

max_chars(아직 예시 x)
    Max number of characters allowed in text input (데이터를 입력 받아야하는 형식이 있을때, 지정할듯?)

key(아직 예시 x)
    An optional string or integer to use as the unique key for the widget
    위젯의 고유한 키로 사용할 선택적인 문자열 또는 정수입니다

    If this is omitted, a key will be generated for the widget based on its content
    이 값이 생략되면 위젯의 내용을 기반으로 키가 생성됩니다

    Multiple widgets of the same type may not share the same key
    동일한 유형의 여러 위젯은 동일한 키를 공유할 수 없습니다

type
    The type of the text input. This can be either "default" (for a regular text input)
    텍스트 입력의 유형입니다. "default"는 일반적인 텍스트 입력을 의미하며, 

    or "password" (for a text input that masks the user's typed value)
    "password"는 사용자가 입력한 값을 마스킹하는 텍스트 입력을 의미합니다

help(아직 예시 x)
    An optional tooltip that gets displayed next to the input
    텍스트 입력 옆에 표시되는 선택적인 툴팁입니다

autocomplete(아직 예시 x)
    An optional value that will be passed to the <input> element's autocomplete property
    <input> 요소의 autocomplete 속성에 전달되는 선택적인 값입니다
    
    If unspecified, this value will be set to "new-password" for "password" inputs,
    지정되지 않은 경우, "password" 입력의 경우 이 값은 "new-password"로 설정되고,
    
    and the empty string for "default" inputs
    "default" 입력의 경우 빈 문자열로 설정됩니다
    
    For more details, see (https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)

on_change(사용법 모르겠음)
    An optional callback invoked when this text input's value changes
    이 텍스트 입력의 값이 변경될 때 호출되는 선택적인 콜백 함수입니다

args
    An optional tuple of args to pass to the callback

kwargs
    An optional dict of kwargs to pass to the callback

placeholder
    An optional string displayed when the text input is empty
    텍스트 입력이 비어있을 때 표시되는 선택적인 문자열입니다
    
    If None, no text is displayed. This argument can only be supplied by keyword
    None인 경우 텍스트가 표시되지 않습니다. 이 인수는 키워드 인수(kwargs)로만 제공할 수 있습니다

disabled
    An optional boolean, which disables the text input if set to True
    선택적으로 사용할 수 있는 부울(boolean) 값으로, True로 설정하면 텍스트 입력을 비활성화합니다
    
    The default is False. This argument can only be supplied by keyword
    기본값은 False입니다. 이 인수는 키워드 인수로만 제공할 수 있습니다

label_visibility
    The visibility of the label
    
    If "hidden", the label doesn't show but there is still empty space for it above the widget (equivalent to label="")
   
    
    If "collapsed", both the label and the space are removed
    
    
    Default is "visible". This argument can only be supplied by keyword.

Returns(str)
    The current value of the text input widget.
'''






# type = 'password' 기능을 이용하면, 사용자가 로그인하는 정보를 기입받는 창으로 이용해서
# DB를 구축해, 사용자가 계정을 생성하고 로그인한 사용자만 대시보드의 민감정보를 확인하도록 할 수 있을듯
# ex. local에 있는 csv에 사용자에게 입력받은 이름, email, password를 저장하고, 로그인할 떄 해당 정보를 비교하여 승인
# 혹은 비밀댓글..?은 안될듯

# placeholder: 기입받을 정보의 형식을 써주면 될듯(보통 생년월일이나 전화번호 기입받을 때)

# Interactive widget을 이용하면 설문조사 형식을 구성할 수 있겠다. 근데 google form이 있는데 굳이...?

txt = st.text_area('Explanation of \"Text_input\" API', '''Text input widgets can customize how to hide their labels with the label_visibility parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to label=""). If "collapsed", both the label and the space are removed. Default is "visible". Text input widgets can also be disabled with the disabled parameter, and can display an optional placeholder text when the text input is empty using the placeholder parameter''')

interpreted_txt = st.text_area('Interpreted explanation of \"Text_input\" API', '''Text_input 위젯은 "label_visibility" 매개변수를 사용하여 스트림릿(Stremlit)의 "text_input"을 숨기는 방법을 사용자 정의할 수 있습니다.
"label_visibility" 매개변수를 "hidden"으로 설정하면 레이블은 표시되지 않지만 위젯 위에는 여전히 레이블을 위한 공간이 있습니다(label=""와 동일).
"collapsed"로 설정하면 레이블과 공간 모두 제거됩니다. 기본값은 "visible"입니다. 텍스트 입력 위젯은 "disabled" 매개변수를 사용하여 비활성화할 수도 있으며(유지보수 측면에서 보면, 배포한 이후 문제가 발생해 일시적으로 해당 text_input에 사용자가 기입하지 못하도록 하는 용도), "placeholder" 매개변수를 사용하여 텍스트 입력이 비어있을 때 선택적인 플레이스홀더 텍스트를 표시할 수도 있습니다.''', height = 500, disabled = True)

#adding a single-line text input widget
title = st.text_input('nothing_parameter', 'write here')


title_hidden = st.text_input('label_visibility: hidden', '', label_visibility = 'hidden')

title_disabled = st.text_input('disabled: True', '', disabled = True)

title_password = st.text_input('type: password', '', type = 'password')

title_placeholder = st.text_input('placeholder', '', placeholder = "write here")











##########################       on_change      #############################
# def handle_text_input_change(new_value):
#     # 값이 변경될 때 실행할 작업을 여기에 작성합니다.
#     st.write("New value:", new_value)
    
# title_onchange = st.text_input('on_change', '', on_change = handle_text_input_change)

# def handle_text_input_change(event):
#     new_value = event.new_value
#     # 값이 변경될 때 실행할 작업을 여기에 작성합니다.
#     st.write("New value:", new_value)

# user_input = st.text_input("Enter text", on_change=handle_text_input_change)
# https://discuss.streamlit.io/t/change-dropdown-options-on-change-in-text-input-widget/27999

def proc():
    # st.write('new_value: ', st.session_state.text_key)
    st.text_input('new_value', st.session_state.text_key)
    # st.write('Done!)

st.text_input('enter text', on_change=proc, key='text_key')

# st.write('interest', st.session_state.text_key)
###############################################################################












'''
text_input은 (동작 설명) 입니다
text_input에는 ... 파라미터를 사용할 수 있습니다
파라미터에 대한 설명
파라미터 설정에 따른 동작을 코드와 실행 결과를 이미지로 제시
살제 사용 예시(대시보드에서), 그 외에도 사용할 수 있는 대안 제시
'''