import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- إعداد الصفحة ----------
st.set_page_config(
    page_title="SEPCO Workshop AI Dashboard",
    page_icon="🤖",
    layout="wide"
)

# شعار الشركة واسمها
st.image("logo.jpg", width=150)  # تأكدي إن الصورة بنفس مجلد المشروع على GitHub
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>SEPCO Workshop AI Dashboard</h1>", unsafe_allow_html=True)
st.write("---")

# ---------- رابط الشيت ----------
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

# قراءة البيانات
df = pd.read_csv(sheet_url)

# ---------- Mapping لمستوى AI ----------
mapping_ai = {
    "معرفة بسيطة": "Basic 🟢",
    "معرفة متوسطة": "Intermediate 🟡",
    "معرفة متقدمة": "Advanced 🔵"
}
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

# ---------- Mapping المشاريع مع إيموجي ----------
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل SOP": "Writing & Updating SOP 📝",
    "تحليل وبناء ال FMEA ": "FMEA Analysis 📊",
    "تحليل الأعطال والتوقفات القسرية": "Failure & Downtime Analysis ⚡",
    "مساعد للمشغل والمهندس – Ops & Maintenance Copilot": "Ops & Maintenance Copilot 🤖",
    "التحكم بالوصول إلى مراكز البيانات": "Access Control 🔐",
    "تخطيط المشتريات": "Procurement Planning 📦"
}
df["Project_EN"] = df["ProjectChoice"].map(project_mapping)

# ---------- Sidebar Summary ----------
st.sidebar.header("Summary")
st.sidebar.write(f"Total Responses: {len(df)}")

# ---------- Pie Chart لمستوى AI ----------
if not df.empty:
    fig_ai = px.pie(
        df,
        names="AI_Level_EN",
        title="AI Knowledge Level Distribution",
        color_discrete_sequence=['#2ca02c','#ff7f0e','#1f77b4'],
        hole=0.4
    )
    fig_ai.update_traces(textposition='inside', textinfo='percent+label', pull=[0.05]*len(df["AI_Level_EN"].unique()))
    st.plotly_chart(fig_ai, use_container_width=True)
else:
    st.warning("No AILevel data available!")

# ---------- Pie Chart للمشاريع ----------
if not df.empty:
    project_counts = df['Project_EN'].value_counts()
    fig_proj = px.pie(
        names=project_counts.index,
        values=project_counts.values,
        title="Project Preference Distribution",
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4
    )
    fig_proj.update_traces(textposition='inside', textinfo='percent+label', pull=[0.05]*len(project_counts))
    st.plotly_chart(fig_proj, use_container_width=True)
else:
    st.warning("No ProjectChoice data available!")

# ---------- Table مع الإجابات ----------
st.write("### Detailed Responses")
if not df.empty:
    st.dataframe(df[["AILevel", "AI_Level_EN", "ProjectChoice", "Project_EN"]])
else:
    st.info("No responses yet.")











