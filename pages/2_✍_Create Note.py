import streamlit as st
import json


def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def add_note(notes):
    st.header("Add a New Note")
    title = st.text_input("Note Title:")
    content = st.text_area("Note Content:")
    if st.button("Save Note"):
        if title and content:
            new_note = {"title": title, "content": content}
            notes.append(new_note)
            save_notes(notes)
            st.success("Note saved successfully!")
        else:
            st.warning("Please enter both title and content.")


def main():
    st.title("Create Note")
    
    # Load existing notes or initialize an empty list
    notes = load_notes()

    add_note(notes)

if __name__ == "__main__":
    main()
