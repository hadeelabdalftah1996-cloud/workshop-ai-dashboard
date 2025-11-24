import streamlit as st
import pandas as pd
import altair as alt

# ---------------------------
# Load Google Sheet
# ---------------------------
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(sheet_url)

st.title("🔍 AI Workshop Feedback Dashboard")

# -----------------------------------------------------
# Convert Arabic answers → English labels for charts only
# -----------------------------------------------------
mapping_ai = {
    "بسيطة": "Basic",
    "متوسطة": "Intermediate",
    "متقدمة": "Advanced"
}

mapping_project = {
    "التنبؤ بالأعطال والصيانة التنبؤية للمحطات والمعدات": "Predictive Maintenance",
    "كشف ارتداء معدات السلامة الشخصية تلقائياً": "PPE Detection",
    "التنبؤ بالاحتياجات من المياه": "Water Demand Forecasting"
}

df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)
df["Project_EN"] = df["ProjectChoice"].map(mapping_project)

# --------------------------
# Show raw Google Sheet data
# --------------------------
st.subheader("📄 All Form Responses")
st.dataframe(df)

# --------------------------
# AI Level Bar Chart
# --------------------------
st.subheader("📊 AI Knowledge Level Distribution")

ai_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("AI_Level_EN:N", title="AI Knowledge Level"),
        y=alt.Y("count():Q", title="Number of Participants"),
        color="AI_Level_EN:N"
    )
    .properties(height=400)
)

st.altair_chart(ai_chart, use_container_width=True)

# --------------------------
# Project Choice Pie Chart
# --------------------------
st.subheader("📈 Project Choice Distribution")

project_chart = (
    alt.Chart(df)
    .mark_arc()
    .encode(
        theta="count():Q",
        color="Project_EN:N",
        tooltip=["Project_EN", "count()"]
    )
    .properties(height=400)
)

st.altair_chart(project_chart, use_container_width=True)

# --------------------------
# Footer
# --------------------------
st.info("💡 Data updates automatically when new Google Form responses arrive.")




