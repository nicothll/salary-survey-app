import streamlit as st
import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
import os


def load_data():
    return pd.read_csv(f"{os.getcwd()}/data/survey_results_cleaned.csv")


df = load_data()


def show():
    st.title("Explore Software Engineer Salaries")

    st.subheader("Stack Overflow Developer Survey 2022")

    st.write("#### Countries who responded to the survey")

    data = df["Country"].value_counts()

    explode = [0.05 for _ in range(data.shape[0])]

    fig = go.Figure(data=[go.Pie(labels=data.index, values=data, hole=0, pull=explode)])
    fig.update_layout(height=600, width=600)

    st.plotly_chart(fig, use_container_width=True)

    st.write("#### Average Salary by Country (in USD)")

    data = df.groupby(["Country"]).mean()
    fig2 = px.bar(data, y="Salary", x=data.index, text_auto=".2s")

    fig2.update_layout(height=600, width=900)

    st.plotly_chart(fig2, use_container_width=True)

    st.write("#### Average Salary by Experience")

    data = df.groupby(["YearsCodePro"]).mean()
    fig3 = px.line(data, y="Salary", x=data.index)

    fig3.data[0].line.color = "#7bf542"
    fig3.update_layout(height=600, width=900)

    st.plotly_chart(fig3, use_container_width=True)
