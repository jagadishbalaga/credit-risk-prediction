# 1 = Good (lower risk)
# 0 = Bad (higher risk)

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('extra_trees_credit_model.pkl')

# Load encoders
encoders = {
    col: joblib.load(f'{col}_encoder.pkl')
    for col in ['Sex', 'housing', 'Saving accounts', 'Checking account']
}

# App title
st.title('Credit Risk Prediction App')

st.write('Enter applicant information to predict whether the credit risk is Good or Bad.')

# User inputs
age = st.number_input(
    'Age',
    min_value=18,
    max_value=80,
    value=30
)

Sex = st.selectbox(
    'Sex',
    ['male', 'female']
)

job = st.number_input(
    'Job (0-3)',
    min_value=0,
    max_value=3,
    value=1
)

housing = st.selectbox(
    'Housing',
    ['own', 'rent', 'free']
)

saving_accounts = st.selectbox(
    'Saving accounts',
    ['little', 'moderate', 'rich', 'quite rich']
)

checking_account = st.selectbox(
    'Checking account',
    ['little', 'moderate', 'rich']
)

credit_amount = st.number_input(
    'Credit amount',
    min_value=0,
    value=1000
)

duration = st.number_input(
    'Duration (months)',
    min_value=1,
    value=12
)

# Create input DataFrame
input_df = pd.DataFrame({
    'Age': [age],
    'Sex': [encoders['Sex'].transform([Sex])[0]],
    'Job': [job],
    'Housing': [encoders['housing'].transform([housing])[0]],
    'Saving accounts': [encoders['Saving accounts'].transform([saving_accounts])[0]],
    'Checking account': [encoders['Checking account'].transform([checking_account])[0]],
    'Credit amount': [credit_amount],
    'Duration': [duration]
})

# Prediction
if st.button('Predict Risk'):

    pred = model.predict(input_df)[0]

    if pred == 1:
        st.success('The predicted credit risk is: **Good**')
    else:
        st.error('The predicted credit risk is: **Bad**')
        