import streamlit as st
import pandas as pd
import altair as alt

# رابط CSV من Google Sheets
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

# قراءة البيانات
df = pd.read_csv(csv_url)

st.title("AI Workshop Dashboard")

# mapping للذكاء الاصطناعي من عربي لانجليزي
mapping_ai = {
    "بسيطة": "Basic",
    "متوسطة": "Intermediate",
    "متقدمة": "Advanced"
}

# تحويل العمود
df["AI_Level_EN"] = df["AILevel"].map(mapping_ai)

st.subheader("Responses Table")
st.dataframe(df)

st.subheader("AI Level Distribution")
chart = alt.Chart(df).mark_bar(color="#4CAF50").encode(
    x=alt.X('AI_Level_EN', title='AI Level'),
    y=alt.Y('count()', title='Number of Respondents'),
    tooltip=['AI_Level_EN', 'count()']
).properties(width=600, height=400)

st.altair_chart(chart)

st.subheader("Most Chosen Project")
most_chosen = df['ProjectChoice'].value_counts().idxmax()
st.write(f"The most chosen project is: **{most_chosen}**")






