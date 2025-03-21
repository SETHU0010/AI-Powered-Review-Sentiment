from fastapi import FastAPI
from auth import router as auth_router
from sentiment import router as sentiment_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow frontend to interact with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, change this in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include authentication and sentiment analysis routes
app.include_router(auth_router, prefix="/auth")
app.include_router(sentiment_router, prefix="/review")

@app.get("/")
def root():
    return {"message": "AI Sentiment Analysis API is running!"}

# Run the app when executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
