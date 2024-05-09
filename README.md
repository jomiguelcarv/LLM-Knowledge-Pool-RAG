# LLM-Knowledge-Pool-RAG

The repository contains **Part 1** of an LLM Pipeline for Design Exploration.

This project covers parsing raw data, creating an embedding database, and doing knowledge retrieval with a RAG system.

## Setup

-- Start by creating a virtual environment:

  

```bash
git clone https://github.com/jomi13/LLM-Knowledge-Pool-RAG
cd <your local repo directory>
python3.10 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

-- Create a `keys.py` file inside the directory, containing any necessary keys you may need, like so:

```python

LLAMAPARSE_API_KEY = "<your key>"
OPENAI_API_KEY = "<your key>"
REPLICATE_API_TOKEN = "<your key>"
....

```
> **Note:** For Part 1, you only need a key from [Llama-index](https://cloud.llamaindex.ai).

-- Install [LM Studio](https://lmstudio.ai) and download:

- An LLM of your preference **in GGUF format**, such as "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF"

- An embedding model, such as: "nomic-ai/nomic-embed-text-v1.5-GGUF"


-- In `config.py`, setup the configuration for the model you just downloaded, like so:

```python
llama3 = [
{
"model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
'api_key': 'any string here is fine',
'api_type': 'openai',
'base_url': "http://localhost:1234/v1",
"cache_seed": random.randint(0, 100000),
}]

```


## Running

--In LM Studio:
- Go to **Local Server** and load both models
- Click **Start Server**

-- Run the python scripts in order:
- `01_parse_pdf.py` will take any pdfs inside the knowledge_pool folder and turn them into structured .txt files
- `02_create_vector_db.py` will create an embeddings database as a json
- `03_ask_rag.py`will let you ask questions about your corpus of text with a RAG system.

> **Note:** To run the RAG with your **own corpus of text**, place any pdf files inside the folder `knowledge_pool`.
