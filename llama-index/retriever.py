import datasets
from llama_index.core.schema import Document
from llama_index.core.tools import FunctionTool
from llama_index.retrievers.bm25 import BM25Retriever

guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")

docs = [
    Document(
        text="\n".join([
                f"Name: {guest_dataset['name'][i]}",
                f"Relation: {guest_dataset['relation'][i]}",
                f"Description: {guest_dataset['description'][i]}",
                f"Email: {guest_dataset['email'][i]}"
            ]),
        metadata={"name": guest_dataset['name'][i]}
    )
    for i in range(len(guest_dataset))
]

bm25_retriever = BM25Retriever.from_defaults(nodes=docs)

def get_guest_info_retriever(query: str) -> str:
    """Retrieves detailed information about gala guests based on their name and relation."""
    results = bm25_retriever.retrieve(query)
    if results:
        return "\n\n".join([doc.text for doc in results[:3]])
    else:
        return "No matching guest information found."
    
def get_guest_conversation_starter(query: str) -> str:
    """Suggests conversation starter for the gala guests based on their interests or background."""
    results = bm25_retriever.retrieve(query)
    if results:
        return "\n\n".join([doc.text for doc in results[:3]])
    else:
        return "No matching guest information found."
    
guest_info_tool = FunctionTool.from_defaults(get_guest_info_retriever)
guest_conversation_starter_tool = FunctionTool.from_defaults(get_guest_conversation_starter)
