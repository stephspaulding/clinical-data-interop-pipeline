# MIMIC-IV Clinical AI Triage Pipeline 🏥 ⚡

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://mimic-triage-validator.streamlit.app/)

An automated end-to-end data interoperability pipeline that triages emergency department data using the MIMIC-IV-ED dataset.

## 🚀 Live Demo
**View the Dashboard:** [https://mimic-triage-validator.streamlit.app/](https://mimic-triage-validator.streamlit.app/)

## 🛠️ System Overview
This project automates the ingestion of clinical CSV data, processes it through a serverless Python logic engine (Pipedream), and identifies high-acuity patients for immediate clinical intervention.

### Key Documentation:
- [🏗️ Architecture & Data Flow](docs/architecture.md)
- [🧬 API Spec & FHIR Mapping](docs/api_spec.md)
- [🩺 Clinical Logic & Triage Rules](docs/clinical_logic.md)

## 🛠️ Tech Stack
- **Data Source:** MIMIC-IV-ED (Clinical Database)
- **Orchestration:** Pipedream (Serverless Workflows)
- **Logic:** Python (Pandas, Requests)
- **Visualization:** Streamlit Cloud
- **Version Control:** GitHub

## 🧪 Quick Start
1. Clone the repo.
2. Ensure `requirements.txt` dependencies are installed.
3. Run `streamlit run app.py` to launch the local dashboard.
