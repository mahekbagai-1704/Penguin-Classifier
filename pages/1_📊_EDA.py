import streamlit as st
import pandas as pd

st.set_page_config(page_title="EDA", page_icon="📊", layout="wide")

df = pd.read_csv("cleaned_penguins.csv")

st.markdown("""
<h1 style='color:#6C4CF1;'>📊 Exploratory Data Analysis</h1>
<p style='font-size:20px;color:gray;'>
Understand your dataset through statistics and data exploration.
</p>
""", unsafe_allow_html=True)


st.sidebar.markdown("## 📊 EDA Information")

st.sidebar.info("""
Exploratory Data Analysis helps understand
patterns, distributions, and relationships
inside the penguin dataset.
""")

st.sidebar.markdown("## 📁 Dataset Details")

st.sidebar.write("""
• Palmer Penguins Dataset  
• 3 Penguin Species  
• Cleaned & Preprocessed Data  
""")

st.sidebar.markdown("## 🔍 Analysis Performed")

st.sidebar.write("""
• Species Distribution  
• Feature Comparison  
• Missing Value Handling  
• Correlation Analysis  
• Data Visualization  
""")


c1, c2, c3= st.columns(3)

with c1:
    st.metric("Rows", df.shape[0])

with c2:
    st.metric("Columns", df.shape[1])

with c3:
    st.metric("Missing Values", df.isnull().sum().sum())

# with c4:
#     st.metric("Duplicate Rows", df.duplicated().sum())

tab1, tab2, tab3 = st.tabs(["📋 Data Preview", "📈 Statistics", "📌 Data Types"])

with tab1:
    rows = st.slider(
    "Select Number of Rows",
    min_value=5,
    max_value=50,
    value=10
)

st.dataframe(
    df.head(rows),
    use_container_width=True
)

with tab2:
    st.dataframe(df.describe())

with tab3:
    st.write(df.dtypes)


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
        "pages/2_📈_Visualization.py",
        label="📈 Interactive Visualizations"
    )

with n3:
    st.page_link(
        "pages/3_🔍_Prediction.py",
        label="🔍 Predict Penguin Species"
    )