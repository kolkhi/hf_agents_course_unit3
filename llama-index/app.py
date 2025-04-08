from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.core.workflow import Context
from retriever import guest_info_tool, guest_conversation_starter_tool
from tools import search_tool, weather_info_tool, hub_stats_tool
from dotenv.main import load_dotenv
import os
import asyncio

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

async def main(): 
    hugging_face_llm = HuggingFaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct", token=HF_TOKEN)

    alfred = AgentWorkflow.from_tools_or_functions(
        [guest_info_tool, guest_conversation_starter_tool, search_tool, weather_info_tool, hub_stats_tool],
        llm=hugging_face_llm
    )

    ctx = Context(alfred)

    print("Enter a question or 'quit' to exit:")
    query = input()
    while query != 'quit':
        response = await alfred.run(query, ctx=ctx)
        print("Alfred's response:")
        print(response)
        print("Next question or enter 'quit' to exit:")
        query = input()

asyncio.run(main())