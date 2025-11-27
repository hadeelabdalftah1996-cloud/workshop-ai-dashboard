import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# ------------------------  PAGE STYLE  ------------------------
st.set_page_config(page_title="SEPCO AI Dashboard", page_icon="🤖", layout="wide")

# Load logo
try:
    logo = Image.open("logo.jpg")
    st.image(logo, width=140)
except:
    st.warning("⚠️ لم يتم العثور على شعار الشركة (logo.jpg) – تأكدي أنه موجود في نفس مجلد المشروع.")

# Title
st.markdown(
    "<h1 style='text-align:center; color:#1F2937;'>SEPCO AI Workshop Dashboard 🤖</h1>",
    unsafe_allow_html=True,
)

st.markdown("---")

# ------------------------  LOAD DATA  ------------------------
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
   # <<< ضعي رابط الشيت هنا
df = pd.read_csv(sheet_url)

# ------------------------  EMOJI MAPPING  ------------------------
ai_mapping = {
    "معرفة بسيطة": "Basic 🟢",
    "معرفة متوسطة": "Intermediate 🟡",
    "معرفة متقدمة": "Advanced 🔵",
}

project_mapping = {
    "كتابة وتحديث إجراءات التشغيل SOP": "📝 Writing & Updating SOP",
    "تحليل وبناء FMEA": "📊 FMEA Analysis & Building",
    "تحليل الأعطال والتوقفات القسرية": "⚡ Fault & Forced-Outage Analysis",
    "مساعد للمشغل والمهندس": "🤖 Ops & Maintenance Copilot",
    "التحكم بالوصول إلى مراكز البيانات": "🔐 Access Control to Data Centers",
    "تخطيط المشتريات": "📦 Procurement Planning",
}

# Apply mapping
df["AILevel_EN"] = df["AILevel"].map(ai_mapping)
df["Project_EN"] = df["ProjectChoice"].map(project_mapping)

# ------------------------  SECTION: AI Level  ------------------------
st.markdown("## 🤖 مستوى المعرفة بالذكاء الاصطناعي")

if df["AILevel_EN"].notna().any():

    # Count values
    ai_counts = df["AILevel_EN"].value_counts()
    ai_df = ai_counts.reset_index()
    ai_df.columns = ["AI Level", "Count"]

    # Pie Chart
    fig_ai = px.pie(
        ai_df,
        names="AI Level",
        values="Count",
        title="AI Knowledge Levels",
        hole=0.45,
        color_discrete_sequence=["#2ecc71", "#f1c40f", "#3498db"]
    )
    fig_ai.update_traces(textinfo="percent+label")

    st.plotly_chart(fig_ai, use_container_width=True)

    # Show answers as text
    st.markdown("### 📋 جميع الإجابات:")
    for val, count in ai_counts.items():
        st.markdown(f"- **{val}** → ({count})")

else:
    st.info("لا توجد بيانات لهذا السؤال.")

st.markdown("---")

# ------------------------  SECTION: Project Choice  ------------------------
st.markdown("## 📌 المشاريع المختارة")

if df["Project_EN"].notna().any():

    # Count values
    proj_counts = df["Project_EN"].value_counts()
    proj_df = proj_counts.reset_index()
    proj_df.columns = ["Project", "Count"]

    # Pie Chart
    fig_proj = px.pie(
        proj_df,
        names="Project",
        values="Count",
        title="Selected Projects Distribution",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_proj.update_traces(textinfo="percent+label")

    st.plotly_chart(fig_proj, use_container_width=True)

    # Show answers as text
    st.markdown("### 📋 جميع الإجابات:")
    for val, count in proj_counts.items():
        st.markdown(f"- **{val}** → ({count})")

else:
    st.info("لا توجد بيانات لهذا السؤال.")

st.markdown("---")

st.markdown(
    "<p style='text-align:center; color:#6B7280;'>Dashboard by SEPCO © 2025</p>",
    unsafe_allow_html=True,
)







