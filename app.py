import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="MIMIC-IV Triage Dashboard", layout="wide")
st.title("🏥 Clinical AI Triage Monitor")

# 2. Fetch Data
URL = "https://raw.githubusercontent.com/stephspaulding/clinical-data-interop-pipeline/refs/heads/main/triage.csv"
df = pd.read_csv(URL)

# 3. Clean and Triage (Mirror your Pipedream logic)
df['acuity'] = pd.to_numeric(df['acuity'], errors='coerce')
high_priority = df[df['acuity'] <= 2]

# 4. Dashboard Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Patients", len(df))
col2.metric("Critical Alerts", len(high_priority), delta_color="inverse")
col3.metric("Avg Temp", f"{df['temperature'].mean():.1f}°F")

# 5. Interactive Visualization
st.subheader("High Acuity Patient List")
st.dataframe(high_priority, use_container_width=True)

st.subheader("Chief Complaint Volume")
st.bar_chart(high_priority['chiefcomplaint'].value_counts())
