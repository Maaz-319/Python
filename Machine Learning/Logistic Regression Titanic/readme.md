# 🚢 Titanic Survival Prediction using Logistic Regression

This project builds a logistic regression model to predict passenger survival on the Titanic using key features such as class, age, number of parents/children, siblings/spouses, and fare. The model was trained on the Titanic dataset, using Python. This is my 1st ever ML project.

---
## Used Libraries
1. **SKLearn**: For Logistic Regression Model
2. **Joblib**: For Dumping and Loading the Model
3. **Pandas**: For Data Manipulation
---

## 📋 Project Overview

Using machine learning, this project aims to:
- Identify which factors influenced passenger survival.
- Predict if a passenger would survive based on their personal attributes and ticket class.

### Features Used:
1. **Class**
2. **Age**
3. **Parch**
4. **SibSp**
5. **Fare**

The model output indicates:
- `1` for "Survived"
- `0` for "Did Not Survive"

## Accuracy:- **75%**
---

## 🛠 Project Workflow
1. ### Data Preprocessing
	• Data Cleaning: Handle missing values, especially for Age.
	• Feature Engineering: Select and scale the features Pclass, Age, Parch, SibSp, and Fare.
2. ### Model Training
	• A logistic regression model was trained using scikit-learn.
3. ### Model Saving
	• The trained model is saved as LogisticRegressionModel.pkl using joblib for quick loading and inference.
4. ### Prediction
• The model is loaded and used to make predictions on new data, indicating whether a passenger would have survived or not.

---
### Feedbacks are highly appreciated! ☺

## 📚 References:

### Logistic Regression: https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegression.html
---