# Document Q&A Assistant

## Overview
The **Document Q&A Assistant** is a robust application built with FastAPI that allows users to upload files (e.g., PDF, TXT, DOCX) and perform two main operations:
1. **Summarize the Entire Document:** Generate a concise summary of the uploaded file.
2. **Answer Specific Questions:** Answer user-provided questions based on the content of the uploaded document.

It leverages the **Gemini-Pro NLP Model**, **LlamaIndex**, and **Google Generative AI** to process, summarize, and query document content intelligently.

---

## Features
- **File Upload Support:** Accepts multiple file formats including PDF, TXT, DOCX.
- **Document Summarization:** Provides a high-level summary of the entire document.
- **Intelligent Q&A:** Answers specific queries about the uploaded document.
- **Consistent JSON Responses:** Returns output in a structured JSON format for easy integration.
- **Error Handling:** Includes custom exceptions and detailed error messages.

---

## Installation

### Prerequisites
- Python 3.8+
- Virtual Environment Tool (e.g., `venv` or `conda`)

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Kar-98-tik/file-query-system
   cd https://github.com/Kar-98-tik/file-query-system
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   - Create a `.env` file in the project root.
   - Add the following:
     ```env
     GOOGLE_API_KEY=<your-google-api-key>
     ```

5. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## API Endpoints

### 1. **Upload and Query Document**
- **Endpoint:** `/process/`
- **Method:** `POST`
- **Description:** Summarizes the document and answers a user query.
- **Request:**
  ```json
  {
    "uploaded_file": <file>,
    "question": "Summarize the financial trends in the document"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "response": {
      "summary": "The document outlines marketing trends...",
      "answer": "The financial section shows a 15% growth in revenue."
    }
  }
  ```

### 2. **Summarize Document**
- **Endpoint:** `/summarize/`
- **Method:** `POST`
- **Description:** Provides a high-level summary of the uploaded document.
- **Request:**
  ```json
  {
    "uploaded_file": <file>
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "response": {
      "summary": "The document discusses marketing trends and revenue growth..."
    }
  }
  ```

---

## Example JSON Response
### For Summarization:
```json
{
  "status": "success",
  "response": {
    "summary": "The document discusses financial trends including revenue growth of 15%."
  }
}
```

### For Query:
```json
{
  "status": "success",
  "response": {
    "summary": "The document outlines multiple marketing campaigns.",
    "answer": "The Electronics division contributed 50% of revenue but faced a 10% decline in profit margins."
  }
}
```

---

## Error Handling
- **Missing API Key:**
  ```json
  {
    "detail": "Missing API key in environment variables."
  }
  ```

- **Unsupported File Type:**
  ```json
  {
    "detail": "File type not supported. Please upload a PDF, TXT, or DOCX file."
  }
  ```

- **Internal Server Error:**
  ```json
  {
    "detail": "An unexpected error occurred while processing the file."
  }
  ```

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For questions or feedback, please contact:
- **Name:** Kartik (Username: kar98tik)
- **Email:** kartikprayagi0@gmail.com
- **GitHub:** https://github.com/Kar-98-tik

