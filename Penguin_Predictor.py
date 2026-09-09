import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title="Penguin Species Classifier",
    page_icon="🐧",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f7f5ff;
}
.block-container {
    padding-top: 2rem;
}
.stButton>button {
    width: 100%;
    border-radius: 14px;
    height: 3em;
    background: linear-gradient(90deg,#7F5AF0,#9B6DFF);
    color: white;
    border: none;
    font-size: 16px;
    font-weight: bold;
}
.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)



with st.sidebar:
   st.sidebar.markdown("### 📌 About Project")
   st.sidebar.info(
    """
    This machine learning application predicts penguin species 
    using physical characteristics such as:

    • Culmen Length  
    • Culmen Depth  
    • Flipper Length  
    • Body Mass  
    • Island  
    • Sex
    """
)

#    st.sidebar.markdown("### 🤖 Model Used")
#    st.sidebar.success("Logistic Regression")

#    st.sidebar.markdown("### 📊 Dataset")
#    st.sidebar.write("Palmer Penguins Dataset")

   st.sidebar.markdown("### 🎯 Purpose")
   st.sidebar.write(
    "To classify penguin species using supervised machine learning."
)
# st.divider()
# st.success("Model Accuracy: 97%")

col1, col2 = st.columns([1,3])

with col1:
    st.image("https://i.pinimg.com/originals/db/c4/f9/dbc4f965cb92e4c5706053314ea2d861.jpg", width=220)

with col2:
    st.markdown("""
    <h1 style='font-size:65px; margin-bottom:0px;'>
    <span style='color:#6C4CF1;'>Penguin</span>
    Species Classifier 🐧
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:28px; color:gray; margin-top:-10px;'>
    Machine Learning Based Penguin Classification System
    </p>
    """, unsafe_allow_html=True)

st.markdown("## 📌 Model Details")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='metric-card'>
    <h3>🏆 Accuracy</h3>
    <h1 style='color:#6C4CF1;'>97%</h1>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-card'>
    <h3>🧠 Algorithm</h3>
    <h2>Logistic Regression</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-card'>
    <h3>⚙️ Type</h3>
    <h2>Classification</h2>
    </div>
    """, unsafe_allow_html=True)

st.success("The model achieved high classification accuracy on the penguin dataset.")

df = pd.read_csv("cleaned_penguins.csv")

st.markdown("## 📋 Dataset Preview")
st.dataframe(df.head())



st.markdown("## 🚀 Explore the Application")


n1, n2, n3 = st.columns(3)

with n1:
    st.page_link("pages/1_📊_EDA.py", label="📊 Exploratory Data Analysis")

with n2:
    st.page_link("pages/2_📈_Visualization.py", label="📈 Interactive Visualizations")

with n3:
    st.page_link("pages/3_🔍_Prediction.py", label="🔍 Predict Penguin Species")
