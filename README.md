# LLM-Knowledge-Pool-RAG

The repository for the first part of an LLM Pipeline for design exploration. This project covers parsing raw data, creating an embedding database, and doing knowledge retrieval with a RAG system.

To set up the project on your local machine, start by creating a virtual environment:

```bash
git clone https://github.com/jomi13/LLM-Knowledge-Pool-RAG
cd <your local repo directory>
source myenv/bin/activate
python3.10 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

- Create a `keys.py` file in your local machine, containing any necessary keys, like so:
    ```python
    LLAMAPARSE_API_KEY = <your key>
    OPENAI_API_KEY = <your key>
    REPLICATE_API_TOKEN = <your key>
    ```