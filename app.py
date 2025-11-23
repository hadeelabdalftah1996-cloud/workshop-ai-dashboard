import streamlit as st
import pandas as pd

st.title("تحليل بيانات الورشة باستخدام AI")
st.write("عرض البيانات الحية وتحديثها مباشرة من Google Form")

# رابط الـ CSV المباشر
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

# قراءة البيانات من الإنترنت
df = pd.read_csv(CSV_URL)

# عرض جدول ردود المشاركين
st.subheader("بيانات المشاركين")
st.dataframe(df)

# توزيع المشاركين حسب القسم
st.subheader("عدد المشاركين حسب القسم")
# تأكّدي أن العمود في CSV اسمه Department
st.bar_chart(df['Department'].value_counts())

# أكثر مشروع اختيارًا
st.subheader("المشروع الأكثر اختيارًا")
# تأكّدي أن العمود في CSV اسمه ProjectChoice
most_chosen = df['ProjectChoice'].value_counts().idxmax()
st.write(f"المشروع الأكثر اختيارًا هو: {most_chosen}")
