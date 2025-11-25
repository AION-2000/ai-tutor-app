from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from typing import Optional

from ..services.ai_service import AIService
from ..services.ocr_service import OCRService
from ..services.speech_service import SpeechService # <-- New import

# Create a router instance
router = APIRouter()

# Define the structure of the request data using Pydantic for validation
class QuestionRequest(BaseModel):
    text: str
    subject: str
    class_level: str
    language: Optional[str] = "english"

@router.post("/solve_question")
async def solve_question(question_data: QuestionRequest):
    """
    Receives a question and returns an AI-generated solution.
    """
    # Call our AI service to get the answer
    solution = await AIService.solve_question(
        question_text=question_data.text,
        subject=question_data.subject,
        class_level=question_data.class_level,
        language=question_data.language
    )

    return solution

@router.post("/solve_from_image")
async def solve_from_image(
        file: UploadFile = File(...),
        subject: str = "General",
        class_level: str = "Class 9-10",
        language: str = "english"
):
    """
    Receives an image file, extracts text using OCR, and solves the question.
    """
    # 1. Read the uploaded file's content
    image_bytes = await file.read()

    # 2. Extract text from the image using our OCR service
    question_text = OCRService.extract_text_from_image(image_bytes)

    if not question_text:
        return {"error": "Could not extract any text from the image. Please try a clearer image."}

    # 3. Pass the extracted text to our AI service to get the solution
    solution = await AIService.solve_question(
        question_text=question_text,
        subject=subject,
        class_level=class_level,
        language=language
    )

    # Add the original extracted text to the response for context
    solution["extracted_text"] = question_text

    return solution

@router.post("/solve_from_audio") # <-- New endpoint
async def solve_from_audio(
        file: UploadFile = File(...),
        subject: str = "General",
        class_level: str = "Class 9-10",
        language: str = "english"
):
    """
    Receives an audio file, transcribes it to text, and solves the question.
    """
    # 1. Read the uploaded file's content
    audio_bytes = await file.read()

    # 2. Transcribe the audio using our speech service
    question_text = await SpeechService.transcribe_audio(audio_bytes, language)

    if not question_text:
        return {"error": "Could not transcribe any audio. Please try a clearer recording."}

    # 3. Pass the transcribed text to our AI service to get the solution
    solution = await AIService.solve_question(
        question_text=question_text,
        subject=subject,
        class_level=class_level,
        language=language
    )

    # Add the original transcribed text to the response for context
    solution["transcribed_text"] = question_text

    return solution