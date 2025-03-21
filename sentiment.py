import openai
import os
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import Review, SessionLocal
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # Get API key securely

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def analyze_sentiment_with_chatgpt(text):
    prompt = f"Analyze the sentiment of the following review and provide a detailed explanation:\n\n'{text}'"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI sentiment analyzer."},
            {"role": "user", "content": prompt}
        ]
    )

    sentiment_response = response["choices"][0]["message"]["content"]
    return sentiment_response

@router.post("/analyze")
def analyze_review(user_id: int, review_text: str, db: Session = Depends(get_db)):
    chatgpt_response = analyze_sentiment_with_chatgpt(review_text)

    # Extract sentiment from ChatGPT's response
    if "Positive" in chatgpt_response:
        sentiment_label = "Positive"
    elif "Negative" in chatgpt_response:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    review = Review(user_id=user_id, review_text=review_text, sentiment=sentiment_label, explanation=chatgpt_response)
    db.add(review)
    db.commit()

    return {"sentiment": sentiment_label, "explanation": chatgpt_response}
