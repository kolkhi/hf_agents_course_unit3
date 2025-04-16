import random

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
