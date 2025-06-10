# 🚀 GUIDE: Growth-based Unified Intelligence Direction Engine

> **Team Name**: NODEMONS  
> **Problem Statement**: The objective is to develop an AI-driven career counseling system that provides personalized career recommendations to students by analyzing their skills, interests, and aptitudes. Many students, especially in underserved areas, struggle to make informed decisions about their future due to a lack of guidance and awareness of career opportunities. This AI-powered solution will bridge that gap by offering tailored career suggestions and actionable insights to help students align their strengths with suitable career paths.

A system that identifies potential career paths, suggests relevant skill-building courses, and provides information about future growth prospects in chosen fields.

---

## 🧠 Project Overview

**GUIDE** (Growth-based Unified Intelligence Direction Engine) is an AI-powered career counseling system built to empower students — especially those from underserved areas — with **personalized career recommendations**.

By analyzing resumes, skills, interests, and aptitudes using cutting-edge **AI and NLP**, GUIDE simulates the insight of a human counselor. It recommends suitable **career paths**, **skill development resources**, and predicts **future career growth**, all tailored to the student's background and goals.

Whether you're a student unsure of what comes next or an institution looking to guide learners at scale, **GUIDE** provides a smart, scalable, and human-like mentoring experience.

---

## 🛠️ Technologies Used

| Category                        | Tool / Technology             |
|--------------------------------|-------------------------------|
| **UI Framework**               | Gradio                        |
| **AI Backend**                 | LangChain                     |
| **Embedding API**              | IBM Watsonx.ai                |
| **Document Parsing**           | PyPDF2                        |
| **Language Model**             | IBM/granite-3-8b-instruct     |
| **RAG (Retriever Chain)**      | Custom LangChain Retriever    |
| **Language**                   | Python                        |
| **API Testing**                | IBM Watsonx.ai platform       |
| **Web search**                 | TavilyAPI                     |

---

## 🧑‍💻 Setup & Run Instructions

Follow these steps to run the project locally:

### 1. 🔁 Clone the Repository
```bash
git clone https://github.com/nodemones/GUIDE.git
cd GUIDE

# For Linux/macOS:
python -m venv venv
source venv/bin/activate

# For Windows:
python -m venv venv
venv\Scripts\activate
```
### 2.📦 Install Dependencies
```bash
pip install -r requirements.txt

Ensure your requirements.txt includes:
gradio, langchain, pypdf2, ibm-watsonx-ai, python-dotenv, etc.
```

### 3.  ▶️ Run the Application
```bash
Gradio ui.py
    or
python ui.py
```
### 4. 🔐 Configure Environment Variables
```bash
cerate a dot env file and ensure to put these credientials the same.

WATSONX_URL=_____________
API_KEY=_____________
PROJECT_ID=_____________
```

### 🎬 Demo Video


### 🌟 Key Highlights
```bash
a. Conversational LLM agents
b. Personalized Carrer Paths
c. Resume parsing
d. Real time Market insights
e. Up to date Recommendations
f. Future growth predictions
g. Empowers undeserved students
```

### Built with ❤️ by Team NODEMONS

