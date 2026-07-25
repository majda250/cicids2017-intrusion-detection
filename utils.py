import pandas as pd
import os


def save_results(
    model_name,
    accuracy,
    precision,
    recall,
    f1_score,
    train_time,
    prediction_time,
    file_path="results/model_results.csv"
):
    """
    Sauvegarde automatiquement les résultats d'un modèle.
    """

    # Créer automatiquement le dossier s'il n'existe pas
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    result = pd.DataFrame([{
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-score": f1_score,
        "Training Time (s)": train_time,
        "Prediction Time (s)": prediction_time
    }])

    if os.path.exists(file_path):

        old = pd.read_csv(file_path)

        # Supprimer l'ancien résultat du même modèle
        old = old[old["Model"] != model_name]

        result = pd.concat([old, result], ignore_index=True)

    result.to_csv(file_path, index=False)

    print(f"{model_name} enregistré avec succès.")