import streamlit as st
import pandas as pd

# 1. Page Configuration for a Professional Feel
st.set_page_config(page_title="MIMIC-IV Triage Command Center", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS to make metrics pop
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 40px; color: #ff4b4b; }
    .stDataFrame { border: 1px solid #31333F; border-radius: 10px; }
    </style>
    """, unsafe_allow_stdio=True)

st.title("🚨 Emergency Department Triage Monitor")
st.caption("Real-time High-Acuity Filtering | Source: MIMIC-IV-ED")

# 2. Data Ingestion & Cleaning
URL = "https://raw.githubusercontent.com/stephspaulding/clinical-data-interop-pipeline/refs/heads/main/triage.csv"
df = pd.read_csv(URL)
df['acuity'] = pd.to_numeric(df['acuity'], errors='coerce')

# Logic for High Priority
high_priority = df[df['acuity'] <= 2].copy()

# 3. Top-Level KPIs (The 1-Second Info)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Critical Alerts", len(high_priority))
with col2:
    # Calculate % of volume that is high acuity
    percent_critical = (len(high_priority) / len(df)) * 100
    st.metric("Acuity Load", f"{percent_critical:.1f}%")
with col3:
    avg_hr = high_priority['heartrate'].mean()
    st.metric("Avg HR (Critical)", f"{avg_hr:.0f} bpm")
with col4:
    st.metric("System Status", "Live", delta="Active")

st.divider()

# 4. Two-Column Insights
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("🔥 Immediate Intervention Queue")
    
    # Conditional Styling: Highlight rows with high heart rates
    def highlight_vitals(s):
        return ['background-color: #701c1c' if s.heartrate > 100 else '' for _ in s]

    # Display clean table with specific columns
    display_cols = ['subject_id', 'acuity', 'chiefcomplaint', 'heartrate', 'temperature', 'resprate']
    st.dataframe(
        high_priority[display_cols].style.apply(highlight_vitals, axis=1),
        use_container_width=True,
        hide_index=True
    )

with right_col:
    st.subheader("Chief Complaint Trends")
    # Horizontal bar chart for easier reading of text labels
    complaint_counts = high_priority['chiefcomplaint'].value_counts().head(10)
    st.bar_chart(complaint_counts, horizontal=True)

# 5. Risk Legend
st.info("💡 **Clinical Note:** Rows highlighted in red indicate Tachycardia (HR > 100) within the High-Acuity subset.")
