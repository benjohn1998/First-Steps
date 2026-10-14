"""RAG- Setup and and explore"""
import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "gemma3:4b"

def query_local_model(query):
    """Query the local model using the OLLAMA API."""
    response = requests.post(
        OLLAMA_URL,
        json = {
            "model": MODEL_NAME,
            "messages": [{
                "role": "user",
                "content": query
            }],
        "stream":False,
        "options": {
            "temperature": 0.2,    #lower creativity
            },
        },
    )
    data = response.json()
    return data

query = "Tell me about Dhoni"


print("Query: ", query)
json_response = query_local_model(query)
print("\nResponse: ", json_response)
reply = json_response["message"]["content"]
print("\n\n\nReply:", reply)

