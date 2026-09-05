#setting up the schema for the feedback request (API Input Validation)

from pydantic import BaseModel, Field


class FeedbackRequest(BaseModel):
    customer_feedback: str = Field(
        min_length=5,
        max_length=5000,
    )