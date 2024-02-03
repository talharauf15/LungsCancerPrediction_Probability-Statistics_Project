from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

def perform_logistic_regression(data, predictors, target):
    # Preparing the data
    X = data[predictors]
    y = data[target]

    # Splitting the data 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Creating regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluating the model
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions)

    return report
