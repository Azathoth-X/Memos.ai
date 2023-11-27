import streamlit as st

st.set_page_config(page_title="Memos.Ai",page_icon=":memo:")

st.title("Welcome to Memos.Ai",anchor="")
title=st.text_input("e","bruh",placeholder="password",)


st.write('The current movie title is', title)

st.markdown("")

# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

st.write()