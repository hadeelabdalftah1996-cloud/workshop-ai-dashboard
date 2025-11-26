import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="AI Workshop Dashboard", layout="wide")

# Google Sheet CSV
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

df = pd.read_csv(csv_url)

st.title("AI Workshop Dashboard")

# -----------------------------
# 1) عرض البيانات
# -----------------------------
st.subheader("Raw Data")
st.dataframe(df)

# -----------------------------
# 2) تحويل قيم AILevel إلى إنجليزي
# -----------------------------
mapping_ai = {
    "بسيطة": "Basic",
    "متوسطة": "Intermediate",
    "متقدمة": "Advanced"
}

# إذا القيم عربي → ترجم
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

# -----------------------------
# 3) شارت مستوى الذكاء الاصطناعي
# -----------------------------
st.subheader("AI Knowledge Level Distribution")

if df["AI_Level_EN"].notna().sum() > 0:
    ai_chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("AI_Level_EN:N", title="AI Knowledge Level"),
            y=alt.Y("count()", title="Number of Participants"),
            color="AI_Level_EN:N"
        )
        .properties(height=400)
    )
    st.altair_chart(ai_chart, use_container_width=True)
else:
    st.write("No AI Level data available.")

# -----------------------------
# 4) شارت اختيار المشروع
# -----------------------------
st.subheader("Most Selected Project")

if df["ProjectChoice"].notna().sum() > 0:
    project_chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("ProjectChoice:N", title="Project Type"),
            y=alt.Y("count()", title="Number of Votes"),
            color="ProjectChoice:N"
        )
        .properties(height=400)
    )
    st.altair_chart(project_chart, use_container_width=True)

    # إظهار الأكثر اختياراً
    st.write(f"Most chosen project: **{df['ProjectChoice'].mode()[0]}**")
else:
    st.write("No project choice data available.")

