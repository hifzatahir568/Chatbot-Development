from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PyPDF2 import PdfReader
import openai
import logging
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# OpenAI API Key
openai.api_key = ""  # Replace with your OpenAI API key

# Serve static files (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

# In-memory storage for uploaded document content and chat history
document_content = {}
conversation_history = []  # Stores the entire conversation

# Define a Pydantic model to handle request body
class ChatRequest(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    API endpoint to upload a PDF document and extract its content.
    """
    try:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload a PDF file.")
        
        reader = PdfReader(file.file)
        text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
        if not text.strip():
            raise HTTPException(status_code=400, detail="The uploaded PDF has no extractable text.")
        
        # Store the document content in memory
        document_content["text"] = text
        return {"message": "PDF uploaded and processed successfully."}
    except HTTPException as e:
        logging.error(f"Error processing PDF: {str(e.detail)}")
        raise e
    except Exception as e:
        logging.error(f"Unexpected error processing PDF: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred while processing the PDF.")

@app.post("/chat")
async def chat(request: ChatRequest):
    if "text" not in document_content:
        raise HTTPException(status_code=400, detail="No document uploaded yet. Please upload a PDF first.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Document content: {document_content['text']}\n\nUser question: {request.question}"}
            ],
            max_tokens=200,
            temperature=0.7
        )

        # Validate and extract response
        answer = response.get('choices', [{}])[0].get('message', {}).get('content', '').strip()
        if not answer:
            raise HTTPException(status_code=500, detail="No valid answer received from OpenAI.")
        return {"answer": answer}

    except Exception as e:
        logging.error(f"Error generating response: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")