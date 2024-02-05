from langchain.utils.math import cosine_similarity
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_community.llms import OpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from config import params
model_name = "gpt-3.5-turbo-instruct"
os.environ["OPENAI_API_KEY"] = params.openai_key
output_parser = StrOutputParser()

# Define model
chat_model = OpenAI(model_name=model_name)


# Define chain

def get_answer(question,instruction):
    # Define prompt
    prompt = ChatPromptTemplate.from_template(instruction + "Question:\n {question}" +"Answer:\n")
    chain = prompt | chat_model
    output = chain.invoke({"question":question})
    return output
