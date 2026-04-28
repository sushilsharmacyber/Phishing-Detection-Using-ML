import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train():
    print("[+] Loading datasets...")

    # ✅ Step 1: Load datasets
    phish = pd.read_csv("dataset/phishing_dataset.csv")
    legit = pd.read_csv("dataset/legitimate_dataset.csv")

    # ✅ Step 2: Combine datasets
    data = pd.concat([phish, legit], ignore_index=True)

    # ✅ Step 3: NOW fix duplicate column (HERE ONLY)
    if "Tiny_URL" in data.columns:
        data = data.drop(columns=["Tiny_URL"])

    # ✅ Step 4: Features & labels
    X = data.drop(columns=["Domain", "Label", "TinyURL"])
    y = data["Label"]

    print("[+] Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("[+] Training model...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=20,
        class_weight='balanced',
        random_state=42
    )

    model.fit(X_train, y_train)

    # Feature importance
    importance = pd.Series(model.feature_importances_, index=X.columns)
    print("\nFeature Importance:\n", importance.sort_values(ascending=False))

    # Accuracy
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("✅ Accuracy:", acc)

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")
    print("✅ Model saved!")

if __name__ == "__main__":
    train()