import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Settings ---
st.set_page_config(page_title="AI Workshop Dashboard", layout="wide")
st.title("AI Workshop Dashboard")

# --- Load Data ---
DATA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"

df = pd.read_csv(DATA_URL)

st.subheader("Raw Data")
st.dataframe(df)

# --- Map Arabic to English for chart ---
mapping_ai = {
    "مبتدئ": "Beginner",
    "متوسط": "Intermediate",
    "متقدم": "Advanced"
}

mapping_projects = {
    "التنبؤ بالأعطال والصيانة التنبؤية للمحطات والمعدات": "Predictive Maintenance",
    "كشف ارتداء معدات السلامة الشخصية تلقائياً": "Safety Gear Detection",
    "التنبؤ بالاحتياجات من المياه": "Water Demand Forecast"
}

df['AI_Level_EN'] = df['AILevel'].map(mapping_ai)
df['ProjectChoice_EN'] = df['ProjectChoice'].map(mapping_projects)

# --- AI Level Chart ---
st.subheader("AI Knowledge Level")
fig1, ax1 = plt.subplots()
sns.countplot(x='AI_Level_EN', data=df, palette="Set2", ax=ax1)
ax1.set_xlabel("AI Knowledge Level")
ax1.set_ylabel("Number of Participants")
ax1.set_title("Distribution of AI Knowledge Level")
st.pyplot(fig1)

# --- Project Choice Chart ---
st.subheader("Preferred Project to Implement")
fig2, ax2 = plt.subplots()
sns.countplot(x='ProjectChoice_EN', data=df, palette="Set3", ax=ax2)
ax2.set_xlabel("Project")
ax2.set_ylabel("Number of Participants")
ax2.set_title("Most Chosen Project")
plt.xticks(rotation=30)
st.pyplot(fig2)

# --- Summary ---
st.subheader("Summary")
st.write(f"Total Participants: {len(df)}")
st.write(f"Most common AI Level: {df['AI_Level_EN'].mode()[0] if not df.empty else 'No data'}")
st.write(f"Most chosen Project: {df['ProjectChoice_EN'].mode()[0] if not df.empty else 'No data'}")
