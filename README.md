RAG with Agents using FAISS and GROQ Cloud

📌 Overview

This project implements Retrieval-Augmented Generation (RAG) with Agents using FAISS for vector storage and GROQ Cloud as the LLM API. The system allows users to upload files, process them through an embedding model from Hugging Face, and retrieve relevant information using an agent-based approach.

🚀 Features

File Upload & Processing: Users can upload files for ingestion into the RAG system.

Vector Database (FAISS): Stores embeddings of the uploaded documents for efficient retrieval.

Hugging Face Embedding Model: Uses an open-source embedding model to convert text into vector representations.

GROQ Cloud for LLM: Utilizes GROQ Cloud API for fast and efficient response generation.

Agent-Based Querying: Queries are processed via agents to enhance context-aware responses.



🔑 Environment Variables

Before running the project, set up the following environment variables:

export GROQ_API_KEY="your-groq-api-key"



🏃 Usage

1️⃣ Run the Application

python app.py

2️⃣ Upload a File

Access the application (if using a web interface) or place the file in a designated folder.

The system will process and store embeddings in FAISS.

3️⃣ Query the System

Input your query, and the agent will retrieve relevant information using FAISS and generate responses using GROQ Cloud.

🔥 Technologies Used

FAISS - Vector storage for efficient similarity search

Hugging Face - Open-source embeddings model

GROQ Cloud - LLM API for response generation

Python - Core development language

🤝 Contributions

Feel free to fork this repository and submit pull requests!

📞 Contact

For any issues or feature requests, please open an issue on the repository.



