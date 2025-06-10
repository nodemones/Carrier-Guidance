from agents.career_chat import run_career_chat
from agents.resume_rag import run_resume_agent

def career_chain(input_text: str):
    return run_career_chat(input_text)

def resume_chain(input_text: str, resume_text: str):
    return run_resume_agent(input_text, resume_text)
