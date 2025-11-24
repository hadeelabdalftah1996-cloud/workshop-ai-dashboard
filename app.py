import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# رابط CSV المنشور من Google Forms/Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

# قراءة البيانات
df = pd.read_csv(sheet_url)

# عنوان التطبيق
st.title("Workshop AI Dashboard")

# عرض البيانات كجدول
st.subheader("Raw Data / البيانات الأولية")
st.dataframe(df)

# عرض مستوى المعرفة بالذكاء الاصطناعي
st.subheader("AI Knowledge Level / مستوى المعرفة بالذكاء الاصطناعي")
if 'AILevel' in df.columns:
    ai_counts = df['AILevel'].value_counts()
    fig, ax = plt.subplots()
    ai_counts.plot(kind='bar', color=['lightgreen', 'gold', 'tomato'], ax=ax)
    ax.set_ylabel("Count / العدد")
    ax.set_xlabel("AI Level / مستوى الذكاء الاصطناعي")
    ax.set_title("Participants by AI Knowledge Level / المشاركون حسب مستوى المعرفة")
    st.pyplot(fig)
else:
    st.warning("Column 'AILevel' not found in the sheet / عمود 'AILevel' غير موجود.")

# عرض شارت لخيارات المشاريع
st.subheader("Project Choices / اختيارات المشاريع")
if 'ProjectChoice' in df.columns:
    project_counts = df['ProjectChoice'].value_counts()
    fig2, ax2 = plt.subplots()
    project_counts.plot(kind='bar', color='skyblue', ax=ax2)
    ax2.set_ylabel("Count / العدد")
    ax2.set_xlabel("Projects / المشاريع")
    ax2.set_title("Number of participants per project / عدد المشاركين لكل مشروع")
    st.pyplot(fig2)
else:
    st.warning("Column 'ProjectChoice' not found in the sheet / عمود 'ProjectChoice' غير موجود.")








