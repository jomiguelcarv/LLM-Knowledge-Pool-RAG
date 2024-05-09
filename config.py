import random
from openai import OpenAI
from keys import *


# API
local_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Models
embedding_model = "nomic-ai/nomic-embed-text-v1.5-GGUF"

mistral_8x7b = [
        {
            "model": "cjpais/llava-1.6-mistral-7b-gguf/llava-1.6-mistral-7b.Q6_K.gguf",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
        }
]

mistral_7b = [
        {
            "model": "TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
        }
]

nous_capybara_3b = [
        {
            "model": "RichardErkhov/NousResearch_-_Nous-Capybara-3B-V1.9-gguf",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
        }
]

westlake = [
        {
            "model": "TheBloke/WestLake-7B-v2-GGUF",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
            "cache_seed": random.randint(0, 100000),
        }
]

# Notice how this model is not running locally. It uses an OpenAI key.
gpt4_turbo = [
        {
            "model": "gpt-4-turbo-preview",
            "api_key": OPENAI_API_KEY,
            "cache_seed": random.randint(0, 100000),
        }
]

command_r = [
        {
            "model": "andrewcanis/c4ai-command-r-v01-GGUF",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
            "cache_seed": random.randint(0, 100000),
        }
]

llama3 = [
        {
            "model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
            "cache_seed": random.randint(0, 100000),
        }
]

# If you download any new models, make sure to add its configuration here. Simply change the "model" name to the correct one.
# myNewModel = [
#         {
#             "model": <the model name that you can find in LM Studio>,
#             'api_key': 'any string here is fine',
#             'api_type': 'openai',
#             'base_url': "http://localhost:1234/v1",
#             "cache_seed": random.randint(0, 100000),
#         }
# ]

# Helping functions
def api_mode (mode):
    if mode == "local":
        client = local_client
        completion_model = mistral_7b #whatever model you want to use
        return client, completion_model
    elif mode == "openai":
        client = openai_client
        completion_model = gpt4_turbo
        return client, completion_model
    else:
        raise ValueError("Please specify if you want to run local or openai models")