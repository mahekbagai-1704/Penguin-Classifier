import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Visualizations", page_icon="📈", layout="wide")

df = pd.read_csv("cleaned_penguins.csv")

st.markdown("""
<h1 style='color:#6C4CF1;'>📈 Data Visualizations</h1>
""", unsafe_allow_html=True)

st.caption("Explore species patterns and feature relationships")


st.sidebar.markdown("## 📊 Visualization Info")

st.sidebar.info("""
Explore different plots related to the penguin dataset.

Available Visualizations:
• Scatter Plot
• Pie Chart
• Box Plot
• Histogram
• Bar Chart
• Violin Plot
""")

st.sidebar.markdown("## 🎯 Purpose")

st.sidebar.write("""
These visualizations help analyze:
- Species distribution
- Feature relationships
- Data patterns
- Variations and correlations
""")

st.sidebar.markdown("## 🧠 ML Features")

st.sidebar.write("""
• Culmen Length  
• Culmen Depth  
• Flipper Length  
• Body Mass  
• Island  
• Sex  
""")

graph = st.selectbox(
    "Select Plot Type",
    [
        "Scatter Plot",
        "Histogram",
        "Box Plot",
        "Violin Plot",
        "Bar Plot",
        "Pie Chart"
    ]
)

if graph == "Scatter Plot":
    fig = px.scatter(df, x="culmen_length_mm", y="culmen_depth_mm", color="species")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### 📘 Plot Information")
    st.info("""
📌 Scatter Plot shows relationship between flipper length and body mass.

Features Used:
• Flipper Length
• Body Mass

Purpose:
• Observe correlation between features
• Identify species clusters
""")
    
elif graph == "Histogram":
    fig = px.histogram(df, x="body_mass_g", color="species")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### 📘 Plot Information")
    st.info("""
📌 Histogram shows the distribution of penguin body mass values.

Features Used:
• Body Mass
• Species

Purpose:
• Understand data distribution
• Observe frequency of body mass values
• Compare species density
""")
    
elif graph == "Box Plot":
    fig = px.box(df, x="species", y="body_mass_g", color="species")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### 📘 Plot Information")
    st.info("""
📌 Box Plot compares penguin species with body mass distribution.

Features Used:
• Species
• Body Mass

Purpose:
• Detect spread and variation
• Compare average body mass
• Identify outliers
""")
    
elif graph == "Violin Plot":
    fig = px.violin(df, x="species", y="flipper_length_mm", color="species")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### 📘 Plot Information")
    st.info("""
📌 Violin Plot shows the distribution and density of flipper length among penguin species.

Features Used:
• Species
• Flipper Length

Purpose:
• Compare feature distribution
• Observe density patterns
• Detect spread and variation
""")
    
elif graph == "Bar Plot":
    fig = px.bar(df, x="species", color="species")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### 📘 Plot Information")
    st.info("""
📌 Bar Chart compares the number of penguins in each species category.

Features Used:
• Species Count

Purpose:
• Compare species frequency
• Understand dataset composition
• Visualize categorical distribution
""")
    
elif graph == "Pie Chart":
    fig = px.pie(df, names="species")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### 📘 Plot Information")
    st.info("""
📌 Pie Chart shows the distribution of penguin species in the dataset.

Feature Used:
• Species Count

Purpose:
• Understand dataset balance
• Compare species proportions
""")
    
    
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
        "pages/3_🔍_Prediction.py",
        label="🔍 Predict Penguin Species"
    )    