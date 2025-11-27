# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(page_title="SEPCO AI Workshop", layout="wide")

# --- Header with logo ---
st.markdown(
    """
    <div style="display:flex; align-items:center;">
        <img src="logo.jpg" width="80" style="margin-right:20px;">
        <h1 style="color:#2E86C1;">🤖 SEPCO AI Workshop Dashboard</h1>
    </div>
    """, unsafe_allow_html=True
)

# --- Google Sheet CSV Link ---
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(sheet_url)

# --- Mapping AI Levels to Emojis ---
mapping_ai = {
    "معرفة بسيطة": "Basic → 🟢",
    "معرفة متوسطة": "Intermediate → 🟡",
    "معرفة متقدمة": "Advanced → 🔵"
}
df['AI_Level_EN'] = df['AILevel'].map(mapping_ai)

# --- Display AI Level Table ---
st.subheader("AI Knowledge Level Responses")
if not df.empty:
    st.dataframe(df[['AILevel', 'AI_Level_EN']])
else:
    st.warning("No AI Level data available.")

# --- Projects Mapping with Emojis ---
project_mapping = {
    "كتابة وتحديث SOP": "📝 كتابة وتحديث SOP",
    "تحليل وبناء FMEA": "📊 تحليل وبناء FMEA",
    "تحليل الأعطال والتوقفات": "⚡ تحليل الأعطال والتوقفات",
    "مساعد للمشغل والمهندس": "🤖 مساعد للمشغل والمهندس",
    "التحكم بالوصول الى مراكز البيانات ": "🔐 Access control to data centers",
    "تخطيط المشتريات": "📦 Procurement planning"
}

# --- Projects Pie Chart ---
st.subheader("Project Preference")
df['ProjectChoice_EN'] = df['ProjectChoice'].map(project_mapping)
df_proj_clean = df.dropna(subset=['ProjectChoice_EN'])

if not df_proj_clean.empty:
    fig_proj = px.pie(
        df_proj_clean,
        names='ProjectChoice_EN',
        values=df_proj_clean['ProjectChoice_EN'].value_counts(),
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_proj.update_traces(textinfo='label+percent', textfont_size=16)
    st.plotly_chart(fig_proj, use_container_width=True)
else:
    st.warning("No valid project data to display.")

# --- AI Level Pie Chart ---
st.subheader("AI Knowledge Distribution")
df_ai_clean = df.dropna(subset=['AI_Level_EN'])
if not df_ai_clean.empty:
    fig_ai = px.pie(
        df_ai_clean,
        names='AI_Level_EN',
        values=df_ai_clean['AI_Level_EN'].value_counts(),
        color_discrete_sequence=['#2ECC71', '#F1C40F', '#3498DB']
    )
    fig_ai.update_traces(textinfo='label+percent', textfont_size=16)
    st.plotly_chart(fig_ai, use_container_width=True)
else:
    st.warning("No AI Level data to display.")

# --- Most Common AI Level ---
if not df_ai_clean.empty:
    most_common_ai = df_ai_clean['AI_Level_EN'].mode()[0]
    st.markdown(f"**Most common AI knowledge level:** {most_common_ai}")
else:
    st.warning("Cannot calculate most common AI level.")


