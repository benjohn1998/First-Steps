"""RAG- Setup and and explore"""
import requests

#---------------------------------------------------------------------------------------------------
#           DATABASE SETUP
#---------------------------------------------------------------------------------------------------
user_data= {
    "Dhoni": "Dhoni is a well-known TV show host, known for his many appearances in kids entertainment industry",
    "Bheem": "Bheem is a famous politician hailing from the state of Bihar, known for his policies and action against corruption.",
    "Rajnikanth": "Rajnikanth is a professional cricketer, best known for his performance in 2023 World Cup",
}

#---------------------------------------------------------------------------------------------------

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "gemma3:4b"

context= ""

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

#---------------------------------------------------------------------------------------------------
#          Amatuer Solution
#---------------------------------------------------------------------------------------------------
for word in query.split():
    if word in user_data:
        context+=user_data[word]

prompt = f"Based on the provided internal data, answer the query.\nQuery: {query}\n\nInternal User Data: {context}"
print(f"\n\nPROMPT: {prompt}")
response= query_local_model(prompt)
reply= response["message"]["content"]


print(f"\n\n\nModel Reply: {reply}")

#---------------------------------------------------------------------------------------------------