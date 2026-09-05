from fastapi import FastAPI, HTTPException

from app.schemas import FeedbackRequest
from app.llm import analyze_feedback


app = FastAPI(
    title="AI Customer Feedback Analyzer",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(request: FeedbackRequest):

    try:
        result = analyze_feedback(
            request.customer_feedback
        )

        return {
            "result": result
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to analyze customer feedback."
        )