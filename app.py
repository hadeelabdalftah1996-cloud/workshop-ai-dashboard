# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# إعداد صفحة Streamlit
st.set_page_config(page_title="SEPCO AI Workshop", page_icon="🤖", layout="wide")

# ---------------------------
# شعار واسم الشركة
st.image("logo.jpg", width=200)
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>🤖 SEPCO AI Workshop Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------
# رابط CSV من Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(sheet_url)

# ---------------------------
# تنظيف الأعمدة
df['AILevel'] = df['AILevel'].fillna('No Response')
df['ProjectChoice'] = df['ProjectChoice'].fillna('No Response')

# ---------------------------
# Mapping للـ AI Levels + إيموجي
mapping_ai = {
    "معرفة بسيطة": "🟢 Basic",
    "معرفة متوسطة": "🟡 Intermediate",
    "معرفة متقدمة": "🔵 Advanced"
}
df['AI_Level_EN'] = df['AILevel'].map(mapping_ai).fillna(df['AILevel'])

# ---------------------------
# Mapping للمشاريع بالعربي → إنجليزي + إيموجي كبير
project_mapping = {
    "كتابة وتحديث إجراءات التشغيل sop": "📝 Update & Write SOP",
    "تحليل وبناء ال FMEA": "📊 FMEA Analysis & Build",
    "تحليل الاعطال والتوقفات القسرية": "⚡ Failure & Downtime Analysis",
    "مساعد للمشغل والمهندس": "🤖 Operator & Engineer Assistant",
    "التحكم بالوصول الى مراكز البيانات": "🔐 Access Control to Data Centers",
    "تخطيط المشتريات": "📦 Procurement Planning"
}
df['ProjectChoice_EN'] = df['ProjectChoice'].map(project_mapping).fillna(df['ProjectChoice'])

# ---------------------------
# عرض جدول الإجابات بألوان حسب مستوى AI
st.subheader("Survey Responses")
def color_row(row):
    if '🟢' in row['AI_Level_EN']:
        return ['background-color: #d4f4dd']*len(row)
    elif '🟡' in row['AI_Level_EN']:
        return ['background-color: #fff4c2']*len(row)
    elif '🔵' in row['AI_Level_EN']:
        return ['background-color: #d0e1f9']*len(row)
    else:
        return ['']*len(row)

st.dataframe(df[['AI_Level_EN', 'ProjectChoice_EN']].style.apply(color_row, axis=1), width=900, height=400)

# ---------------------------
# شارت مستويات AI
st.subheader("AI Knowledge Level Distribution")
fig_ai = px.pie(
    df,
    names='AI_Level_EN',
    values=df['AI_Level_EN'].value_counts(),
    color='AI_Level_EN',
    color_discrete_sequence=['#2ca02c','#ff7f0e','#1f77b4']
)
fig_ai.update_traces(textinfo='percent+label', textfont_size=20, pull=[0.05]*len(df['AI_Level_EN'].unique()))
st.plotly_chart(fig_ai, use_container_width=True)

# ---------------------------
# شارت المشاريع
st.subheader("Project Choice Distribution")
fig_proj = px.pie(
    df,
    names='ProjectChoice_EN',
    values=df['ProjectChoice_EN'].value_counts(),
    color='ProjectChoice_EN',
    color_discrete_sequence=px.colors.qualitative.Set3
)
fig_proj.update_traces(textinfo='percent+label', textfont_size=18, pull=[0.05]*len(df['ProjectChoice_EN'].unique()))
st.plotly_chart(fig_proj, use_container_width=True)

# ---------------------------
# ملخص سريع
st.subheader("Summary")
most_common_ai = df['AI_Level_EN'].mode()[0] if not df.empty else 'No data'
most_chosen_proj = df['ProjectChoice_EN'].mode()[0] if not df.empty else 'No data'

st.markdown(f"<h3 style='color: #2ca02c;'>Most common AI Level: {most_common_ai}</h3>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color: #ff7f0e;'>Most chosen Project: {most_chosen_proj}</h3>", unsafe_allow_html=True)



