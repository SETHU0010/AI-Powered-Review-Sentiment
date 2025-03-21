from fastapi import FastAPI
from auth import router as auth_router
from sentiment import router as sentiment_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(sentiment_router, prefix="/review")

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running"}
