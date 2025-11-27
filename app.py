import streamlit as st
import pandas as pd
import plotly.express as px

# --- رابط البيانات (CSV منشور من جوجل شيت)
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(url)

# --- Mapping AI Level مع الإيموجي
mapping_ai = {
    "معرفة بسيطة": "Basic 🟢",
    "معرفة متوسطة": "Intermediate 🟡",
    "معرفة متقدمة": "Advanced 🔵"
}
df['AI_Level_EN'] = df['AILevel'].map(mapping_ai)

# --- Mapping المشاريع مع الإيموجي
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل sop": "Writing & updating SOP 📝",
    "تحليل وبناء ال FMEA": "FMEA Analysis 📊",
    "تحليل الاعطال والتوقفات القسرية": "Faults & Downtime ⚡",
    "مساعد للمشغل والمهندس": "Ops & Maintenance Copilot 🤖",
    "التحكم بالوصول الى مراكز البيانات": "Access Control 🔐",
    "تخطيط المشتريات": "Procurement Planning 📦"
}
df['ProjectChoice_EN'] = df['ProjectChoice'].map(project_mapping).fillna(df['ProjectChoice'])

# --- عنوان الصفحة وشعار الشركة
st.set_page_config(page_title="SEPCO AI Workshop Dashboard", page_icon="🤖", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2F4F4F;'>SEPCO AI Workshop 🤖</h1>", unsafe_allow_html=True)

# --- جدول البيانات
st.subheader("Responses Table")
st.dataframe(df)

# --- شارت مستوى AI
st.subheader("AI Knowledge Level Distribution")
fig_ai = px.pie(
    df.groupby('AI_Level_EN').size().reset_index(name='Count'),
    names='AI_Level_EN',
    values='Count',
    color_discrete_sequence=['#2ca02c','#ff7f0e','#1f77b4'],
    hole=0.3
)
fig_ai.update_traces(textinfo='percent+label', textfont_size=16)
st.plotly_chart(fig_ai, use_container_width=True)

# --- شارت المشاريع
st.subheader("Project Preferences Distribution")
proj_counts = df.groupby('ProjectChoice_EN').size().reset_index(name='Count')
fig_proj = px.pie(
    proj_counts,
    names='ProjectChoice_EN',
    values='Count',
    color_discrete_sequence=px.colors.qualitative.Set3,
    hole=0.3
)
fig_proj.update_traces(textinfo='percent+label', textfont_size=16)
st.plotly_chart(fig_proj, use_container_width=True)





