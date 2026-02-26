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
    """, unsafe_allow_html=True) # Fixed the parameter name here

st.title("🚨 Emergency Department Triage Monitor")
st.caption("Real-time High-Acuity Filtering | Source: MIMIC-IV-ED")

# 2. Data Ingestion
URL = "https://raw.githubusercontent.com/stephspaulding/clinical-data-interop-pipeline/refs/heads/main/triage.csv"

try:
    # ADDED: Robust CSV parsing for clinical strings
    df = pd.read_csv(
        URL, 
        sep=',', 
        quotechar='"', 
        on_bad_lines='skip', 
        engine='python'
    )
    
    # Standardize column names (strips hidden spaces/casing)
    df.columns = df.columns.str.strip().str.lower()
    
    # Convert acuity to numeric
    df['acuity'] = pd.to_numeric(df['acuity'], errors='coerce')

except Exception as e:
    st.error(f"⚠️ Pipeline Error: Could not parse clinical data. Details: {e}")
    st.stop()

# 4. Interactive Display
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("🔥 Immediate Intervention Queue")
    
    # Robust styling logic
    def highlight_vitals(s):
        # We check if heart rate exists and is over 100
        return ['background-color: #701c1c' if (not pd.isna(s.heartrate) and s.heartrate > 100) else '' for _ in s]

    display_cols = ['subject_id', 'acuity', 'chiefcomplaint', 'heartrate', 'temperature', 'resprate']
    
    st.dataframe(
        high_priority[display_cols].style.apply(highlight_vitals, axis=1),
        use_container_width=True,
        hide_index=True
    )

with right_col:
    st.subheader("Chief Complaint Trends")
    complaint_counts = high_priority['chiefcomplaint'].value_counts().head(10)
    st.bar_chart(complaint_counts, horizontal=True)

st.info("💡 **Clinical Note:** Rows highlighted in red indicate Tachycardia (HR > 100) within the High-Acuity subset.")
