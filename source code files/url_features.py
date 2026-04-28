import re
import tldextract

def extract_features(url):
    features = []

    # Have_IP
    features.append(1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0)

    # Have_At
    features.append(1 if "@" in url else 0)

    # URL_Length
    features.append(1 if len(url) < 54 else 2 if len(url) <= 75 else 3)

    # URL_Depth
    features.append(url.count('/'))

    # Redirection
    features.append(1 if "//" in url[7:] else 0)

    # https_Domain
    features.append(1 if "https" in url else 0)

    # Tiny_URL
    shortening = r"bit\.ly|goo\.gl|tinyurl|t\.co"
    features.append(1 if re.search(shortening, url) else 0)

    # Prefix/Suffix
    features.append(1 if "-" in url else 0)

    # DNS_Record (dummy)
    features.append(0)

    # Web_Traffic (dummy)
    features.append(1)

    # Domain_Age (dummy)
    features.append(1)

    # Domain_End (dummy)
    features.append(1)

    # iFrame
    features.append(0)

    # Mouse_Over
    features.append(0)

    # Right_Click
    features.append(1)

    # Web_Forwards
    features.append(0)

    return features