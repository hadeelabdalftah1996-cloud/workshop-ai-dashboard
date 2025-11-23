import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------
# إعداد الصفحة
st.set_page_config(page_title="AI Workshop Dashboard", layout="wide")
st.title("AI Workshop Live Dashboard")
st.markdown("تابعوا الردود وتحليلاتها لحظيًا")

# --------------------------
# رابط CSV العام للفورم
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

# قراءة البيانات
df = pd.read_csv(csv_url)

# --------------------------
# عرض الجدول الكامل
st.subheader("جدول الردود")
st.dataframe(df)

# --------------------------
# تحليل المشاريع الأكثر اختيارًا
if 'ProjectChoice' in df.columns and not df['ProjectChoice'].dropna().empty:
    most_chosen = df['ProjectChoice'].value_counts().idxmax()
    st.success(f"المشروع الأكثر اختيارًا: {most_chosen}")
else:
    st.warning("لم يتم إدخال أي اختيارات بعد.")

# --------------------------
# رسم بياني: عدد الاختيارات لكل مشروع حسب القسم
if 'Department' in df.columns and 'ProjectChoice' in df.columns:
    st.subheader("تحليل حسب القسم")
    plt.figure(figsize=(10,6))
    sns.countplot(data=df, x='ProjectChoice', hue='Department')
    plt.xticks(rotation=45)
    plt.title("عدد الاختيارات لكل مشروع حسب القسم")
    plt.tight_layout()
    st.pyplot(plt)
