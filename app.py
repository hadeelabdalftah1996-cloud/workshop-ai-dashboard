import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- إعداد الصفحة (لازم أول شي) ----------
st.set_page_config(
    page_title="SEPCO Workshop AI Dashboard",
    page_icon="🤖",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #eef2f3 0%, #dfe9f3 100%);
}
h1 {
    font-size: 42px !important;
    font-weight: 800 !important;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ---------- شعار (اختياري – بدون كسر) ----------
try:
    st.image("logo.jpg", width=140)
except:
    pass

st.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>🤖 SEPCO Workshop AI Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# ---------- رابط Google Sheet (CSV) ----------
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

df = pd.read_csv(sheet_url)

# ---------- تأكيد الأعمدة ----------
required_cols = ["AILevel", "ProjectChoice"]
for col in required_cols:
    if col not in df.columns:
        st.error(f"❌ العمود مفقود في الشيت: {col}")
        st.stop()

# ---------- Mapping AI ----------
mapping_ai = {
    "معرفة بسيطة": "Basic 🟢",
    "معرفة متوسطة": "Intermediate 🟡",
    "معرفة متقدمة": "Advanced 🔵"
}
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai).fillna("Unknown")

# ---------- Mapping Projects ----------
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل SOP": "Writing & Updating SOP 📝",
    "تحليل وبناء FMEA": "FMEA Analysis 📊",
    "تحليل الأعطال والتوقفات القسرية": "Failure & Downtime Analysis ⚡",
    "مساعد للمشغل والمهندس – Ops & Maintenance Copilot": "Ops & Maintenance Copilot 🤖",
    "التحكم بالوصول إلى مراكز البيانات": "Access Control 🔐",
    "تخطيط المشتريات": "Procurement Planning 📦"
}
df["Project_EN"] = df["ProjectChoice"].map(project_mapping).fillna("Other")

# ---------- Sidebar ----------
st.sidebar.header("📌 Summary")
st.sidebar.metric("Total Responses", len(df))

# ---------- AI Level Pie ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
fig_ai = px.pie(
    df,
    names="AI_Level_EN",
    title="AI Knowledge Level Distribution",
    hole=0.4
)
st.plotly_chart(fig_ai, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- Project Pie ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
project_counts = df["Project_EN"].value_counts()
fig_proj = px.pie(
    names=project_counts.index,
    values=project_counts.values,
    title="Project Preference Distribution",
    hole=0.4
)
st.plotly_chart(fig_proj, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- Table ----------
st.markdown("### 📄 Detailed Responses")
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.dataframe(
    df[["AILevel", "AI_Level_EN", "ProjectChoice", "Project_EN"]],
    use_container_width=True
)
st.markdown("</div>", unsafe_allow_html=True)



















