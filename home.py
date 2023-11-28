import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title,add_indentation

st.set_page_config(page_title="Memos.Ai",page_icon=":memo:")

st.title("Welcome to Memos.Ai",anchor="")



add_indentation()


show_pages(
    [
        Page("home.py", "Homepage", "🏠"),
        Section("My Notes", icon="📄"),
        # Pages after a section will be indented
        Page("pages/view.py", "Show Notes", "📃"),
        Page("pages/add.py", "New Note", "✍"),
        Page("pages/edit.py", "Edit My Note", "📝"),
        Page("pages/chat.py", "Memos AI", "💬",in_section=False)
    ]
)


st.write()