from fastapi import FastAPI
from backend.app.api.routes import router

app = FastAPI(title="HealthBridge API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "HealthBridge API running"}