import re
import joblib
import pandas as pd
from src.feature_extraction import extract_features

# -------------------------------
# LOAD ML MODEL (URL MODEL)
# -------------------------------
model = joblib.load("model/model.pkl")

# -------------------------------
# TRUSTED EMAIL DOMAINS
# -------------------------------
trusted_domains = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com"
]

# -------------------------------
# EXTRACT FUNCTIONS
# -------------------------------
def extract_urls(text):
    return re.findall(r'https?://\S+|www\.\S+', text)

def extract_emails(text):
    return re.findall(r'\S+@\S+', text)

# -------------------------------
# URL PREDICTION USING ML
# -------------------------------
def predict_url(url):
    if not url.startswith("http"):
        url = "http://" + url

    features = extract_features(url)
    df = pd.DataFrame([features])

    # align columns
    for col in model.feature_names_in_:
        if col not in df.columns:
            df[col] = 0

    df = df[model.feature_names_in_]

    return model.predict(df)[0]

# -------------------------------
# EMAIL PHISHING ANALYZER
# -------------------------------
def analyze_email(text):

    urls = extract_urls(text)
    emails = extract_emails(text)

    score = 0
    total = 0

    print("\n🔍 EMAIL ANALYSIS REPORT\n")

    # ---------------- URLs ----------------
    for url in urls:
        result = predict_url(url)
        total += 1

        if result == 1:
            print(f"URL: {url} → ⚠️ PHISHING")
            score += 2
        else:
            print(f"URL: {url} → ✅ SAFE")

    # ---------------- EMAILS ----------------
    for em in emails:
        domain = em.split("@")[-1].lower()
        total += 1

        if domain in trusted_domains:
            print(f"EMAIL: {em} → ✅ LEGITIMATE")
        else:
            print(f"EMAIL: {em} → ⚠️ SUSPICIOUS")
            score += 1

    # ---------------- KEYWORD CHECK ----------------
    keywords = ["verify", "password", "login", "urgent", "bank", "account", "click"]
    text_lower = text.lower()

    for word in keywords:
        if word in text_lower:
            score += 1

    # ---------------- FINAL DECISION ----------------
    print("\n📊 FINAL RESULT:")

    if score >= 3:
        print("🚨 PHISHING EMAIL DETECTED")
    elif score == 1 or score == 2:
        print("⚠️ SUSPICIOUS EMAIL")
    else:
        print("✅ LEGITIMATE EMAIL")

    print(f"Score: {score}/{total + len(keywords)}")