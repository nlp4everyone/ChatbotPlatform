from langchain.tools import BaseTool, StructuredTool, tool
from data import all_data
class BalanceTool(BaseTool):
    name = "get_data"
    description = "useful for when you need to access to balance or wallet of user"
    def _run(self,query:str):
        """Use the tool."""
        return all_data.balance_data

    async def _arun(self) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")