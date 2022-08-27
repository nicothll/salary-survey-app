import streamlit as st
import numpy as np
import pandas as pd
import settings


model = settings.MODEL["model"]
columns = settings.MODEL["model_columns"]
countries = settings.CATEGORIES["countries"]
ages = settings.CATEGORIES["age"]
education = settings.CATEGORIES["education"]


def show():
    st.title("Software Developer Salary Prediction")

    st.write(
        """
        ### We need some information to predict the salary
    """
    )

    country = st.selectbox("Country", countries)
    ed_level = st.selectbox("Education level", education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    clicked = st.button("Calculate Salary")

    if clicked:
        X = pd.DataFrame(
            np.array([[country, ed_level, experience, 1]]), columns=columns
        )
        pred_salary = model.predict(X)[0]

        st.subheader(f"The estimated salary is ${pred_salary:,.2f}")
