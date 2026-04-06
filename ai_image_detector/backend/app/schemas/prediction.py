from pydantic import BaseModel


class PredictionResponse(BaseModel):
    filename: str
    score: float
    label: str