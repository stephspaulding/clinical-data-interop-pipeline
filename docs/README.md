# MIMIC-IV Clinical AI Triage Pipeline 🏥 ⚡

An automated end-to-end data interoperability pipeline that triages emergency department data using the MIMIC-IV-ED dataset.

## 🚀 The Solution
This project automates the ingestion of clinical CSV data via GitHub, processes it through a cloud-based Python logic engine (Pipedream), and identifies high-acuity patients (Acuity 1-2) for immediate clinical intervention.

### Key Features:
- **Automated Ingestion:** Real-time triggers on GitHub commits.
- **Data Validation:** Hardened Python ingestion layer that handles malformed CSV delimiters and encoding issues.
- **Clinical Logic:** Automated triage identifies high-priority cases (115 alerts detected in demo).
- **Interoperability:** Built for rapid validation of health-tech startup data.

## 🛠️ Tech Stack
- **Data Source:** MIMIC-IV-ED (Clinical Database)
- **Orchestration:** Pipedream (Serverless Workflows)
- **Logic:** Python (Pandas, Requests, IO)
- **Version Control:** GitHub
