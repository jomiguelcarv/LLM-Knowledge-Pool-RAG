import json
import os
from config import *

### UPDATE ACCORDING TO YOUR SETUP ###
embedding_model = "nomic-ai/nomic-embed-text-v1.5-GGUF"
knowledge_pool = "C1_KnowledgePool_Rag/knowledge_pool"

def get_embedding(text, model=embedding_model):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

for document in os.listdir(knowledge_pool):
    if document.endswith(".txt"):
        filepath = os.path.join(knowledge_pool, document)
    
        # Read the text document
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
            text_file = infile.read()

        # Split the text into lines (each line = 1 vector)
        lines = text_file.split("\n")
                
        # Create the embeddings
        embeddings = []
        for i, line in enumerate(lines):
            print(f'{i} / {len(lines)}')
            vector = get_embedding(line.encode(encoding='utf-8').decode())
            database = {'content': line, 'vector': vector}
            embeddings.append(database)

        # Save the embeddings to a json file
        output_filename = os.path.splitext(document)[0]
        output_path = os.path.join(knowledge_pool, f"{output_filename}.json")
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(embeddings, outfile, indent=2, ensure_ascii=False)

        print(f"Finished vectorizing {document}")

print("Finished vectorizing all documents")