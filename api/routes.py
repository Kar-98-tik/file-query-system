from fastapi import APIRouter, UploadFile, Form, HTTPException
from app.services.document_processing import process_uploaded_file
from app.exceptions.custom_exceptions import CustomException
from app.services.document_processing import process_file_and_query

router = APIRouter()

@router.post("/upload/")
async def upload_file(uploaded_file: UploadFile, question: str = Form(...)):
    try:
        query_engine = await process_uploaded_file(uploaded_file)
        if not query_engine:
            raise HTTPException(status_code=400, detail="Error processing the file.")
        
        response = query_engine.query(question)
        return {"status": "success", "answer": response.response}
    except CustomException as e:
        raise HTTPException(status_code=500, detail=f"{e.error_message}: {e.system_error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/process/")
async def process_file_and_query_route(uploaded_file: UploadFile, question: str):
    try:
        # Process file and get response
        result = await process_file_and_query(uploaded_file, question)
        return {
            "status": "success",
            "response": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
