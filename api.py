from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import Recommender

app = FastAPI()

# Load and prepare the model
recommender = Recommender('ratings.csv')
recommender.preprocess_data()
recommender.train_model()

class RecommendationRequest(BaseModel):
    user_id: int
    top_n: int = 10

@app.post("/recommendations")
async def get_recommendations(request: RecommendationRequest):
    try:
        recommendations = recommender.recommend(request.user_id, request.top_n)
        return {"user_id": request.user_id, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))