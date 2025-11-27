import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# إعداد الصفحة
# -------------------------
st.set_page_config(page_title="SEPCO AI Workshop Dashboard", layout="wide")

# شعار واسم الشركة
st.image("logo.jpg", width=120)
st.markdown("<h1 style='text-align:center;'>SEPCO AI Workshop Dashboard</h1>", unsafe_allow_html=True)

# -------------------------
# رابط الشيت من Google Forms
# -------------------------
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(sheet_url)

# -------------------------
# Mapping للمستويات مع الإيموجي
# -------------------------
mapping_ai = {
    "Basic": "Basic 🟢",
    "Intermediate": "Intermediate 🟡",
    "Advanced": "Advanced 🔵"
}

df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

# -------------------------
# Mapping المشاريع مع الإيموجي وألوان ثابتة
# -------------------------
project_mapping = {
    "كتابة وتحديث SOP": ("📝 كتابة وتحديث SOP", "#1f77b4"),
    "تحليل وبناء FMEA": ("📊 تحليل وبناء FMEA", "#ff7f0e"),
    "تحليل الأعطال والتوقفات": ("⚡ تحليل الأعطال والتوقفات", "#2ca02c"),
    "مساعد للمشغل والمهندس": ("🤖 مساعد للمشغل والمهندس", "#d62728"),
    "Access control": ("🔐 Access control", "#9467bd"),
    "Procurement planning": ("📦 Procurement planning", "#8c564b")
}

# تحويل ProjectChoice إلى النص مع الإيموجي
df["Project_Emoji"] = df["ProjectChoice"].map(lambda x: project_mapping.get(x, (x, "#cccccc"))[0])
df["Project_Color"] = df["ProjectChoice"].map(lambda x: project_mapping.get(x, (x, "#cccccc"))[1])

# -------------------------
# جدول الردود
# -------------------------
st.subheader("Responses Table")
st.dataframe(df[["AILevel", "AI_Level_EN", "ProjectChoice", "Project_Emoji"]])

# -------------------------
# شارت مستويات AI
# -------------------------
st.subheader("AI Knowledge Levels")
ai_count = df["AI_Level_EN"].value_counts().reset_index()
ai_count.columns = ["Level", "Count"]
fig_ai = px.pie(ai_count, names="Level", values="Count", color="Level",
                color_discrete_map={
                    "Basic 🟢": "#2ca02c",
                    "Intermediate 🟡": "#ff7f0e",
                    "Advanced 🔵": "#1f77b4"
                },
                title="Distribution of AI Knowledge Levels")
st.plotly_chart(fig_ai, use_container_width=True)

# -------------------------
# شارت المشاريع
# -------------------------
st.subheader("Projects Selection")
project_count = df.groupby(["Project_Emoji", "Project_Color"]).size().reset_index(name='Count')
fig_proj = px.pie(project_count, names="Project_Emoji", values="Count", color="Project_Emoji",
                  color_discrete_map={row["Project_Emoji"]: row["Project_Color"] for idx, row in project_count.iterrows()},
                  title="Distribution of Project Choices")
st.plotly_chart(fig_proj, use_container_width=True)

# -------------------------
# ملخص سريع
# -------------------------
if not df.empty:
    most_common_ai = df["AI_Level_EN"].mode()[0]
    most_common_project = df["Project_Emoji"].mode()[0]
else:
    most_common_ai = "No data"
    most_common_project = "No data"

st.markdown(f"**Most common AI Level:** {most_common_ai}")
st.markdown(f"**Most chosen Project:** {most_common_project}")







