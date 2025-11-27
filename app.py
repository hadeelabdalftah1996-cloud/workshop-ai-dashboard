import streamlit as st
import pandas as pd
import plotly.express as px

# --- إعداد الصفحة ---
st.set_page_config(page_title="SEPCO AI Workshop Dashboard", layout="wide")

# --- اسم الشركة وشعارها ---
st.image("logo.jpg", width=150)  # ضع اسم ملف الشعار بالضبط كما على GitHub
st.title("Welcome to SEPCO AI Workshop 🚀")

# --- رابط البيانات ---
DATA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

# --- قراءة البيانات ---
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data(DATA_URL)

# --- عرض البيانات إذا موجودة ---
if not df.empty:
    st.subheader("📊 Responses Table")
    st.dataframe(df)

    # --- Mapping AI Level to English labels (optional) ---
    mapping_ai = {
        "بسيطة": "Basic",
        "متوسطة": "Intermediate",
        "متقدمة": "Advanced"
    }

    if "AILevel" in df.columns:
        df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)
        st.write(f"Most common AI Level: {df['AI_Level_EN'].mode()[0]}")

    # --- Charts ---
    if "AILevel" in df.columns:
        fig1 = px.pie(df, names="AILevel", title="Knowledge Level of AI 🤖", color_discrete_sequence=px.colors.sequential.Tealrose)
        st.plotly_chart(fig1, use_container_width=True)

    if "ProjectChoice" in df.columns:
        fig2 = px.pie(df, names="ProjectChoice", title="Most Preferred Project 📌", color_discrete_sequence=px.colors.sequential.Viridis)
        st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("No data available yet. Please fill the Google Form responses first!")




