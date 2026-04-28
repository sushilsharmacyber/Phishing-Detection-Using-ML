import joblib
import pandas as pd
from src.feature_extraction import extract_features

def predict_url(url):
    try:
        model = joblib.load("model/model.pkl")

        features = extract_features(url)

        df = pd.DataFrame([features])

        # ensure all columns match training data
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0

        df = df[model.feature_names_in_]

        prediction = model.predict(df)[0]

        # 🔴 ADD THIS FIX (IMPORTANT)
        if prediction == 1:
            return "⚠ Phishing URL"
        else:
            return "✅ Legitimate URL"

    except Exception as e:
        print("❌ Error:", e)
        return "Error occurred"