# validate.py

import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import joblib


def main():
    # Load dataset
    df = pd.read_csv("data/Phishing_Email.csv")  # adjust the path as necessary

    # Assume dataset has columns "text" and "label"
    X = df["Email Text"].fillna("")
    y = df["Email Type"]

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Load the trained model
    model = joblib.load("phishing_model.pkl")

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()
