# MIMIC-IV Clinical AI Triage Pipeline 🏥 ⚡

An automated end-to-end data interoperability pipeline that triages emergency department data using the MIMIC-IV-ED dataset.

## 🚀 Live Demo
**View the Dashboard:** [https://mimic-triage-validator.streamlit.app/](https://mimic-triage-validator.streamlit.app/)

## 🛠️ System Overview
This project automates the ingestion of clinical CSV data, processes it through a serverless Python logic engine (Pipedream), and identifies high-acuity patients for immediate clinical intervention.

### 📖 Key Documentation
| Resource | Description |
| :--- | :--- |
| [🏗️ Architecture & Data Flow](./docs/architecture.md) | High-level system design and serverless pipeline orchestration. |
| [🧬 API Spec & FHIR Mapping](./docs/api_spec.md) | Technical schema and crosswalk to HL7 FHIR R4 standards. |
| [🩺 Clinical Logic & Triage Rules](./docs/clinical_logic.md) | Rules for patient prioritization and clinical decision support (CDS). |

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
