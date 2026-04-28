import re

def extract_features(url):
    features = {}

    features["Have_IP"] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features["Have_At"] = 1 if "@" in url else 0
    features["URL_Length"] = len(url)
    features["URL_Depth"] = url.count('/')
    features["Redirection"] = 1 if '//' in url[7:] else 0
    features["https_Domain"] = 1 if 'https' in url else 0
    features["Prefix/Suffix"] = 1 if '-' in url else 0

    # Better defaults
    features["DNS_Record"] = 1
    features["Web_Traffic"] = 1
    features["Domain_Age"] = 1
    features["Domain_End"] = 1

    features["iFrame"] = 0
    features["Mouse_Over"] = 0
    features["Right_Click"] = 0
    features["Web_Forwards"] = 0

    return features