import streamlit as st
import pandas as pd
import plotly.express as px

# --- Header ---
st.set_page_config(page_title="SEPCO AI Workshop Dashboard", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1F77B4;'>🤖 SEPCO AI Workshop Responses</h1>", unsafe_allow_html=True)
st.image("logo.jpg", width=200)

# --- Load data from Google Sheet CSV link ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(url)

# --- Map AI Levels to English + Emoji ---
mapping_ai = {
    "معرفة بسيطة": "Basic 🟢",
    "معرفة متوسطة": "Intermediate 🟡",
    "معرفة متقدمة": "Advanced 🔵"
}
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

# --- Projects mapping with Emoji ---
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل sop": "📝 كتابة وتحديث SOP",
    "تحليل وبناء ال FMEA": "📊 تحليل وبناء FMEA",
    "تحليل الاعطال والتوقفات القسرية": "⚡ تحليل الأعطال والتوقفات",
    "مساعد للمشغل والمهندس": "🤖 مساعد للمشغل والمهندس",
    "Access control to data centers": "🔐 Access control",
    "Procurement planning": "📦 Procurement planning"
}
df["ProjectChoice_EN"] = df["ProjectChoice"].map(project_mapping)

# --- Display Data Table ---
st.subheader("Responses Table")
st.dataframe(df[["AI_Level_EN", "ProjectChoice_EN"]])

# --- AI Level Pie Chart ---
st.subheader("AI Knowledge Levels")
fig_ai = px.pie(
    df,
    names='AI_Level_EN',
    values=df['AI_Level_EN'].value_counts(),
    color_discrete_sequence=px.colors.sequential.RdBu
)
fig_ai.update_traces(textinfo='label+percent', textfont_size=18)
st.plotly_chart(fig_ai, use_container_width=True)

# --- Projects Pie Chart ---
st.subheader("Project Preference")
fig_proj = px.pie(
    df,
    names='ProjectChoice_EN',
    values=df['ProjectChoice_EN'].value_counts(),
    color_discrete_sequence=px.colors.qualitative.Set3
)
fig_proj.update_traces(textinfo='label+percent', textfont_size=16)
st.plotly_chart(fig_proj, use_container_width=True)
