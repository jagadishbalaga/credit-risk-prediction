# Credit Risk Prediction

## Objective

Predict whether a customer has **Good** or **Bad** credit risk using Machine Learning.

## Steps

1. **Data Loading**

   * Loaded German Credit dataset using Pandas.

2. **Data Cleaning**

   * Checked missing values and duplicates.
   * Removed missing values.
   * Removed unnecessary column.

3. **EDA**

   * Analyzed numerical and categorical features.
   * Used histograms, boxplots, countplots, scatterplots and heatmap.
   * Compared features with Risk.

4. **Feature Selection**

   * Selected important features such as Age, Sex, Job, Housing, Saving accounts, Checking account, Credit amount and Duration.

5. **Encoding**

   * Converted categorical values into numbers using `LabelEncoder`.

6. **Train-Test Split**

   * Split data into **80% training** and **20% testing** data.

7. **Model Training**

   * Trained:

     * Decision Tree
     * Random Forest
     * Extra Trees
     * XGBoost

8. **Hyperparameter Tuning**

   * Used `GridSearchCV` to find the best parameters.

9. **Model Evaluation**

   * Compared models using **Accuracy**.

10. **Model Saving**

* Saved the best Extra Trees model using `joblib`.

11. **Deployment**

* Created a **Streamlit** application.
* User enters customer details.
* Model predicts **Good** or **Bad** credit risk.

## Tools

**Python | Pandas | NumPy | Matplotlib | Seaborn | Scikit-learn | XGBoost | Joblib | Streamlit**

## Result

A machine learning model was developed and deployed as a Streamlit application for credit risk prediction.
## Installation

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib streamlit
```

## Run the Project

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in the browser.

Usually:

```text
http://localhost:8501
```
