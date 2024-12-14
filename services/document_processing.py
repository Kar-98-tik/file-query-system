import os
from fastapi import UploadFile
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.gemini import GeminiEmbedding
from app.services.model_loading import load_model

async def process_uploaded_file(uploaded_file: UploadFile):
    try:
        temp_dir = "temp"
        os.makedirs(temp_dir, exist_ok=True)
        
        file_path = os.path.join(temp_dir, uploaded_file.filename)
        with open(file_path, "wb") as f:
            f.write(await uploaded_file.read())
        
        loader = SimpleDirectoryReader(temp_dir)
        documents = loader.load_data()
        
        model = load_model()
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        
        index = VectorStoreIndex.from_documents(
            documents, 
            llm=model, 
            embed_model=gemini_embed_model, 
            chunk_size=800, 
            chunk_overlap=20
        )
        
        return index.as_query_engine(llm=model)
    finally:
        if os.path.exists(temp_dir):
            for file in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, file))
            os.rmdir(temp_dir)

async def process_file_and_query(uploaded_file: UploadFile, user_question: str):
    try:
        # Save the uploaded file temporarily
        temp_dir = "temp"
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, uploaded_file.filename)
        with open(file_path, "wb") as f:
            f.write(await uploaded_file.read())

        # Load the document
        loader = SimpleDirectoryReader(temp_dir)
        documents = loader.load_data()

        # Combine all text from the document
        document_text = " ".join([doc.text for doc in documents])

        # Load the model
        model = load_model()

        # Generate combined summary and answer
        prompt = f"""
        You are an intelligent assistant. I will provide you with the content of a document. 
        1. First, provide a brief summary of the entire document.
        2. Then, answer a specific question based on the document.

        Document Content:
        {document_text}

        ---

        1. Summary:
        Provide a concise summary of the document content in 5–7 sentences.

        2. Question:
        {user_question}

        Answer:
        """

        # Generate response
        response = model.complete(
            prompt=prompt,
        )

        # Extract the response text
        result_text = response["text"]

        # Split response into summary and answer
        summary, answer = result_text.split("Answer:", 1)
        return {
            "summary": summary.strip(),
            "answer": answer.strip()
        }
    finally:
        # Cleanup temporary files
        if os.path.exists(temp_dir):
            for file in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, file))
            os.rmdir(temp_dir)
