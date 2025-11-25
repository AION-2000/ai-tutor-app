import io
import logging
from openai import OpenAI
from ..utils.config import settings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

class SpeechService:
    @staticmethod
    async def transcribe_audio(audio_bytes: bytes, language: str = "en") -> str:
        """
        Transcribes audio to text using OpenAI's Whisper model.
        """
        try:
            logger.info("Received audio file for transcription.")

            # Create a byte stream from the audio bytes
            audio_stream = io.BytesIO(audio_bytes)

            # Use the correct model name for Whisper
            model_name = "whisper-1"

            # Determine the language code for Whisper
            lang_code = "bn" if language == "bangla" else "en"

            logger.info(f"Transcribing audio with model '{model_name}' in language '{lang_code}'...")

            transcription = client.audio.transcriptions.create(
                model=model_name,
                file=audio_stream,
                language=lang_code
            )

            transcribed_text = transcription.text
            logger.info(f"Successfully transcribed audio: '{transcribed_text[:100]}...'")
            return transcribed_text

        except Exception as e:
            logger.error(f"An error occurred during transcription: {e}", exc_info=True)
            return ""