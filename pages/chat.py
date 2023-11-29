from st_pages import add_indentation
import streamlit as st
import json
import os
from dotenv import load_dotenv,dotenv_values
from langchain.vectorstores.qdrant import Qdrant
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
import qdrant_client
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI,HuggingFaceHub

add_indentation()
load_dotenv()

client = qdrant_client.QdrantClient(
    os.getenv("QDRANT_HOST"),
    api_key=os.getenv("QDRANT_API_KEY")
)
collection_config = qdrant_client.http.models.VectorParams(
    size=786, # 768 for instructor-xl, 1536 for OpenAI
    distance=qdrant_client.http.models.Distance.COSINE
)

# st.write(collection_config)
client.recreate_collection(
    collection_name=os.getenv("QDRANT_COLLECTION"),
    vectors_config=collection_config,
)

embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=os.getenv("HF_API_KEY"),
    model_name="BAAI/bge-large-en-v1.5"
)

vectorstore = Qdrant(
    client=client,
    collection_name=os.getenv("QDRANT_COLLECTION_NAME"),
    embeddings=embeddings
)

def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def vectordata():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        st.error("Please add notes to continue")
    
    if st.button("Load Notes to AI"):
        text=[]
        for note in notes:
            text=note['content']
        chunks=get_chunks(text)
        vectorstore.add_texts(chunks)