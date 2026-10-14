# RETRIEVAL AUGMENTED GENERATION (RAG)


This code explores stages and implementation of RAG. 

LLM Agent: Ollama Gemma 3:4b

## 1. Setting Up

### RAG_Practice.py
This file contains the main learning segment of RAG pracctices. As the learning progresses, the commits are added to see the changes made to the file.

Created the virtual environment and installing dependencies
Local Model Inference: Ollama gemma3:4b

`def_query_model`: We send the query to the locl model for processing and returning back the data in JSON format. This is used at the final output after pulling the message and content of the returned value.


## 2. Database And An Amateur Solution
Here, we provided a user database with three prominent figures (celebrities) with descriptions that do not match their real-world description. 
Example: In the real world, Dhoni is an Indian cricket player.
         In our database, Dhoni is a TV show host in the kids entertainment industry.
By making a description, we see how the model is directed to the database and provide the response from our database rather than pulling out real world data for context.

We then search through the query for a word that matches with the key in the database, when found, we add it to context

` context= "" ` : Whatever data is being retrieved from the database (eg. Dhoni is a tv actor) is pushed into context. This will be passed to Ollama with the query so that Ollama now has information of who is being talked about here.

`Isuse:` This can only take in exact matches. If the searched item is misspelt, then the retrieval will end with an error, since the error made in the query cannot be identified.

If we replace the context sent with the user_data, we may be able to get the answer as expected, i.e,

prompt = f"Based on the following context about our users, answer the user queries. \nContext:`{user_data}`. \nQuery: {misspelt_query}"
print("PROMPT:\n" + prompt)

But in reality, databases are huge, this solution is not practical in the real-world scenario.
This requires some semantic level retrieval.


## 3. Retrieval Using FAISS and Sentence Transformers

Required Installs:
!pip install PyPDF2 -q
!pip install faiss-cpu -q
!pip install sentence-transformers -q


`FAISS (Faccebook AI Similarity Search):` It`s an open-source library created by Meta for efficient similarity search and clustering of dense vectors. In one lookup, it can quickly access all the vectors in a parallelized manner.
    `IndexFlatL2:` Consists of all the embeddings in a 1-D format. It comes in single-level or multi-level tables.

`PyPdf:` To read files

`Sentence Transformer:` an encoder model for math tasks (NOT a language model).
    `tensor:` allows the embedding to be a tensor, performing faster calculation on a TPU(Tensor Processing Unit)
  

### Steps for FAISS retrieval:

Vectorize our database. 
1. Chunk the data in the database
2. Create embeddings for each chunks.
3. Build an index to perform the search when a user query arrives.

Once query arrives:
1. Embed the query
2. Finding vectors closest to that query(top_k) in the database
3. Finding the text associated to the embeddings to those closest vectors
4. Return that text

`retrieve_text`: This function will create query embeddings and perform the search for best and closest match to return the result i.e. the answer to the query.
