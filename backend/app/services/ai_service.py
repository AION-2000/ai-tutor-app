import openai
from typing import Dict, Any
from ..utils.config import settings

# Initialize the OpenAI client with the API key from our settings
client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

class AIService:
    @staticmethod
    async def solve_question(question_text: str, subject: str, class_level: str, language: str = "english") -> Dict[str, Any]:
        """
        Generates a solution for a given question using the OpenAI API.
        """
        language_instruction = "in Bangla" if language == "bangla" else "in simple English"

        # This is the prompt we send to the AI. We are engineering it to get the best possible response.
        prompt = f"""
        You are an expert AI tutor for Bangladeshi students. Your task is to provide a clear, step-by-step solution to the following question.

        **Instructions:**
        - The solution must be {language_instruction}.
        - The question is for a student in {class_level}, studying {subject}.
        - Provide a detailed, step-by-step explanation.
        - End with a short, concise summary of the answer.

        **Question:** {question_text}
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Using a fast and cost-effective model
                messages=[
                    {"role": "system", "content": "You are a helpful AI tutor for Bangladeshi students."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,  # Lower temperature for more factual answers
                max_tokens=1000   # Limit the response length
            )

            answer = response.choices[0].message.content

            return {
                "question": question_text,
                "answer": answer,
                "subject": subject,
                "class_level": class_level,
                "language": language
            }
        except Exception as e:
            # It's important to handle potential errors from the API
            print(f"Error calling OpenAI: {e}")
            return {
                "error": "Failed to generate an answer. Please try again later.",
                "details": str(e)
            }