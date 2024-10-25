import os
import joblib
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import sklearn
# import seaborn as sns
import warnings
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report, accuracy_score

input_data = None

warnings.filterwarnings('ignore')
# plt.rcParams["figure.figsize"] = [10,5]
# Ignore warnings

import warnings
# Set the warning filter to ignore FutureWarning
warnings.simplefilter(action = "ignore", category = FutureWarning)


def take_input():

    global input_data

    os.system('cls')

    pclass = input("Enter Class: ")
    age = input("Enter Age: ")
    sibSp = input("Enter SibSp: ")
    parch = input("Enter Parch: ")
    fare = input("Enter Fare: ")

    input_data = pd.DataFrame({
            'Pclass': [pclass],
            'Age': [age],
            'SibSp': [sibSp],
            'Parch': [parch],
            'Fare': [fare]
        })

    predict_input()

def predict_input():

    global input_data

    prediction = lreg.predict(input_data)
    if prediction:
        print("\n\nPrediction ---> Survived", end="")
    else:
        print("\n\nPrediction ---> Didn't Survived", end="")

    input("\n\nDone Prediction....")

    take_input()


# Load model
print("Loading Model...")
lreg = joblib.load("LogisticRegressionModel.pkl")
print("Model Loaded...")


take_input()
