import streamlit as st
import pandas as pd
import plotly.express as px

# --- عنوان الصفحة وشعار الشركة ---
st.set_page_config(page_title="SEPCO AI Workshop", page_icon="🤖", layout="wide")
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>🤖 SEPCO AI Workshop Dashboard</h1>", unsafe_allow_html=True)
st.image("logo.jpg", width=200)  # الشعار موجود بنفس مجلد المشروع على GitHub

# --- جلب البيانات من Google Sheet ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(url)

# --- Mapping للـ AI Level مع الإيموجي ---
mapping_ai = {
    "Basic": "Basic → 🟢",
    "Intermediate": "Intermediate → 🟡",
    "Advanced": "Advanced → 🔵"
}
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

# --- Mapping للمشاريع مع الإيموجي ---
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل SOP": "📝 كتابة وتحديث SOP",
    "تحليل وبناء ال FMEA": "📊 تحليل وبناء FMEA",
    "تحليل الأعطال والتوقفات القسرية": "⚡ تحليل الأعطال والتوقفات",
    "مساعد للمشغل والمهندس": "🤖 مساعد للمشغل والمهندس",
    "Access control to data centers": "🔐 Access control",
    "Procurement planning": "📦 Procurement planning"
}
df["ProjectChoice_EMOJI"] = df["ProjectChoice"].map(project_mapping)

# --- عرض جدول الإجابات ---
st.subheader("📋 Responses Table")
st.dataframe(df)

# --- شارت AI Levels ---
st.subheader("AI Knowledge Levels")
fig_ai = px.pie(df, names='AI_Level_EN', 
                title="Distribution of AI Knowledge Levels",
                color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig_ai, use_container_width=True)

# --- شارت المشاريع ---
st.subheader("Selected Projects")
fig_proj = px.pie(df, names='ProjectChoice_EMOJI', 
                  title="Most Chosen Projects",
                  color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig_proj, use_container_width=True)

# --- عرض المشروع الأكثر اختيارًا ---
if not df.empty:
    most_chosen = df['ProjectChoice_EMOJI'].value_counts().idxmax()
    st.markdown(f"🏆 **Most Chosen Project:** {most_chosen}")
else:
    st.markdown("No data available yet.")
