import gradio as gr
from app import career_chain, resume_chain
import PyPDF2
from tempfile import NamedTemporaryFile

def extract_pdf_text(file_bytes: bytes) -> str:
    with NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(file_bytes)
        tmp.flush()
        reader = PyPDF2.PdfReader(tmp.name)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

def unified_chat(message, history, resume_file):
    history = history or []
    history.append({"role": "user", "content": message})

    resume_text = None
    if resume_file:
        # resume_file is bytes directly
        resume_text = extract_pdf_text(resume_file)

    if resume_text:
        reply = resume_chain(message, resume_text)
    else:
        reply = career_chain(message)

    history.append({"role": "assistant", "content": reply})
    return "", history

import gradio as gr
from app import career_chain, resume_chain
import PyPDF2
from tempfile import NamedTemporaryFile

# Helper to extract text from uploaded PDF file
def extract_pdf_text(file_path: str) -> str:
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

# Unified chatbot function
def unified_chat(input_data, history):
    text = input_data.get("text", "").strip()
    files = input_data.get("files", [])
    resume_text = None

    if not text and not files:
        return "", history  # Don't process if nothing provided

    if files:
        resume_text = extract_pdf_text(files[0])

    if resume_text:
        reply = resume_chain(text, resume_text)
    else:
        reply = career_chain(text)

    history = history or []
    history.append({"role": "user", "content": text})
    history.append({"role": "assistant", "content": reply})
    return "", history

# --- Gradio UI ---
with gr.Blocks(theme=gr.themes.Soft(), title="GUIDE Chatbot") as demo:
    with gr.Column(elem_id="col-container"):
        gr.HTML(
        """
        <div style="text-align: center; max-width: 700px; margin: 0 auto;">
            <div style="display: inline-flex; align-items: center; gap: 0.8rem; font-size: 1.75rem;">
               <h1 style="font-weight: 900; margin-bottom: 7px;">
               🎓 GUIDE: Growth-based Unified Intelligent Direction Engine
               </h1>
            </div>
            <p style="margin-bottom: 10px; font-size: 1.1rem; color: #606060;">
            Upload your resume (optional) with your question for personalized career advice.
            </p>
        </div>
        """
        )
        chatbot = gr.Chatbot(
            label="GUIDE Chat Assistant",
            type="messages",
            height=500,
            show_copy_button=True,
            bubble_full_width=False
        )
        chat_input = gr.MultimodalTextbox(
            interactive=True,
            file_types=[".pdf"],
            placeholder="Enter your question or upload PDF and ask...",
            show_label=False
        )
        clear_button = gr.Button("Clear Chat", variant="secondary")

    # --- Event Handlers ---
    chat_input.submit(
        unified_chat,
        [chat_input, chatbot],
        [chat_input, chatbot]
    )

    clear_button.click(lambda: ("", []), None, [chat_input, chatbot])

    gr.Markdown(
        """
        <div style="text-align: center; margin-top: 20px; font-size: 0.9rem; color: #888;">
        Made with ❤️ using LangChain, WatsonX, and Gradio by NODEMONS
        </div>
        """
    )

demo.launch(share=True)




