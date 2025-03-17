# train.py

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def main():
    # Load dataset
    df = pd.read_csv("data/Phishing_Email.csv")  # adjust the path as necessary

    # Assume dataset has columns "text" and "label"
    X = df["Email Text"].fillna("")
    y = df["Email Type"]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create a pipeline with TF-IDF and Logistic Regression
    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer(stop_words="english")),
            ("clf", LogisticRegression(solver="liblinear")),
        ]
    )

    # Train the model
    pipeline.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(pipeline, "phishing_model.pkl")
    print("Model trained and saved as phishing_model.pkl")


if __name__ == "__main__":
    main()
