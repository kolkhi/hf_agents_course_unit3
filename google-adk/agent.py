from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import random
from dotenv.main import load_dotenv
import os
import asyncio

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

hugging_face_llm = LiteLlm(model="huggingface/Qwen/Qwen2.5-Coder-32B-Instruct")

def get_weather_info(location: str) -> str:
    """Fetches dummy weather information for given location.
    
    Args:
        location (str): The location to get weather information for.

    Returns:
        str: A string describing the weather in the specified location.    
    """

    weather_conditions = [
        {"condition": "Rainy", "temp_c": 15},
        {"condition": "Clear", "temp_c": 20},
        {"condition": "Windy", "temp_c": 25}
    ]

    data = random.choice(weather_conditions)

    return f"Weather in {location} is: {data['condition']}, {data['temp_c']}°C"


root_agent = Agent(
    name = "weather_agent",
    tools=[get_weather_info],
    model=hugging_face_llm,
    description=(
        "A weather agent that provides weather information for a given location."
    ),
    instruction=(
        "You are a helpful weather agent. You provide weather information for a given location."
    )
)   