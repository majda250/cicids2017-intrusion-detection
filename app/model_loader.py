import joblib
from pathlib import Path

MODEL_PATH = Path("best_model/best_model.pkl")


def load_model():
    """
    Charge le meilleur modèle sauvegardé.

    Returns:
        Le modèle entraîné.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Le fichier {MODEL_PATH} est introuvable."
        )

    model = joblib.load(MODEL_PATH)

    return model