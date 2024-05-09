from openai import OpenAI
import numpy as np
import json
from config import *

### UPDATE ACCORDING TO YOUR SETUP ###
# question = "What is the program for the building?"
# question = "What is the place like?"
question = "Is there any mention of the construction materials that should be used?"
num_results = 100 #how many vectors to retrieve
embeddings_json= "C1_KnowledgePool_Rag/knowledge_pool/Competition_brief.json"
embedding_model = "nomic-ai/nomic-embed-text-v1.5-GGUF"
rag_model = "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF"

def get_embedding(text, model=embedding_model):
    text = text.replace("\n", " ")
    response = client.embeddings.create(input = [text], model=model)
    vector = response.data[0].embedding
    return vector

def similarity(v1, v2):
    return np.dot(v1, v2)

def load_embeddings(embeddings_json):
    with open(embeddings_json, 'r', encoding='utf8') as infile:
        return json.load(infile)
    
def get_vectors(question_vector, index_lib):
    scores = []
    for vector in index_lib:
        score = similarity(question_vector, vector['vector'])
        scores.append({'content': vector['content'], 'score': score})

    scores.sort(key=lambda x: x['score'], reverse=True)
    best_vectors = scores[0:num_results]
    return best_vectors

def rag_answer(question, rag_result, model=rag_model):
    completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", 
            "content": f"""Answer the user question based on the provided information. 
                        If the provided information does not answer the question, 
                        simply reply "There is no information available to answer the question"
                        and nothing else.
                        PROVIDED INFORMATION: """ + rag_result},
        {"role": "user", 
            "content": question}
    ],
    temperature=0.6,
    )
    return completion.choices[0].message.content

# Embed our question
question_vector = get_embedding(question)

# Load the knowledge embeddings
index_lib = load_embeddings(embeddings_json)

# Retrieve the best vectors
scored_vectors = get_vectors(question_vector,index_lib)
scored_contents = [vector['content'] for vector in scored_vectors]
rag_result = "\n".join(scored_contents)

# Get answer from rag informed agent
answer = rag_answer(question, rag_result)
print(answer)
