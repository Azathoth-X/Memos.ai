import streamlit as st
from json_interact import load_notes
from st_pages import add_indentation
import requests
from dotenv import load_dotenv
import os
load_dotenv()
add_indentation()

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers={"Authorization":os.getenv("HF_API")}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def summarynote(notes):
    if not notes:
        st.warning("No notes available to edit.")
        return

    note_titles = [note['title'] for note in notes]

    selected_note_title = st.selectbox("Select a note to edit:", note_titles)

    selected_note_index = next((index for index, note in enumerate(notes) if note['title'] == selected_note_title), None)

    if selected_note_index is not None:
        selected_note = notes[selected_note_index]
        st.divider()
        st.subheader(f"{selected_note['title']} \n")
        st.markdown(f"{selected_note['content']}")

        if st.button("Summarize Note"):
            with st.spinner("Loading..."):
                 output = query({"inputs": selected_note['content']})
            sum_note=output[0]["summary_text"]
            st.subheader(f"{selected_note['title']} \n")
            st.write(sum_note)

def main():
    notes=load_notes()
    summarynote(notes)

if __name__=="__main__":
    main()