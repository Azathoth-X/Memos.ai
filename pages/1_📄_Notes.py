# Import necessary libraries
import streamlit as st
import json

# Function to load notes from a JSON file
def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Function to save notes to a JSON file
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

# Function to display the list of notes
def display_notes(notes):
    st.header("Your Notes")
    if not notes:
        st.write("No notes available.")
    else:
        for i, note in enumerate(notes, start=1):
            st.write(f"**Note {i}:**")
            st.write(f"Title: {note['title']}")
            st.write(f"Content: {note['content']}")
            st.write("---")

# Function to add a new note
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

# Main function
def main():
    st.title("Simple Note-taking App")
    
    # Load existing notes or initialize an empty list
    notes = load_notes()

    # Display existing notes
    display_notes(notes)

    # Allow users to add new notes
    add_note(notes)

if __name__ == "__main__":
    main()
