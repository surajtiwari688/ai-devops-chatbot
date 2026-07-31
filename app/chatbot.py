from ollama import Client

client = Client(host="http://host.minikube.internal:11434")

def ask_ai(message: str):
    response = client.chat(
        model="llama3.2", 
        messages=[
            {
                "role": "system", 
                "content": (
                    "You are a helpful DevOps assistant." 
                    "Answer the user's questions to the best of your ability."
                )
            },
            {
                "role": "user", 
                "content": message,
            }
        ]
    )
    return response["message"]["content"]