# AI-Security-Lab
AI Security Lab

Project Overview

AI Security Lab is a local Streamlit-based educational project for demonstrating AI application security concepts and basic agent tool authorization.

Features

- Local demo chatbot
- Mock AI agent tools
- Security risk catalogue
- Local security checks
- Test results dashboard
- CSV results export
- Agent Tool Authorization mitigation

Technologies

- Python
- Streamlit
- Pandas

Run Locally

Install dependencies:

pip install -r requirements.txt

Start the application:

python -m streamlit run app.py

Open "http://localhost:8501" in your browser.

Mitigation Evidence

Five local mock authorization checks passed:

- Approved file access: PASS
- Restricted file access: PASS
- Email without approval: PASS
- HTTP without approval: PASS
- Approved mock email: PASS

Limitations

This is a local educational prototype. It does not claim production-grade security validation or real Claude/Gemini model testing. Mock email and HTTP actions do not perform real external actions.
