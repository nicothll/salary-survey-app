import streamlit as st
import predict_page
import explore_page

explore, predict = st.tabs(["Explore", "Predict"])

with predict:
    predict_page.show()

with explore:
    explore_page.show()
