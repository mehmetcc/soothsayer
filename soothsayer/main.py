from dataclasses import dataclass
from fastapi import FastAPI
from typing import Dict, Optional
import uvicorn

from soothsayer.config import ConfigurationService
from soothsayer.prediction import PredictionService


app = FastAPI()

# Services
config = ConfigurationService().load()
prediction_service = PredictionService()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "It's alive!"}

@dataclass
class PredictionRequest:
    text: str


@dataclass
class PredictionResponse:
    text: str
    value: Optional[str]
    score: Optional[float]


@app.get("/prediction", response_model=PredictionResponse)
async def predict(request: PredictionRequest) -> PredictionResponse:
    result = prediction_service.predict(request.text)
    response = PredictionResponse(result.text, result.value, result.score)
    return response


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("soothsayer.main:app", host=config["Server"]["host"], port=int(
        config["Server"]["port"]), reload=True)
