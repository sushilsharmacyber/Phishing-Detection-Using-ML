def generate_report(phish_results, legit_results, accuracy):
    import os

    os.makedirs("report", exist_ok=True)

    with open("report/report.txt", "w", encoding="utf-8") as f:
        f.write("PHISHING DETECTION REPORT\n")
        f.write("="*40 + "\n\n")

        f.write(f"Overall Accuracy: {accuracy}\n\n")

        f.write("Sample Phishing Results:\n")
        for url, res in phish_results[:50]:
            f.write(f"{url} -> {res}\n")

        f.write("\nSample Legitimate Results:\n")
        for url, res in legit_results[:50]:
            f.write(f"{url} -> {res}\n")

    print("📄 Report saved in report/report.txt")