
import json
import streamlit as st

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def display_notes(notes):
    st.header("Your Notes")
    if not notes:
        st.write("No notes available.")
    else:
        for i, note in enumerate(notes, start=1):
            st.write(f'''<details><summary><b><h5>{note['title']}</h5></summary></b>
                {note['content']}</details>''',unsafe_allow_html=True)
            st.divider()


def add_note(notes):
    st.header("Add a New Note")
    title = st.text_input("Note Title:")
    content = st.text_area("Note Content:")
    if st.button("Save Note",):
        if title and content:
            new_note = {"title": title, "content": content}
            notes.append(new_note)
            save_notes(notes)
            st.success("Note saved successfully!")
        else:
            st.warning("Please enter both title and content.")

def edit_note(notes):
    
    if not notes:
        st.warning("No notes available to edit.")
        return

    note_titles = [note['title'] for note in notes]

    selected_note_title = st.selectbox("Select a note to edit:", note_titles)

    selected_note = next((note for note in notes if note['title'] == selected_note_title), None)
    st.divider()
    st.subheader(f"{selected_note['title']} \n")
    st.markdown(f"{selected_note['content']}")
    st.divider()
    new_title = st.text_input("New Title:", value=selected_note['title'])
    new_content = st.text_area("New Content:", value=selected_note['content'])

    if st.button("Save Changes"):
        notes[selected_note]['title'] = new_title
        notes[selected_note]['content'] = new_content
        save_notes(notes)
        st.success("Changes saved successfully!")



if __name__ == "__main__":
    ()