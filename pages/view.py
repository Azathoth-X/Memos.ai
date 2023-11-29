# Import necessary libraries
import streamlit as st
import json
from json_interact import load_notes,display_notes
from st_pages import add_indentation
st.set_page_config(page_title="View Notes",page_icon=":memo:")
add_indentation()


def main():
    st.title("Simple Note-taking App")
    notes = load_notes()
    display_notes(notes)

if __name__ == "__main__":
    main()
