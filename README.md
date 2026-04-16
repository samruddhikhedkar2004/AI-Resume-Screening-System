# 🤖 AI Resume Screening System with Tracing

An AI-powered Resume Screening System built using **LangChain** and **Groq LLM**, designed to evaluate candidates based on job descriptions.  
The system performs **skill extraction, matching, scoring, and explanation generation**, along with **LangSmith tracing for monitoring and debugging**.

---

## 🚀 Features

- 📄 Resume Skill Extraction  
- 🔍 Candidate vs Job Matching  
- 🎯 Automated Scoring (0–100)  
- 💬 Explainable AI Feedback  
- 🔗 Modular LangChain Pipeline  
- 📊 LangSmith Tracing & Monitoring  
- ⚡ Fast LLM inference using Groq  

---

## 🧠 System Architecture
```
Resume → Skill Extraction → Matching → Scoring → Explanation
```

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Groq (LLM - LLaMA 3)**
- **LangSmith (Tracing & Debugging)**
- **VS Code**

---

## 📂 Project Structure

```
resume_screening/
├── prompts/
│   └── prompt_templates.py      # All LangChain PromptTemplates
|
├── chains/
│   └── screening_chain.py       # LCEL pipeline using Groq LLM
|
├── data/
│   └── resumes.py               # 3 sample resumes + job description
|
├── screenshots/                 # LangSmith tracing screenshots
├── main.py                      # Entry point — runs all 3 candidates
├── .env                         
├── requirements.txt
└── README.md
```

---

## 📊 Sample Output

**Skills:** Python, SQL, Pandas
**Tools:** NumPy, Matplotlib
**Experience:** 1 year

Matched: Python, Pandas
Missing: Deep Learning

Score: 65

Explanation: Candidate has strong fundamentals but lacks advanced ML experience.

---

## 🔍 LangSmith Tracing

- Tracks each step of the pipeline
- Helps debug LLM outputs
- Visualizes workflow execution

## 📸 Screenshots

- Terminal Output
- Groq Logs & Metrics
- LangSmith Pipeline Traces
- LLM Call Details

## ⭐ Conclusion

This project gave me hands-on experience building a modular AI pipeline using LangChain covering skill extraction, matching, scoring, and explanation in structured steps. LangSmith tracing helped monitor and debug each stage.
Overall, it was a practical introduction to how real-world GenAI systems are designed and monitored.

## 👩‍💻 Author

Samruddhi Khedkar

Final Year B.Tech — Electronics & Telecommunication Engineering

Agentic AI Intern — Innomatics Research Labs
