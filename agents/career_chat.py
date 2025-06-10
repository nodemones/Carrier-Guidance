from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config.watson_config import get_llm
from tavily import TavilyClient
import os

# Initializ
memory = ConversationBufferMemory(return_messages=True)
llm = get_llm()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Updated Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI career counselor. If relevant information is provided from the web, use it."),
    MessagesPlaceholder("history"),
    ("human", "{input}\n\nWeb Results:\n{web_context}")
])
career_chain = prompt | llm

def search_web(query: str) -> str:
    try:
        results = tavily.search(query=query, search_depth="advanced", max_results=3)
        return "\n\n".join([f"- {res['content']}" for res in results["results"]])
    except Exception as e:
        return "No real-time data available at the moment."

def run_career_chat(user_input: str) -> str:
    if user_input.strip().lower() in {"hi", "hello", "hey"}:
        memory.clear()
        greeting = "Hello! How can I assist you with your career today?"
        memory.save_context({"input": user_input}, {"output": greeting})
        return greeting

    # Load history
    past = memory.load_memory_variables({}).get("history", [])

    # Fetch real-time context
    web_context = search_web(user_input)

    # Generate response
    resp = career_chain.invoke({
        "input": user_input,
        "history": past,
        "web_context": web_context
    })
    text = getattr(resp, "content", resp)

    # Save interaction to memory
    memory.save_context({"input": user_input}, {"output": text})
    return text