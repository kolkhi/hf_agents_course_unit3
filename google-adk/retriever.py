import datasets
from langchain.docstore.document import Document
from langchain.tools import Tool
from langchain_community.retrievers import BM25Retriever

guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")

docs = [
    Document(
        page_content="\n".join([
                f"Name: {guest['name']}",
                f"Relation: {guest['relation']}",
                f"Description: {guest['description']}",
                f"Email: {guest['email']}"
            ]),
        metadata={"name": guest['name']}
    )
    for guest in guest_dataset
]

bm25_retriever = BM25Retriever.from_documents(documents=docs)

def extract_text(query: str) -> str:
    """Retrieves detailed information about gala guests based on their name or relation.
    
    Args:
        query (str): The name or relation of the guest you want information about.

    Returns:
        str: A string containing detailed information about the guest.
    """
    results = bm25_retriever.invoke(query)
    if results:
        return "\n\n".join([doc.page_content for doc in results[:3]])
    else:
        return "No matching guest information found."