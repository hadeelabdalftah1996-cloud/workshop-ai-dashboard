import streamlit as st
import pandas as pd
import altair as alt

# عنوان التطبيق
st.title("AI Workshop Dashboard")
st.markdown("عرض نتائج الاستبيان وتحليل البيانات باستخدام الذكاء الاصطناعي")

# رابط CSV من Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

# تحميل البيانات
df = pd.read_csv(sheet_url)

st.subheader("Raw Data")
st.dataframe(df)  # عرض الجدول الأولي

# Mapping لمستوى الذكاء الاصطناعي
mapping_ai = {
    "بسيط": "Basic",
    "متوسط": "Intermediate",
    "متقدم": "Advanced"
}

# التحقق من العمود AILevel
if 'AILevel' in df.columns:
    df['AI_Level_EN'] = df['AILevel'].map(mapping_ai)
else:
    st.warning("عمود AILevel غير موجود!")

# تحليل أكثر مشروع تم اختياره
if 'ProjectChoice' in df.columns:
    if df['ProjectChoice'].dropna().empty:
        most_chosen_project = "لا توجد بيانات كافية"
    else:
        most_chosen_project = df['ProjectChoice'].dropna().value_counts().idxmax()
    st.subheader("Most Chosen Project")
    st.write(f"**{most_chosen_project}**")
else:
    st.warning("عمود ProjectChoice غير موجود!")

# رسم شارت لمستوى الذكاء الاصطناعي
if 'AI_Level_EN' in df.columns:
    st.subheader("AI Knowledge Level Distribution")
    chart_ai = alt.Chart(df).mark_bar().encode(
        x=alt.X('AI_Level_EN', sort=None, title='AI Level'),
        y=alt.Y('count()', title='Number of Respondents'),
        color='AI_Level_EN'
    )
    st.altair_chart(chart_ai, use_container_width=True)

# رسم شارت لمشاريع الاستبيان
if 'ProjectChoice' in df.columns and not df['ProjectChoice'].dropna().empty:
    st.subheader("Project Choice Distribution")
    chart_proj = alt.Chart(df.dropna(subset=['ProjectChoice'])).mark_bar().encode(
        x=alt.X('ProjectChoice', sort=None, title='Project'),
        y=alt.Y('count()', title='Number of Respondents'),
        color='ProjectChoice'
    )
    st.altair_chart(chart_proj, use_container_width=True)







