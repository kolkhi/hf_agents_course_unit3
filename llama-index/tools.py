from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from llama_index.core.tools import FunctionTool
from huggingface_hub import list_models
import random


def get_search_tool(query: str) -> str:
    """Searches information int the Internet"""
    tool_spec = DuckDuckGoSearchToolSpec()

    search_tool = FunctionTool.from_defaults(tool_spec.duckduckgo_full_search)

    response = search_tool(query)

    return response.raw_input[-1]['body']

def get_weather_info(location: str) -> str:
    """Fetches dummy weather information for given location"""

    weather_conditions = [
        {"condition": "Rainy", "temp_c": 15},
        {"condition": "Clear", "temp_c": 20},
        {"condition": "Windy", "temp_c": 25}
    ]

    data = random.choice(weather_conditions)

    return f"Weather in {location} is: {data['condition']}, {data['temp_c']}°C"

def get_hub_stats_tool(author: str)->str:
    """Fetches the most downloaded model from a specific author on the Hugging Face Hub."""
    try:
        models = list(list_models(author=author, sort="downloads", direction=-1, limit=1))

        if models:
            model = models[0]
            return f"The most downloaded model by author {author} is {model.id} with {model.downloads:,} downloads"
        else:
            return f"No models found for author {author}"
    except Exception as e:
        return f"Error fetching model for author {author}: {str(e)}"

weather_info_tool = FunctionTool.from_defaults(get_weather_info)
hub_stats_tool = FunctionTool.from_defaults(get_hub_stats_tool)
search_tool = FunctionTool.from_defaults(get_search_tool)