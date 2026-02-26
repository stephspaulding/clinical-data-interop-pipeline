import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="MIMIC-IV Triage Command Center", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for the "Command Center" look
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 40px; color: #ff4b4b; }
    .stDataFrame { border: 1px solid #31333F; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚨 Emergency Department Triage Monitor")
st.caption("Real-time High-Acuity Filtering | Source: MIMIC-IV-ED")

# 2. Data Ingestion
URL = "https://raw.githubusercontent.com/stephspaulding/clinical-data-interop-pipeline/refs/heads/main/triage.csv"

try:
    df = pd.read_csv(
        URL, 
        sep=',', 
        quotechar='"', 
        on_bad_lines='skip', 
        engine='python'
    )
    
    # Standardize column names to lowercase and remove spaces
    df.columns = df.columns.str.strip().str.lower()
    
    # Ensure acuity and vitals are numeric
    df['acuity'] = pd.to_numeric(df['acuity'], errors='coerce')
    df['heartrate'] = pd.to_numeric(df['heartrate'], errors='coerce')

    # Filter for High Priority
    high_priority = df[df['acuity'] <= 2].copy()

except Exception as e:
    st.error(f"⚠️ Pipeline Error: {e}")
    st.stop()

# 3. Top-Level Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Critical Alerts", len(high_priority))
with col2:
    percent_critical = (len(high_priority) / len(df)) * 100 if len(df) > 0 else 0
    st.metric("Acuity Load", f"{percent_critical:.1f}%")
with col3:
    avg_hr = high_priority['heartrate'].mean()
    st.metric("Avg HR (Critical)", f"{int(avg_hr) if not pd.isna(avg_hr) else 0} bpm")
with col4:
    st.metric("System Status", "Live", delta="Active")

st.divider()

# 4. Interactive Display
left_col, right_col = st.columns([2, 1])

# Define columns once, globally, to avoid NameErrors
target_cols = ['subject_id', 'acuity', 'chiefcomplaint', 'heartrate', 'temperature', 'resprate']

with left_col:
    st.subheader("🔥 Immediate Intervention Queue")
    
    def highlight_vitals(s):
        # Apply red background if Heart Rate > 100
        return ['background-color: #701c1c' if (not pd.isna(s.heartrate) and s.heartrate > 100) else '' for _ in s]

    # Use the target_cols we defined above
    if not high_priority.empty:
        st.dataframe(
            high_priority[target_cols].style.apply(highlight_vitals, axis=1),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.write("No high-acuity patients detected.")

with right_col:
    st.subheader("Chief Complaint Trends")
    if not high_priority.empty:
        complaint_counts = high_priority['chiefcomplaint'].value_counts().head(10)
        st.bar_chart(complaint_counts, horizontal=True)

st.info("💡 **Clinical Note:** Rows highlighted in red indicate Tachycardia (HR > 100) within the High-Acuity subset.")
