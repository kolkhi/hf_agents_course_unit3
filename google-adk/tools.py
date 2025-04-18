import random
from huggingface_hub import list_models

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

def get_hub_stats_tool(author: str)->str:
    """Fetches the most downloaded model from a specific author on the Hugging Face Hub.
    
    Args:
        author (str): The author of the model on the Hugging Face Hub.

    Returns:
        str: A string describing the most downloaded model by the specified author.
    """

    try:
        models = list(list_models(author=author, sort="downloads", direction=-1, limit=1))

        if models:
            model = models[0]
            return f"The most downloaded model by author {author} is {model.id} with {model.downloads:,} downloads"
        else:
            return f"No models found for author {author}"
    except Exception as e:
        return f"Error fetching model for author {author}: {str(e)}"

