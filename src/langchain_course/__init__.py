from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

import os
load_dotenv()

tavily=TavilyClient()
@tool
def search(query:str)->str:
    """
    This tools searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"searching for {query}")
    return tavily.search(query=query)


llm= ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
tools = [search]
agent=create_agent(model=llm,tools=tools)

def main():
    print("Hello from langchain-course!")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    result=agent.invoke({"messages":HumanMessage(content="search for 3 job posting for an ai engineer using lanchain in bay area on linkedin   and list their details")})
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()
