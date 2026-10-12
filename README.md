<<<<<<< HEAD
# First-Steps
This repository contains different learning materials in different packages.
=======
# Create Simple Chatbots



## Setup


### Creatae a virtual environment:


``Powershell
python -m venv .venv 

### Activate it:
.venv\Scripts\Activate.ps1

If powershell blocks the activtaion, tun this code once, and try agin:
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

### Install python dependencies:
python -m pip install -r requirements.txt


## Run the Gemini Chatbot


Create a key in [Google AI Studio](https://aistudio.google.com/apikey).
Create a local .env file in this folder (**Do not share or commit it) with:
```Powershell
$env: "Insert_Key_Name" = "paste_your_key_here"
python gemini_chatbot.py
```

## Run the Ollama Chatbot


Install and open [Ollama](https://ollama.com/download).

`python ollama_chatbot.py` does **not** start Ollama by itself. It needs the local service on port `11434` already running.

Use **one** of these:
- Open the **Ollama app** and leave it running, **or**
- Run `ollama serve` in a separate terminal

Then check the service and download the demonstration model once:

```bash
ollama list
ollama pull gemma4:12b
python ollama_chatbot.py
```



In either chatbot, type `/exit` to stop. To test conversation memory, try:
```text
You: My name is John and I am learning about local models.
You: What is my name, and what am I learning?
```
>>>>>>> old-target/main
