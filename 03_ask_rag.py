# This script can run both locally (w/LM Studio) or with an OpenAI key.
from openai import OpenAI
import numpy as np
import json
from config import *

embeddings_json= "knowledge_pool/brutalism_wikipedia.json"

# Choose between "local" or "openai" mode
mode = "local" # or "local"
client, completion_model = api_mode(mode)

# question = "What is the program for the building?"
# question = "What is the place like?"
# question = "Is there any mention of the construction materials that should be used?"
question = "What are the names of the most famous brutalist buildings?"

num_results = 1 #how many vectors to retrieve


def get_embedding(text, model=embedding_model):
    text = text.replace("\n", " ")
    response = local_client.embeddings.create(input = [text], model=model)
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

def rag_answer(question, prompt, model=completion_model[0]["model"]):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", 
             "content": prompt
            },
            {"role": "user", 
             "content": question
            }
        ],
        temperature=0.1,
    )
    return completion.choices[0].message.content

# def rag_answer(question, prompt, model=completion_model[0]["model"]):
#     print("got in")
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo", # model = "deployment_name".
#         messages=[
#             {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
#             {"role": "user", "content": "Who were the founders of Microsoft?"}
#         ]
#     )
#     return response.choices[0].message.content

print("Waiting for an answer...")
# Embed our question
question_vector = get_embedding(question)

# Load the knowledge embeddings
index_lib = load_embeddings(embeddings_json)

# Retrieve the best vectors
scored_vectors = get_vectors(question_vector,index_lib)
scored_contents = [vector['content'] for vector in scored_vectors]
rag_result = "\n".join(scored_contents)

# Get answer from rag informed agent
prompt = f"""Answer the question based on the provided information. 
            You are given the extracted parts of a long document and a question. Provide a direct answer.
            If you don't know the answer, just say "I do not know." Don't make up an answer.
            PROVIDED INFORMATION: """ + rag_result

print(prompt)
answer = rag_answer(question, prompt)
print("ANSWER:")
print(answer)
