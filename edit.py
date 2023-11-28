import streamlit as st
import json
from json_interact import load_notes,save_notes,edit_note
from st_pages import add_indentation

add_indentation()

def main():
    st.title("Edit Note App")
    
    
    notes = load_notes()

    
    edit_note(notes)

if __name__ == "__main__":
    main()
