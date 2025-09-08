 🚀 RAG Chatbot with End-to-End CI/CD Deployment

An end-to-end **Retrieval-Augmented Generation (RAG) chatbot** project, fully containerized with **Docker**, automated via **Jenkins CI/CD pipeline**, scanned for vulnerabilities with **Trivy**, and deployed on **AWS App Runner** using **ECR**.

---

## 📌 Features
- 🧠 **RAG Pipeline** – Ingests domain-specific documents, chunks text, and retrieves context for LLM-powered answers.  
- 🐳 **Containerization** – Built Docker images for reproducible environments.  
- ⚡ **CI/CD Pipeline** – Automated with Jenkins:
  - Code checkout from GitHub  
  - Docker build & Trivy security scan  
  - Push to AWS Elastic Container Registry (ECR)  
  - Deploy to AWS App Runner  
- 🔐 **Security** – Integrated Trivy for container vulnerability scanning.  
- ☁️ **Cloud Deployment** – Scalable chatbot hosted on AWS App Runner.  

---

## 🏗️ Tech Stack
- **Backend**: Python, FastAPI/Flask (depending on your code)  
- **LLM**: HuggingFace Transformers / SentenceTransformers  
- **CI/CD**: Jenkins (Docker-in-Docker setup)  
- **Security**: Trivy  
- **Cloud**: AWS ECR + App Runner  
- **Containerization**: Docker  

---

## 🔑 Environment Variables

This project requires the **OpenAI API key** for LLM access.

1. Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AbdullahHasan0/RAG-MEDICAL-CHATBOT
```

## 2️⃣ Create Virtual Environment (Local Development)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -e .
```

## 3️⃣ Run Locally
```bash
python .\app\application.py
```

Visit: ```http://localhost:8000```
