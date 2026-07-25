import numpy as np

from app.schemas import PredictionInput

# Correspondance entre les identifiants numériques
# et les noms des classes
LABELS = {
    0: "BENIGN",
    1: "Bot",
    2: "DDoS",
    3: "DoS GoldenEye",
    4: "DoS Hulk",
    5: "DoS Slowhttptest",
    6: "DoS slowloris",
    7: "FTP-Patator",
    8: "Heartbleed",
    9: "Infiltration",
    10: "PortScan",
    11: "SSH-Patator",
    12: "Web Attack - Brute Force",
    13: "Web Attack - Sql Injection",
    14: "Web Attack - XSS"
}


def predict(model, data: PredictionInput):
    """
    Effectue une prédiction à partir
    des données reçues par l'API.
    """

    # Conversion des données Pydantic
    # vers un tableau NumPy
    features = np.array([
    list(data.model_dump(by_alias=False).values())
    ])

    # Prédiction
    prediction = int(model.predict(features)[0])

    # Conversion en nom de classe
    label = LABELS[prediction]

    return {
        "prediction": prediction,
        "label": label
    }