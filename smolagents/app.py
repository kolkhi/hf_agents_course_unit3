from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool
from tools import WeatherInfoTool, HubStatsInfo
from retriever import load_guest_dataset

model = HfApiModel()

search_tool = DuckDuckGoSearchTool()
weather_info_tool = WeatherInfoTool()
hub_stats_tool = HubStatsInfo()

guest_tools = load_guest_dataset()

tools = [search_tool, weather_info_tool, hub_stats_tool] + guest_tools

def main(): 
    
    alfred = CodeAgent(
        tools=tools, 
        model=model, 
        add_base_tools=True, 
        planning_interval=3)

    print("Enter a question or 'quit' to exit:")
    query = input()
    while query != 'quit':
        response = alfred.run(query)
        print("Alfred's response:")
        print(response)
        print("Next question or enter 'quit' to exit:")
        query = input()

main()