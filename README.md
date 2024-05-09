# LLM-Knowledge-Pool-RAG

A repository for the first part of an LLM Pipeline for design exploration.

- Create a `keys.py` file in your local machine, containing any necessary keys, like so:
    ```python
    LLAMAPARSE_API_KEY = <your key>
    OPENAI_API_KEY = <your key>
    REPLICATE_API_TOKEN = <your key>
    ```

To setup the project:
```bash
source myenv/bin/activate
python3.10 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
