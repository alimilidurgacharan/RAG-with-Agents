from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.indices.vector_store.base import VectorStoreIndex
from llama_index.core.readers import SimpleDirectoryReader
from llama_index.core import load_index_from_storage
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.llms.groq import Groq
import faiss 
import streamlit as st

# dimensions of text-ada-embedding-002
d = 384
faiss_index = faiss.IndexFlatL2(d)

Settings.llm = Groq(model="llama3-70b-8192", api_key="YOUR_API_KEY")
vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
documents = SimpleDirectoryReader("data").load_data()

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)
index.storage_context.persist()

vecotr_store = FaissVectorStore.from_persist_dir("./storage")
storage_context = StorageContext.from_defaults(vector_store = vector_store, persist_dir = "./storage")
index = load_index_from_storage(storage_context = storage_context, embed_model = embed_model)
query_engine = index.as_query_engine()
response = query_engine.query("give me breify summary of canadian budget 2023 in tabular form")
print(response)
