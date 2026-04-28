# Phishing-Detection-Using-ML
 A Machine Learning-based phishing URL detection system that classifies websites as legitimate or malicious using extracted URL features. The project supports bulk analysis of 5000+ URLs, automated report generation, and real detection
🚀 Features
Detect phishing vs legitimate URLs
Bulk URL analysis (5000+ URLs)
Feature extraction from URLs
Machine Learning model (Random Forest)
Automated CSV & PDF report generation
Easy command-line interface
🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
Tldextract
ReportLab

phishing_detection/
│
├── dataset/
├── model/
├── reports/
├── feature_extraction.py
├── train_model.py
├── detector.py
├── bulk_test.py
├── report_generator.py
├── main.py
└── requirements.txt
▶️ How to Run
python main.py
📊 Output
bulk_results.csv → URL predictions
report.pdf → Summary report
📚 Dataset
5000+ legitimate URLs
Phishing URLs dataset
Combined and labeled for training
📈 Model Performance
Algorithm: Random Forest
Metrics: Accuracy, Precision, Recall, F1-score

🔮 Future Scope
GUI-based interface
Real-time browser extension
Deep learning models
API integration

📜 License

This project is licensed under the MIT License.
