# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SEPCO AI Workshop Dashboard", layout="wide")

# ---- Header with logo ----
st.markdown(
    """
    <div style="display:flex; align-items:center; margin-bottom:30px;">
        <img src="logo.jpg" width="80" style="margin-right:20px;">
        <h1 style="color:#2E86C1;">SEPCO AI Workshop Dashboard 🤖</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- Data Import ----
DATA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(DATA_URL)

# Fill empty values to avoid errors
df['AILevel'] = df['AILevel'].fillna("Unknown")
df['ProjectChoice'] = df['ProjectChoice'].fillna("Unknown")

# ---- Mapping AI levels to English + Emoji ----
mapping_ai = {
    "معرفة بسيطة": "Basic 🟢",
    "معرفة متوسطة": "Intermediate 🟡",
    "معرفة متقدمة": "Advanced 🔵",
    "Unknown": "Unknown ⚪"
}
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

# ---- Mapping Projects to English + Emoji ----
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل sop": "Writing & updating SOP 📝",
    "تحليل وبناء ال FMEA": "FMEA Analysis 📊",
    "تحليل الاعطال والتوقفات القسرية": "Faults & Downtime ⚡",
    "مساعد للمشغل والمهندس": "Ops & Maintenance Copilot 🤖",
    "التحكم بالوصول الى مراكز البيانات": "Access Control 🔐",
    "تخطيط المشتريات": "Procurement Planning 📦",
    "Unknown": "Unknown ❌"
}
df["ProjectChoice_EN"] = df["ProjectChoice"].map(project_mapping)

# ---- Display AI Level Responses ----
st.markdown("## AI Knowledge Levels")
ai_counts = df['AI_Level_EN'].value_counts().reset_index()
ai_counts.columns = ['AI_Level_EN', 'Count']

fig_ai = px.pie(
    ai_counts,
    names='AI_Level_EN',
    values='Count',
    color='AI_Level_EN',
    color_discrete_sequence=['#2ca02c','#ff7f0e','#1f77b4','#7f7f7f'],
    title='Distribution of AI Knowledge Levels',
    hole=0.3
)
fig_ai.update_traces(textinfo='percent+label', textfont_size=16)  # show percentage + label
st.plotly_chart(fig_ai, use_container_width=True)

st.table(ai_counts.style.set_properties(**{'font-size':'16px'}))

# ---- Display Project Choice Responses ----
st.markdown("## Chosen Projects")
proj_counts = df['ProjectChoice_EN'].value_counts().reset_index()
proj_counts.columns = ['Project', 'Count']

fig_proj = px.pie(
    proj_counts,
    names='Project',
    values='Count',
    title='Most Chosen Projects',
    color_discrete_sequence=px.colors.qualitative.Set3,
    hole=0.3
)
fig_proj.update_traces(textinfo='percent+label', textfont_size=16)  # show percentage + label
st.plotly_chart(fig_proj, use_container_width=True)

st.table(proj_counts.style.set_properties(**{'font-size':'16px'}))




