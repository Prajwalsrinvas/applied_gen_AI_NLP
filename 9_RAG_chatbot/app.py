import os

import chromadb
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5-turbo"
# Set up ChromaDB
chroma_db = chromadb.PersistentClient(path="db")
collection = chroma_db.get_or_create_collection("endgame")

# Streamlit app
st.set_page_config(page_title="Avengers Endgame Q&A", page_icon="🎬", layout="wide")

st.title("🎬 Avengers Endgame Q&A")

# User input
query = st.text_input("Ask your question about Avengers Endgame:", key="user_question")

if query:
    with st.spinner("Searching for an answer..."):
        # Query the collection
        results = collection.query(query_texts=[query], n_results=3)

        # Prepare context
        context = "\n\n".join(results["documents"][0])

        # Prepare messages for OpenAI
        messages = [
            {
                "role": "system",
                "content": "You are a helpful expert on the movie 'Avengers Endgame'. Answer the user's question concisely using only the provided information, in well formatted markdown. Provide reasoning for your answer as proof",
            },
            {"role": "user", "content": f"Question: {query}\nInformation: {context}"},
        ]

        # Get response from OpenAI
        response = client.chat.completions.create(model=model, messages=messages)
        content = response.choices[0].message.content

        # Display answer
        st.success(content)
        st.write()
        # Display relevant chunks
        st.subheader("Relevant Script Chunks")
        for i, (doc, metadata) in enumerate(
            zip(results["documents"][0], results["metadatas"][0]), start=1
        ):
            with st.expander(f"Chunk {i} (Page {metadata['page']})"):
                st.write(doc)

# Sidebar
st.sidebar.info(
    "This app uses RAG to answer questions about the Avengers Endgame movie. "
    "It searches through the movie script to find relevant information and generates answers."
)
st.sidebar.title("How to use")
st.sidebar.markdown(
    """
    1. Type your question in the text box
    2. Press Enter or click outside the box
    3. Wait for the LLM to generate an answer
    4. Read the answer and explore the relevant script chunks
    """
)
