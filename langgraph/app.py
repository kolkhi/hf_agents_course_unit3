from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import START, StateGraph
from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_community.tools import DuckDuckGoSearchRun
from retriever import guest_info_tool, guest_conversation_starter_tool
from tools import weather_info_tool, hub_stats_tool
from dotenv.main import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

seach_tool = DuckDuckGoSearchRun()

def main(): 
    hugging_face_llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-Coder-32B-Instruct", huggingfacehub_api_token=HF_TOKEN)

    chat = ChatHuggingFace(llm=hugging_face_llm, verbose=True)

    tools = [guest_info_tool, guest_conversation_starter_tool, seach_tool, weather_info_tool, hub_stats_tool]

    chat_with_tools = chat.bind_tools(tools)

    class AgentState(TypedDict):
        messages: Annotated[list[AnyMessage], add_messages]

    def assistant(state: AgentState):
        return {
            "message": [chat_with_tools.invoke(state["messages"])]
        }

    builder = StateGraph(AgentState)

    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant",
        tools_condition
    )

    builder.add_edge("tools","assistant")
    alfred = builder.compile()

    print("Enter a question or 'quit' to exit:")
    response = {"messages": []}
    query = input()
    while query != 'quit':
        messages = response["messages"] + [HumanMessage(content=query)]
        response = alfred.invoke({"messages": messages})
        print("Alfred's response:")
        print(response)
        print("Next question or enter 'quit' to exit:")
        query = input()

main()