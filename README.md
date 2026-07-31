# AI Chatbot on Kubernetes

## Technologies
- Python
- FastAPI
- Docker
- Kubernetes
- Minikube
- Ollama
- Llama 3.2

## Run

docker build -t ai-chatbot .

kubectl apply -f k8s/

minikube service ai-chatbot-service

# Architecture

User
   ↓
FastAPI
   ↓
Kubernetes (Minikube)
   ↓
Python Chatbot
   ↓
Ollama
   ↓
Llama 3.2
   ↓
AI Response
