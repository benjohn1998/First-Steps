"""RAG- Setup and and explore"""
import requests
from sentence_transformers import SentenceTransformer
import faiss


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
print(f"Query: {query}")

#---------------------------------------------------------------------------------------------------
#          FAISS RETRIEVAL Solution
#---------------------------------------------------------------------------------------------------
# 1. Chunk the data

all_chunks= list(user_data.values())
print(f"All Chunks: {all_chunks}")

#2. Create embeddings for the chunks
embedder= SentenceTransformer("all-MiniLm-L6-V2")
embeddings= embedder.encode(all_chunks, convert_to_tensor= True)
print(len(embeddings), len(embeddings[0]))
print(f"Embeddings: {embeddings[0]}")

#3. Create a FAISS index and add the embeddings
dim= embeddings[0].shape[0]
index= faiss.IndexFlatL2(dim)
index.add(embeddings)

print(f"Indexed: {len(all_chunks)} chunks")

#4. Create an embedding for the query

def retrieve_text(query, top_k=3):
    query_emb= embedder.encode([query])
    distances, indices = index.search(query_emb, top_k)     # Finding vectors closest to the query
    results = []
    for i, dist in zip(indices[0], distances[0]):           # Finding text associated with that closest vector
        results.append({"text": all_chunks[i], "distance": dist})
    return results

query = "Who is a sportsman?"
results = retrieve_text(query)

for result in results:
    print(f"Distance:{result['distance']:.4f}") 
    print(f"Text: {result['text']}")
    print("----------")
#---------------------------------------------------------------------------------------------------
