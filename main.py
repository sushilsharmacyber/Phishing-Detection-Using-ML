def menu():
    while True:
        print("\n===== PHISHING DETECTION SYSTEM =====")
        print("1. Train Model")
        print("2. Manual URL Detection")
        print("3. Bulk Detection")
        print("4. Email Detection")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            from src.train_model import train
            train()

        elif choice == "2":
            from src.predict import predict_url
            url = input("Enter URL: ")
            print(predict_url(url))

        elif choice == "3":
            from src.bulk_test import bulk_test
            bulk_test()

        elif choice == "4":
            from src.email_analyzer import analyze_email
            print("\nPaste email content:")
            email_text = input()
            analyze_email(email_text)

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()