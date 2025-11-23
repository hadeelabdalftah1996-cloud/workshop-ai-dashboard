import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------
st.set_page_config(page_title="AI Workshop Dashboard", layout="wide")
st.title("AI Workshop Live Dashboard")
st.markdown("Track responses and analyze preferred projects by department")

# --------------------------
# Load responses CSV (from Google Forms)
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTeUXVi-EbjECbsrtKKSE4kjFsg5sUi-s0Ezj8PdyWL0yw4DxeNjVVEYPAuJBj00B0KYVqgoRO1TuPD/pub?output=csv"
df = pd.read_csv(csv_url)

# --------------------------
# Test Mode (temporary responses)
st.subheader("💡 Test Mode (Optional)")
test_mode = st.checkbox("Enable test responses")

if test_mode:
    st.info("Add test responses to see live analysis. These won't affect real data.")
    test_department = st.selectbox("Select Department", ["Maintenance", "Operations", "Admin"])
    test_project = st.selectbox("Select Project", ["Safety Helmet Check", "Predictive Maintenance", "Other Project"])
    
    if st.button("Add Test Response"):
        test_row = pd.DataFrame({"Department":[test_department], "ProjectChoice":[test_project]})
        df = pd.concat([df, test_row], ignore_index=True)
        st.success("Test response added! Check table and chart above.")

# --------------------------
# Display full table
st.subheader("Responses Table (Including Test if enabled)")
st.dataframe(df)

# --------------------------
# Most chosen project
if 'ProjectChoice' in df.columns and not df['ProjectChoice'].dropna().empty:
    most_chosen = df['ProjectChoice'].value_counts().idxmax()
    st.success(f"Most chosen project: {most_chosen}")
else:
    st.warning("No responses submitted yet.")

# --------------------------
# Bar chart with colors
if 'Department' in df.columns and 'ProjectChoice' in df.columns:
    st.subheader("Project Selection by Department (Including Test if enabled)")
    plt.figure(figsize=(10,6))
    palette = sns.color_palette("Set2")  # colorful palette
    sns.countplot(data=df, x='ProjectChoice', hue='Department', palette=palette)
    plt.xticks(rotation=45)
    plt.xlabel("Projects", fontsize=12)
    plt.ylabel("Number of selections", fontsize=12)
    plt.title("Number of selections per project by department", fontsize=14)
    plt.legend(title="Department")
    plt.tight_layout()
    st.pyplot(plt)


