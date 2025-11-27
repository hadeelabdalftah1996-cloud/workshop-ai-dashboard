import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------
# 1) تحميل البيانات من Google Sheet
# -------------------------------------------
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(sheet_url)

# -------------------------------------------
# 2) تأكيد أسماء الأعمدة كما في الشيت
# -------------------------------------------
AI_COL = "AILevel"
PROJECT_COL = "ProjectChoice"

# -------------------------------------------
# 3) تنسيقات الواجهة
# -------------------------------------------
st.set_page_config(page_title="AI Dashboard", page_icon="🤖", layout="wide")

st.markdown("""
    <h1 style='text-align:center; color:#4A90E2;'>📊 لوحة تحليل إجابات الذكاء الاصطناعي</h1>
    <p style='text-align:center;'>تحليل فوري لنتائج النموذج من Google Sheet</p>
""", unsafe_allow_html=True)

st.write("---")

# -------------------------------------------
# 4) عرض البيانات الخام
# -------------------------------------------
with st.expander("📄 عرض البيانات"):
    st.dataframe(df)

st.write("---")

# -------------------------------------------
# 5) إحصائيات أساسية
# -------------------------------------------
col1, col2 = st.columns(2)

with col1:
    most_ai = df[AI_COL].mode()[0] if not df.empty else "لا يوجد بيانات"
    st.metric("أكثر مستوى ذكاء مكرر", most_ai)

with col2:
    most_proj = df[PROJECT_COL].mode()[0] if not df.empty else "لا يوجد بيانات"
    st.metric("أكثر مشروع مختار", most_proj)

st.write("---")

# -------------------------------------------
# 6) الرسم الدائري Pie Chart (النسب)
# -------------------------------------------
st.markdown("## 🔵 نسبة اختيار المشاريع")

if df.empty:
    st.warning("لا يوجد بيانات لعرض الرسم البياني.")
else:
    proj_counts = df[PROJECT_COL].value_counts().reset_index()
    proj_counts.columns = ["Project", "Count"]

    fig = px.pie(
        proj_counts,
        names="Project",
        values="Count",
        title="نسبة اختيار كل مشروع",
        hole=0.35
    )
    st.plotly_chart(fig, use_container_width=True)

st.write("---")

# -------------------------------------------
# 7) الرسم الدائري لمستويات AI
# -------------------------------------------
st.markdown("## 🤖 توزيع مستوى الذكاء الاصطناعي")

if not df.empty:
    ai_counts = df[AI_COL].value_counts().reset_index()
    ai_counts.columns = ["AI_Level", "Count"]

    fig2 = px.pie(
        ai_counts,
        names="AI_Level",
        values="Count",
        title="نسبة تكرار مستويات الذكاء"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.write("---")

st.markdown("""
    <p style='text-align:center; color:gray; margin-top:20px;'>
        تم التطوير بواسطة ChatGPT 🧡
    </p>
""", unsafe_allow_html=True)


