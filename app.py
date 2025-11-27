import streamlit as st
import pandas as pd
import plotly.express as px

# ---- واجهة ----
st.set_page_config(page_title="SEPCO AI Workshop Dashboard", page_icon="🤖", layout="wide")

# شعار الشركة
st.image("logo.jpg", width=200)

# عنوان
st.markdown("## Welcome to SEPCO AI Workshop Dashboard 🤖📊")
st.markdown("### Real-time Responses Analysis")

# ---- رابط البيانات ----
data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

# ---- تحميل البيانات ----
df = pd.read_csv(data_url)

# ---- التأكد من الأعمدة ----
expected_cols = ["AILevel", "ProjectChoice"]
for col in expected_cols:
    if col not in df.columns:
        st.error(f"Column '{col}' is missing from the data!")
        st.stop()

# ---- تعيين ألوان للإيموجي ----
ai_mapping = {
    "Simple 😎": "Simple",
    "Intermediate 🤓": "Intermediate",
    "Advanced 🤖": "Advanced"
}

# تطبيق الترجمة للإنجليزية للشارت
df["AI_Level_EN"] = df["AILevel"].map(ai_mapping)

# ---- Project Names مع الإيموجي ----
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل sop 📝": "SOP Documentation 📝",
    "تحليل وبناء ال FMEA ⚙️": "FMEA Analysis ⚙️",
    "تحليل الاعطال والتوقفات القسرية 🔧": "Failure & Downtime Analysis 🔧",
    "مساعد للمشغل والمهندس ops & maintenance copilot 🤝": "Ops & Maintenance Copilot 🤝",
    "التحكم بالوصول لمراكز البيانات 🔐": "Access Control to Data Centers 🔐",
    "تخطيط المشتريات 📦": "Procurement Planning 📦"
}

df["Project_EN"] = df["ProjectChoice"].map(project_mapping)

# ---- جدول البيانات ----
st.markdown("### Raw Data Table")
st.dataframe(df)

# ---- شارت مستوى AI ----
st.markdown("### AI Knowledge Level Distribution")
fig_ai = px.pie(
    df,
    names="AI_Level_EN",
    title="Distribution of AI Knowledge Levels",
    color="AI_Level_EN",
    color_discrete_map={"Simple":"#636EFA", "Intermediate":"#EF553B", "Advanced":"#00CC96"}
)
st.plotly_chart(fig_ai, use_container_width=True)

# ---- شارت اختيار المشاريع ----
st.markdown("### Most Selected Project")
fig_proj = px.pie(
    df,
    names="Project_EN",
    title="Distribution of Selected Projects",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig_proj, use_container_width=True)

# ---- أبرز النتائج ----
st.markdown("### Key Insights")
if not df.empty:
    most_common_ai = df['AI_Level_EN'].mode()[0]
    most_chosen_project = df['Project_EN'].mode()[0]
    st.write(f"Most common AI Level: **{most_common_ai}**")
    st.write(f"Most chosen Project: **{most_chosen_project}**")
else:
    st.write("No data available yet.")





