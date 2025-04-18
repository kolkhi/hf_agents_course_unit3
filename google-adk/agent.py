from google.adk import Agent, Runner
from google.adk.sessions import InMemorySessionService
from google.adk.models.lite_llm import LiteLlm
from dotenv.main import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from google.adk.tools.langchain_tool import LangchainTool
from google.genai import types
from .tools import get_hub_stats_tool, get_weather_info
from .retriever import extract_text
import os

load_dotenv()

web_search = DuckDuckGoSearchRun()
adk_dds_tool = LangchainTool(tool=web_search)

root_agent = Agent(
    name = "Alfred",
    tools=[get_weather_info, get_hub_stats_tool, extract_text, adk_dds_tool],
    #model=LiteLlm(model="huggingface/Qwen/Qwen2.5-Coder-32B-Instruct"), # Uncomment this line to use the Hugging Face model via LiteLlm
    model = "gemini-2.0-flash",
    description=(
        "An agent that can answer questions, provide weather information, and fetch the most downloaded model from a specific author on the Hugging Face Hub."
        " It can also provide detailed information about gala guests based on theri name or relation."
        " It can also search the web for information."
    ),
    instruction=(
        "You are a helpful agent. Your name is Alfred."
        "You can answer questions, provide weather information, and fetch the most downloaded model from a specific author on the Hugging Face Hub."
        "You can also search the web for information using DuckDuckGo Search."
        "You can also provide detailed information about gala guests based on theri name or relation."
    )
)   

USER_ID = "user-1"
SESSION_ID = "gala-assistant"
APP_NAME = "Gala Assistant"

session_service = InMemorySessionService()
session = session_service.create_session(
    session_id=SESSION_ID,
    user_id=USER_ID,
    app_name=APP_NAME,
 )

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)

def call_agent(query: str):
    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(
        user_id = USER_ID,
        session_id = SESSION_ID,
        new_message=content
    )

    for event in events:
        if event.is_final_response():
            final_resposne = event.content.parts[0].text
            print(F"Alfred's response: {final_resposne}")

call_agent("Hello Alfred!")