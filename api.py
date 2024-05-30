from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class RecommendationRequest(BaseModel):
    mood: str
    day: str
    genre: str
    duration: str

@app.post("/recommend")
async def get_recommendations(request: RecommendationRequest):
    try:
        recommendations = generate_recommendations(request.mood, request.day, request.genre, request.duration)
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def generate_recommendations(mood, day, genre, duration):
    # This function will be implemented in the next step
    return ["Movie 1", "Movie 2", "Movie 3"]