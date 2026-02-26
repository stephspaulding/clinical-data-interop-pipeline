# System Architecture: MIMIC-IV Triage Pipeline

## Overview
This project implements a serverless data pipeline designed to ingest, validate, and visualize clinical data from the MIMIC-IV-ED dataset. The goal is to provide real-time decision support by flagging high-acuity patients.

## Data Flow
1. **Ingestion Layer (GitHub):** Raw clinical CSV files are committed to the repository, acting as the landing zone.
2. **Orchestration & Logic (Pipedream):** - A Python-based workflow triggers on new commits.
    - Logic handles "dirty data" challenges (e.g., nested delimiters).
    - Patients are filtered by Acuity (Levels 1-2).
3. **Presentation Layer (Streamlit):**
    - A cloud-hosted dashboard pulls the processed data.
    - Custom CSS and clinical sorting prioritize unstable patients for ED staff.
