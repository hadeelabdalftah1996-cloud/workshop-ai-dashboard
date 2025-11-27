import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# Header with logo & company name
# -------------------------
st.set_page_config(page_title="SEPCO AI Workshop Dashboard", layout="wide")
st.markdown(
    "<h1 style='text-align:center; color: #1f77b4;'>🤖 SEPCO AI Workshop Dashboard</h1>",
    unsafe_allow_html=True
)

# Logo
st.image("logo.jpg", width=200)

# -------------------------
# Google Sheets CSV Link
# -------------------------
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(csv_url)

# -------------------------
# Mapping AI Levels
# -------------------------
mapping_ai = {
    "معرفة بسيطة": "Basic 🟢",
    "معرفة متوسطة": "Intermediate 🟡",
    "معرفة متقدمة": "Advanced 🔵"
}
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

# -------------------------
# Mapping Projects
# -------------------------
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل sop": "📝 كتابة وتحديث SOP",
    "تحليل وبناء ال FMEA": "📊 تحليل وبناء FMEA",
    "تحليل الاعطال والتوقفات القسرية": "⚡ تحليل الأعطال والتوقفات",
    "مساعد للمشغل والمهندس": "🤖 مساعد للمشغل والمهندس",
    "Access control to data centers": "🔐 التحكم بالوصول الى مراكز البيانات",
    "Procurement planning": "📦 تخطيط المشتريات"
}
df["ProjectChoice_EN"] = df["ProjectChoice"].map(project_mapping)

# -------------------------
# AI Level Chart
# -------------------------
st.subheader("AI Knowledge Level")
df_ai_clean = df.dropna(subset=['AI_Level_EN'])
if not df_ai_clean.empty:
    fig_ai = px.pie(
        df_ai_clean,
        names='AI_Level_EN',
        color='AI_Level_EN',
        color_discrete_map={
            "Basic 🟢": "#77DD77",
            "Intermediate 🟡": "#FFD700",
            "Advanced 🔵": "#1f77b4"
        }
    )
    fig_ai.update_traces(textinfo='label+percent', textfont_size=16)
    st.plotly_chart(fig_ai, use_container_width=True)
else:
    st.warning("No AI level data available.")

# -------------------------
# Projects Chart
# -------------------------
st.subheader("Project Preferences")
df_proj_clean = df.dropna(subset=['ProjectChoice_EN'])
if not df_proj_clean.empty:
    fig_proj = px.pie(
        df_proj_clean,
        names='ProjectChoice_EN',
        color='ProjectChoice_EN',
        color_discrete_map={
            "📝 كتابة وتحديث SOP": "#FFB347",
            "📊 تحليل وبناء FMEA": "#FF6961",
            "⚡ تحليل الأعطال والتوقفات": "#77DD77",
            "🤖 مساعد للمشغل والمهندس": "#AEC6CF",
            "🔐 التحكم بالوصول الى مراكز البيانات": "#CBAACB",
            "📦 تخطيط المشتريات": "#FFD700"
        }
    )
    fig_proj.update_traces(textinfo='label+percent', textfont_size=16)
    st.plotly_chart(fig_proj, use_container_width=True)
else:
    st.warning("No project data available.")

# -------------------------
# Show Raw Data Table
# -------------------------
st.subheader("Responses Table")
st.dataframe(df, use_container_width=True)
