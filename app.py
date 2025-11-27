import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# إعداد الصفحة والواجهة
# -------------------------
st.set_page_config(page_title="Workshop AI Dashboard", layout="wide")
st.title("AI Workshop Dashboard")

# عرض شعار الشركة
st.image("https://raw.githubusercontent.com/USERNAME/REPO/main/logo.png", width=200)

st.markdown("### تحليل إجابات المشاركين على الفورم")

# -------------------------
# جلب البيانات من Google Sheets (CSV link)
# -------------------------
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(sheet_url)

# التأكد من الأعمدة وتسميتها
df.rename(columns={
    "AILevel": "AILevel",
    "ProjectChoice": "ProjectChoice"
}, inplace=True)

# -------------------------
# تحويل مستويات AI للإنجليزية للعرض
# -------------------------
mapping_ai = {
    "بسيطة": "Basic",
    "متوسطة": "Intermediate",
    "متقدمة": "Advanced"
}
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

# -------------------------
# ترتيب المشاريع للعرض
# -------------------------
project_names_en = {
    "كتابة وتحديث إجراءات التشغيل sop": "SOP Writing & Update",
    "تحليل وبناء ال FMEA": "FMEA Analysis & Build",
    "تحليل الاعطال والتوقفات القسرية": "Failure & Downtime Analysis",
    "مساعد للمشغل والمهندس ops & maintaenance copilot": "Ops & Maintenance Copilot",
    "Access control to data centers": "Access Control to Data Centers",
    "Procurement planning": "Procurement Planning"
}

df["ProjectChoice_EN"] = df["ProjectChoice"].map(project_names_en)

# -------------------------
# عرض جدول البيانات
# -------------------------
st.subheader("جدول الإجابات")
st.dataframe(df[["AILevel", "AI_Level_EN", "ProjectChoice", "ProjectChoice_EN"]])

# -------------------------
# شارت دائري لمستوى معرفة AI
# -------------------------
st.subheader("نسبة المشاركين حسب مستوى المعرفة بالذكاء الاصطناعي")
fig_ai = px.pie(df, names="AI_Level_EN", title="AI Knowledge Level Distribution",
                color="AI_Level_EN", color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig_ai, use_container_width=True)

# -------------------------
# شارت دائري لاختيار المشروع
# -------------------------
st.subheader("نسبة المشاركين حسب المشروع الذي يرغبون بتطبيقه")
fig_proj = px.pie(df, names="ProjectChoice_EN", title="Project Choice Distribution",
                  color="ProjectChoice_EN", color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig_proj, use_container_width=True)

# -------------------------
# إحصائيات سريعة
# -------------------------
st.subheader("إحصائيات سريعة")
st.write(f"أكثر مستوى AI شيوعاً: {df['AI_Level_EN'].mode()[0] if not df.empty else 'No data'}")
st.write(f"أكثر مشروع اختياراً: {df['ProjectChoice_EN'].mode()[0] if not df.empty else 'No data'}")
st.write(f"عدد الإجابات: {len(df)}")



