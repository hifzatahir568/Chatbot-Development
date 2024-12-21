# Chatbot-Development
# PDF Chatbot Application

This project is a Python-based chatbot application that uses AI/ML techniques to provide answers based on content extracted from uploaded PDF documents. Users can upload documents, interact with the chatbot via a simple interface, and deploy the app seamlessly using Docker.

Note: For project configuration and successful execution an openai API Key will be required.

## Features
1. **Document Upload API**:
   - Upload PDF documents through an API endpoint.
   - Extract and process text using `PyPDF2`.

2. **Chatbot API**:
   - Interact with the chatbot via an API endpoint.
   - Leverages OpenAI GPT-3.5 to provide accurate, contextually relevant responses.

3. **User Interface**:
   - Simple and user-friendly web interface for uploading PDFs and chatting.

4. **Deployment**:
   - Fully containerized using Docker for easy deployment.

5. **Code Management**:
   - Clear, well-documented, and version-controlled codebase.

## Requirements

- Python 3.10 or higher
- OpenAI API key
- Docker
- Dependencies listed in `requirements.txt`

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**
   Replace the placeholder in the code with your OpenAI API key:
   ```python
   openai.api_key = "your_openai_api_key"
   ```

4. **Run the Application Locally**
   Start the FastAPI server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   Access the application at [http://localhost:8000](http://localhost:8000).

5. **Run with Docker**
   Build and run the Docker container:
   ```bash
   docker build -t pdf-chatbot .
   docker run -p 8000:8000 pdf-chatbot
   ```

## API Endpoints

### Document Upload
- **URL**: `/upload-pdf`
- **Method**: `POST`
- **Description**: Upload a PDF file and extract its content.
- **Request**: Multipart form-data with `file` parameter.
- **Response**:
  ```json
  {
    "message": "PDF uploaded and processed successfully."
  }
  ```

### Chatbot Interaction
- **URL**: `/chat`
- **Method**: `POST`
- **Description**: Submit a question to the chatbot.
- **Request**: JSON with `question` parameter.
- **Response**:
  ```json
  {
    "answer": "<chatbot_response>"
  }
  ```

## File Structure

- `main.py`: Core application logic and API endpoints.
- `templates/`: HTML files for the user interface.
- `static/`: CSS and JavaScript files.
- `Dockerfile`: Docker configuration for containerization.
- `requirements.txt`: List of dependencies.

## Deployment

To deploy the application:

1. Build the Docker image:
   ```bash
   docker build -t pdf-chatbot .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 pdf-chatbot
   ```

Access the app at [http://localhost:8000](http://localhost:8000).



## Author

Developed by [HIFZA TAHIR].
