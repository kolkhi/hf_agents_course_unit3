# hf_agents_course_unit3
HuggingFace Agents course Unit3

Example of RAG agents, created using the smolagents, llama-index, langgraph and google-adk libraries. 
Agents were created based on the Unit3 of the HuggingFace Agents course ([HuggingFAce Agents Unit3](https://huggingface.co/learn/agents-course/unit3/agentic-rag/introduction)) and Google ADK tutorials ([Google ADK](https://google.github.io/adk-docs/))

Use the following commands to run agents:

> python ./smolagents/app.py
> python ./langgraph/app.py
> python ./llama-index/app.py
> python adk run google-adk

>[!NOTE]
>To run google-adk agent with Google model, a Google API key must be specified in the .env file in the root folder:
>
>>GOOGLE_API_KEY=<google_api_key>
>
>To run agents with HuggingFace model, a HuggingFace token must be specified in the .env file in the root folder:
>
>>HF_TOKEN='<hf_api_token>'
>
