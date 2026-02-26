import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="ED Command Center", layout="wide")

# Updated CSS for better readability
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 38px; font-weight: 700; }
    /* Soften the red alert color for readability */
    .stDataFrame [data-testid="stTable"] { font-family: sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚨 ED Triage Command Center")
st.caption("MIMIC-IV Real-time High-Acuity Monitor")

# 2. Data Ingestion
URL = "https://raw.githubusercontent.com/stephspaulding/clinical-data-interop-pipeline/refs/heads/main/triage.csv"

try:
    df = pd.read_csv(URL, sep=',', quotechar='"', on_bad_lines='skip', engine='python')
    df.columns = df.columns.str.strip().str.lower()
    df['acuity'] = pd.to_numeric(df['acuity'], errors='coerce')
    df['heartrate'] = pd.to_numeric(df['heartrate'], errors='coerce')
    
    # --- CLINICAL SORTING LOGIC ---
    # 1. Acuity (1 first)
    # 2. Heart rate (Highest first - indicates distress)
    df = df.sort_values(by=['acuity', 'heartrate'], ascending=[True, False])
    
    high_priority = df[df['acuity'] <= 2].copy()
except Exception as e:
    st.error(f"Sync Error: {e}")
    st.stop()

# 3. Clinical Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Critical Alerts", len(high_priority))
col2.metric("Acuity Load", f"{(len(high_priority)/len(df)*100):.1f}%")
col3.metric("Avg HR (Critical)", f"{int(high_priority['heartrate'].mean())} bpm")
col4.metric("System Status", "Live", delta="Active")

st.divider()

# 4. Refined View
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("🔥 Immediate Attention Required")
    
    def style_critical(res):
        # Using a softer red (#ffcccc) with black text for better contrast
        # Only highlight if Acuity is 1 AND Heartrate is high
        color = 'background-color: #ffcccc; color: black; font-weight: bold;'
        default = ''
        return [color if (res.acuity == 1 or res.heartrate > 100) else default for _ in res]

    target_cols = ['subject_id', 'acuity', 'chiefcomplaint', 'heartrate', 'temperature', 'resprate']
    
    st.dataframe(
        high_priority[target_cols].style.apply(style_critical, axis=1),
        use_container_width=True,
        hide_index=True
    )

with right_col:
    st.subheader("Top Chief Complaints")
    # Sorted descending as requested
    complaint_counts = high_priority['chiefcomplaint'].value_counts().sort_values(ascending=True).tail(10)
    st.bar_chart(complaint_counts, horizontal=True)

st.info("💡 **Triage Logic:** Patients are sorted by Acuity (1-2) and descending Heart Rate. Red highlight indicates clinical instability.")
