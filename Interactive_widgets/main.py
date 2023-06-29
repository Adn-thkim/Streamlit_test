from st_pages import Page, Section, add_page_title, show_pages, show_pages_from_config
from pathlib import Path
import streamlit as st

# add_page_title()

# -----------------------------------------------------------------------------------------------
# from pathlib import Path
# import streamlit as st

with st.echo("below"):
    from st_pages import Page, Section, add_page_title, show_pages

    # "## Declaring the pages in your app:"

    show_pages(
        [
            # Page("Interactive_widgets/main.py", "Home"),
            # Can use :<icon-name>: or the actual icon
            # Since this is a Section, all the pages underneath it will be indented
            # The section itself will look like a normal page, but it won't be clickable
            Section(name = "Interactive widgets", icon = "⚾️"),
            # The pages appear in the order you pass them
            Page("Interactive_widgets/text_input.py", "Text Input"),
            Page("Interactive_widgets/text_area.py", "Text Area"),
            Page("Interactive_widgets/number_input.py", "Number Input"),
            Page("Interactive_widgets/date_input.py", "Date Input"),
            Page("Interactive_widgets/time_input.py", "Time Input"),
            Page("Interactive_widgets/button.py", "Button"),
            Page("Interactive_widgets/file_uploader.py", "File Uploader"),
            Page("Interactive_widgets/download_button.py", "Download Button"),
            Page("Interactive_widgets/slider.py", "Slider"),
            Page("Interactive_widgets/select_slider.py", "Select Slider"),
            Page("Interactive_widgets/radio.py", "Radio"),
            Page("Interactive_widgets/checkbox.py", "Checkbox"),
            Page("Interactive_widgets/selectbox.py", "Selectbox"),
            Page("Interactive_widgets/multiselect.py", "Multiselect"),
            Page("Interactive_widgets/color.py", "Color Picker"),
            Page("Interactive_widgets/camera_input.py", "Camera Input"),
            Page("Interactive_widgets/data_editor.py", "Data Editor"),
            # Page("Interactive_widgets/4_onchange.py", "On Change"),
            # Section(name="Dashboard_Examples", icon="💼"),
            # Will use the default icon and name based on the filename if you don't
            # pass them
            
            # You can also pass in_section=False to a page to make it un-indented
        ]
    )

    add_page_title()  # Optional method to add title and icon to current page
#     # Also calls add_indentation() by default, which indents pages within a section


# "## Alternative approach, using a config file"

# "Contents of `.streamlit/pages_sections.toml`"

# st.code(Path(".streamlit/pages_sections.toml").read_text(), language="toml")

# "Streamlit script:"

# with st.echo("below"):
#     from st_pages import show_pages_from_config

#     show_pages_from_config(".streamlit/pages_sections.toml")

# "See more at https://github.com/blackary/st_pages"

# with st.expander("Show documentation"):
#     from st_pages import add_indentation

#     st.help(show_pages)

#     st.help(Page)

#     st.help(add_page_title)

#     st.help(Section)

#     st.help(add_indentation)
    
# -------------------------------------------------------------------------------------------------------







st.checkbox("Disable radio widget", help="disabled")






