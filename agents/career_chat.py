from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config.watson_config import get_llm

memory = ConversationBufferMemory(return_messages=True)
llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI career counselor."),
    MessagesPlaceholder("history"),
    ("human", "{input}")
])
career_chain = prompt | llm

def run_career_chat(user_input: str) -> str:
    # 1) Greeting override before loading memory
    if user_input.strip().lower() in {"hi", "hello", "hey"}:
        memory.clear()  # clear any previous context
        greeting = "Hello! How can I assist you with your career today?"
        memory.save_context({"input": user_input}, {"output": greeting})
        return greeting

    # 2) Normal flow with memory
    past = memory.load_memory_variables({}).get("history", [])
    resp = career_chain.invoke({"input": user_input, "history": past})
    text = getattr(resp, "content", resp)

    memory.save_context({"input": user_input}, {"output": text})
    return text
