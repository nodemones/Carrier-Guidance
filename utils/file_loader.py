from langchain.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.watson_config import get_embeddings

def get_vectorstore():
    loader = PyPDFLoader("data/resume.pdf")
    docs = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(loader.load())
    embeddings = get_embeddings()
    return Chroma.from_documents(docs, embedding=embeddings, persist_directory="resume_db")
