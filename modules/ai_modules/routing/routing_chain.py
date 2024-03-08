from langchain.utils.math import cosine_similarity
from langchain_community.embeddings import OpenAIEmbeddings
import os
from config import params
from enum import Enum
from modules.ai_modules.features import DeFiFeature
import json

# Import key
os.environ["OPENAI_API_KEY"] = params.openai_key
# Define embedding
embeddings = OpenAIEmbeddings()
defiFeature = DeFiFeature()

class TaskName(Enum):
    GET_BALANCE = 0
    SWAP = 1
    OTHER = 2

def embed_prompt(input_question,path="data/prompts.json"):
    # Check file exist
    if not os.path.exists(path):
        raise Exception("File prompt not found!")
    # Open file
    with open(path,'r') as f:
        prompt_data = json.load(f)
        # Get description prompt
        description_prompts = [base_prompt['description'] for base_prompt in dict(prompt_data).values()]
        content_prompts = [base_prompt['text'] for base_prompt in dict(prompt_data).values()]

        # Get embedding from prompt
        prompt_embeddings = embeddings.embed_documents(description_prompts)

        # Get embedding of query sentence
        query_embedding = embeddings.embed_query(input_question)
        return query_embedding,prompt_embeddings,description_prompts,content_prompts


def prompt_router(input_question):
    # Get the embedding of prompt and incoming query
    query_embedding,prompt_embeddings,description_prompts,content_prompts = embed_prompt(input_question=input_question)

    # Calculate similarity
    similarity = cosine_similarity([query_embedding], prompt_embeddings)[0]

    # Get most similar template
    prompt_index = similarity.argmax()
    prompt_content = content_prompts[prompt_index]

    # Add information about prompt
    print(f"Branch: {description_prompts[prompt_index]}")
    return prompt_index,prompt_content

def assign_task(task_index,question,instruction,session_id):
    answer = ""
    # Get balance case
    if task_index == TaskName.GET_BALANCE.value:
        answer = defiFeature.answer_balance(question=question,instruction=instruction)
    # Swap case
    elif task_index == TaskName.SWAP.value:
        answer = defiFeature.answer_swapping(question=question,instruction=instruction,session_id=session_id)
    # Other case
    elif task_index == TaskName.OTHER.value:
        answer = defiFeature.answer_normal_question(question=question,instruction=instruction,session_id=session_id)
    return answer

def get_answer_on_pipeline(input_question,session_id):
    # Define prompt and index corresponding
    prompt_index,prompt_content = prompt_router(input_question)

    # Get the answer
    answer = assign_task(task_index=prompt_index,question=input_question,instruction=prompt_content,session_id=session_id)
    return answer