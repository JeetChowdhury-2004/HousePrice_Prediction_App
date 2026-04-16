import streamlit as st
import numpy as np
import joblib
import streamlit.components.v1 as components
import plotly.graph_objects as go

st.set_page_config(page_title="Pro House Price Predictor", layout="wide")

st.title("🏠 Smart Real Estate Dashboard")
st.markdown("---")

st.set_page_config(page_title="Pro House Price Predictor", layout="wide")

st.title("🏠 Smart Real Estate Dashboard")
st.markdown("---")

components.html(""" YOUR FULL HTML CODE """, height=420)

# Load model
model = joblib.load("Random_search.pkl")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Property Details")

    bedroom = st.number_input("Bedrooms", 0, 10, 2)
    bathroom = st.number_input("Bathrooms", 0, 10, 2)
    living_area = st.number_input("Living Area", 500, 10000, 2000)
    condition = st.slider("Condition", 1, 5, 3)
    school = st.number_input("Nearby Schools", 0, 10, 2)

    if st.button("Predict"):
        x = np.array([[bedroom, bathroom, living_area, condition, school]])
        price = int(model.predict(x)[0])
        st.success(f"💰 Price: ₹ {price:,}")
