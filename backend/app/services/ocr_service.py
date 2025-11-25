import logging
import easyocr

# Set up logging to see detailed output in the terminal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the EasyOCR reader. This might download models the first time it runs.
# We specify 'en' for English and 'bn' for Bangla to support both.
# Initialize the reader once to avoid reloading it on every request
try:
    logger.info("Initializing EasyOCR reader...")
    reader = easyocr.Reader(['en', 'bn'])
    logger.info("EasyOCR reader initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize EasyOCR reader: {e}")
    reader = None

class OCRService:
    @staticmethod
    def extract_text_from_image(image_bytes: bytes) -> str:
        """
        Extracts text from an image using EasyOCR.
        """
        if reader is None:
            logger.error("OCR reader is not available.")
            return ""

        try:
            logger.info("Received image for OCR processing.")

            # Use EasyOCR to read the text directly from bytes
            logger.info("Running EasyOCR readtext...")
            results = reader.readtext(image_bytes) # <-- THE FIX IS HERE
            logger.info(f"EasyOCR processing complete. Found {len(results)} results.")

            if not results:
                logger.warning("EasyOCR returned no results. The image might not contain readable text.")
                return ""

            # Combine all the detected text into a single string
            extracted_text = " ".join([result[1] for result in results])

            logger.info(f"Successfully extracted text: '{extracted_text[:100]}...'")
            return extracted_text

        except Exception as e:
            logger.error(f"An error occurred during OCR processing: {e}", exc_info=True)
            # Return an empty string or raise an exception, depending on desired behavior
            return ""