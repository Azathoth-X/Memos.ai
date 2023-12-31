import streamlit as st
from json_interact import load_notes,save_notes,add_note
from st_pages import add_indentation
st.set_page_config(page_title="Create Notes",page_icon=":memo:")
add_indentation()



def main():
    st.title("Create Note")

    
    # Load existing notes or initialize an empty list
    notes = load_notes()

    add_note(notes)

if __name__ == "__main__":
    main()
