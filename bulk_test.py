import pandas as pd
import joblib
import os

def bulk_test():
    model = joblib.load("model/model.pkl")

    print("[+] Testing Phishing URLs...")
    phish = pd.read_csv("dataset/phishing_dataset.csv")

    print("[+] Testing Legitimate URLs...")
    legit = pd.read_csv("dataset/legitimate_dataset.csv")

    # Prepare data
    X_phish = phish.drop(columns=["Domain", "Label"])
    y_phish = phish["Label"]

    X_legit = legit.drop(columns=["Domain", "Label"])
    y_legit = legit["Label"]

    # Clean column names
    X_phish.columns = X_phish.columns.str.strip()
    X_legit.columns = X_legit.columns.str.strip()

    # Fix column naming issues
    X_phish = X_phish.rename(columns={
        "Tiny_URL": "TinyURL",
        "Tiny-URL": "TinyURL"
    })

    X_legit = X_legit.rename(columns={
        "Tiny_URL": "TinyURL",
        "Tiny-URL": "TinyURL"
    })

    # Match model features
    expected_columns = model.feature_names_in_

    for col in expected_columns:
        if col not in X_phish.columns:
            X_phish[col] = 0
        if col not in X_legit.columns:
            X_legit[col] = 0

    X_phish = X_phish[expected_columns]
    X_legit = X_legit[expected_columns]

    # Predictions (IMPORTANT: no extra space here)
    pred_phish = model.predict(X_phish)
    pred_legit = model.predict(X_legit)

    # Accuracy
    phish_acc = (pred_phish == y_phish).mean()
    legit_acc = (pred_legit == y_legit).mean()
    total_acc = (phish_acc + legit_acc) / 2

    print("\n✅ Phishing Accuracy:", phish_acc)
    print("✅ Legitimate Accuracy:", legit_acc)
    print("🔥 Overall Accuracy:", total_acc)

    # Save report
    os.makedirs("results", exist_ok=True)

    with open("results/report.txt", "w", encoding="utf-8") as f:
        f.write(f"Phishing Accuracy: {phish_acc}\n")
        f.write(f"Legitimate Accuracy: {legit_acc}\n")
        f.write(f"Overall Accuracy: {total_acc}\n\n")

        f.write("Sample Results:\n")

        for i in range(min(50, len(phish))):
            f.write(f"{phish['Domain'][i]} -> {pred_phish[i]}\n")

        for i in range(min(50, len(legit))):
            f.write(f"{legit['Domain'][i]} -> {pred_legit[i]}\n")

    print("✅ Report saved in results/report.txt")