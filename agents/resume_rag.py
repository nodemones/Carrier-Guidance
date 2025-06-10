from langchain.chains import RetrievalQA
from utils.file_loader import get_vectorstore
from config.watson_config import get_llm

llm = get_llm()
vectordb = get_vectorstore()

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

def run_resume_agent(user_input: str, resume_text: str) -> str:
    # Simply use the user_input as the "query" for retrieval
    qa_response = qa_chain.invoke({"query": user_input})
    return qa_response["result"]
