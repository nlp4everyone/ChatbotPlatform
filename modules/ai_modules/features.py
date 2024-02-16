from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from operator import itemgetter
from langchain_core.runnables.history import RunnableWithMessageHistory
import os
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.chat_message_histories import Neo4jChatMessageHistory
from langchain.memory import MotorheadMemory

from config import params
from langchain.memory import AstraDBChatMessageHistory
from modules.ai_modules.custom_tool import BalanceTool
# Import key
os.environ["OPENAI_API_KEY"] = params.openai_key
# model_name = "gpt-3.5-turbo-1106"
# chat_model = ChatOpenAI(model_name=model_name)
# Define memory
memory = ConversationBufferMemory(return_messages=True)

class DeFiFeature():
    def __init__(self,model_name = "gpt-3.5-turbo-1106"):
        # Define chat model
        self.chat_model = ChatOpenAI(model_name=model_name)
        # Define memory
        self.memory = memory


    def history_chain(self,instruction,session_id):
        # Define prompt
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", instruction),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
            ]
        )

        # Define chain
        # chain = (
        #         RunnablePassthrough.assign(
        #             history=RunnableLambda(self.memory.load_memory_variables) | itemgetter("history")
        #         )
        #         | prompt
        #         | self.chat_model
        # )
        chain = prompt | self.chat_model
        # chain_with_history = RunnableWithMessageHistory(
        #     chain,
        #     lambda session_id: RedisChatMessageHistory(
        #         session_id,url="redis://127.0.0.1:6379"
        #     ),
        #     input_messages_key="question",
        #     history_messages_key="history",
        # )

        # self.msgs = StreamlitChatMessageHistory(key=session_id)
        self.msgs = Neo4jChatMessageHistory(
            url="neo4j+s://3ccedd0c.databases.neo4j.io",
            username="neo4j",
            password="jYCaJAAuUBCMI0JeTNoziEHO838geclJPHhGkHLuJbY",
            session_id=session_id,
        )
        # self.msgs = MotorheadMemory(
        #     session_id=session_id, url="http://localhost:8080", memory_key="history"
        # )

        chain_with_history = RunnableWithMessageHistory(
            chain,
            lambda session_id: self.msgs,
            input_messages_key="question",
            history_messages_key="history",
        )

        return chain_with_history

    def tool_chain(self,instruction):
        # Define prompt
        prompt = ChatPromptTemplate.from_template(f"Instruction:{instruction}")
        # Define chain
        chain = prompt | self.chat_model | StrOutputParser() | BalanceTool()
        return chain

    def get_memory(self):
        # Return memory
        return self.memory.load_memory_variables({})

    def update_memory(self,user_input,bot_answer):
        # Add answer to history
        self.memory.save_context(user_input, {"output": bot_answer})

    def answer_normal_question(self,question, instruction,session_id):
        # Init chain
        chain = self.history_chain(instruction=instruction,session_id=session_id)

        # # Define input
        # user_input = {"input": question}
        # # Answer
        # bot_answer = chain.invoke(user_input)
        # bot_answer = bot_answer.content
        config = {"configurable": {"session_id": session_id}}
        bot_answer = chain.invoke({"input": question}, config=config)
        bot_answer = bot_answer.content

        self.msgs.add_ai_message(bot_answer)
        self.msgs.add_user_message(question)
        print(self.msgs.messages)

        # Update to context
        # self.update_memory(user_input=user_input,bot_answer=bot_answer)
        return bot_answer

    def answer_swapping(self,question, instruction):
        # Answer
        answer = self.answer_normal_question(question=question,instruction=instruction)
        return answer

    def answer_balance(self,question,instruction):
        # Init chain
        chain = self.tool_chain(instruction=instruction)

        # Define input
        user_input = {"input": question}
        # Answer
        bot_answer = chain.invoke(user_input)

        # Update memory
        # self.memory.save_context(user_input, {"output": str(bot_answer)})
        return bot_answer

# class OldDeFiFeature():
#     @staticmethod
#     def answer_normal_question(question, instruction):
#         # Define prompt
#         prompt = ChatPromptTemplate.from_messages(
#             [
#                 ("system", instruction),
#                 MessagesPlaceholder(variable_name="history"),
#                 ("human", "{input}"),
#             ]
#         )
#
#         # Define chain
#         chain = (
#                 RunnablePassthrough.assign(
#                     history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
#                 )
#                 | prompt
#                 | chat_model
#         )
#         # Define input
#         inputs = {"input": question}
#         # Answer
#         answer = chain.invoke(inputs)
#         # Add answer to history
#         memory.save_context(inputs, {"output": answer.content})
#         # print("History:")
#         # Get history
#         # history = memory.load_memory_variables({})
#         # print(history)
#         return answer.content
#
#     @staticmethod
#     def answer_swapping(question, instruction):
#         # Answer
#         answer = DeFiFeature.answer_normal_question(question,instruction)
#         return answer
#
#     @staticmethod
#     def answer_balance(question,instruction):
#         # Define prompt
#         prompt = ChatPromptTemplate.from_template(f"Instruction:{instruction}")
#
#         # Define chain
#         # Define input
#         inputs = {"input": question}
#         chain = prompt | chat_model | StrOutputParser() | BalanceTool()
#         # Answer
#         answer = chain.invoke(inputs)
#         # Add answer to history
#         # memory.save_context(inputs, {"output": answer.content})
#         # print("History:")
#         # Get history
#         # history = memory.load_memory_variables({})
#         # print(history)
#         return answer
