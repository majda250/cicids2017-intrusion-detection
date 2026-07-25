from fastapi import FastAPI

from app.model_loader import load_model

from app.schemas import PredictionInput, PredictionOutput
from app.prediction import predict

# Chargement du meilleur modèle
model = load_model()

# Création de l'application FastAPI
app = FastAPI(
    title="Network Intrusion Detection API",
    description="API REST pour la détection des intrusions réseau basée sur le Machine Learning",
    version="1.0.0"
)

# Route d'accueil
@app.get("/")
def home():
    return {
        "message": "Bienvenue sur l'API de détection d'intrusions réseau.",
        "status": "API opérationnelle"
    }

@app.post(
    "/predict",
    response_model=PredictionOutput
)
def predict_intrusion(data: PredictionInput):

    result = predict(model, data)

    return result