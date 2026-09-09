import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config(page_title="Prediction", page_icon="🔍", layout="wide")

st.markdown("""
<h1 style='font-size:55px;color:#6C4CF1;'>
🔍 Penguin Species Prediction
</h1>
""", unsafe_allow_html=True)
st.caption("Predict penguin species using machine learning")

st.sidebar.markdown("## 🔍 Prediction Info")

st.sidebar.info("""
Enter penguin characteristics to predict
the penguin species using the trained
machine learning model.
""")

st.sidebar.markdown("## 🤖 Model Used")

st.sidebar.success("""
Logistic Regression
""")

st.sidebar.markdown("## 🧠 Input Features")

st.sidebar.write("""
• Culmen Length  
• Culmen Depth  
• Flipper Length  
• Body Mass  
• Island  
• Sex  
""")

st.sidebar.markdown("## 🎯 Prediction Goal")

st.sidebar.write("""
The model predicts whether the penguin
belongs to:
- Adelie
- Chinstrap
- Gentoo
""")

st.sidebar.markdown("## 📌 Note")

st.sidebar.warning("""
Prediction accuracy depends on the
quality and range of input values.
""")

# Load model files
model = pickle.load(open("penguin_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

feature_columns = [
    'culmen_length_mm',
    'culmen_depth_mm',
    'flipper_length_mm',
    'body_mass_g',
    'island_Dream',
    'island_Torgersen',
    'sex_MALE'
]


st.markdown("## 📝 Enter Penguin Details")

c1, c2 = st.columns(2)

with c1:
    culmen_length = st.number_input("Culmen Length (mm)", value=40.0)
    culmen_depth = st.number_input("Culmen Depth (mm)", value=18.0)
    flipper_length = st.number_input("Flipper Length (mm)", value=200.0)

with c2:
    body_mass = st.number_input("Body Mass (g)", value=4000.0)
    island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
    sex = st.selectbox("Sex", ["MALE", "FEMALE"])
if st.button("🔍 Predict Species"):

    input_data = pd.DataFrame({
        'culmen_length_mm': [culmen_length],
        'culmen_depth_mm': [culmen_depth],
        'flipper_length_mm': [flipper_length],
        'body_mass_g': [body_mass],
        'island_Dream': [1 if island == "Dream" else 0],
        'island_Torgersen': [1 if island == "Torgersen" else 0],
        'sex_MALE': [1 if sex == "MALE" else 0]
    })

    # Arrange columns
    input_data = input_data[feature_columns]

    # Scale input
    scaled_data = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(scaled_data)

    # Decode label
    predicted_species = label_encoder.inverse_transform(prediction)

    # Confidence
    confidence = model.predict_proba(scaled_data).max() * 100

    # YOUR STYLE
    st.success(f"Predicted Species: {predicted_species[0]} 🐧")

    st.progress(int(confidence))

    st.info(f"Confidence Score: {confidence:.2f}%")


st.divider()

st.markdown("## 🚀 Explore the Application")

n1, n2, n3 = st.columns(3)

with n1:
    st.page_link(
        "Penguin_Predictor.py",
        label="🏠 Home Page"
    )

with n2:
    st.page_link(
        "pages/1_📊_EDA.py",
        label="📊 Exploratory Data Analysis"
    )

with n3:
    st.page_link(
        "pages/2_📈_Visualization.py",
        label="📈 Interactive Visualizations"
    )