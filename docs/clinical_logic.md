# Clinical Decision Support (CDS) Logic

## Triage Criteria
The dashboard prioritizes patients based on the following logic:

1. **Acuity Filtering:** Only patients with an ESI (Emergency Severity Index) of **1 (Immediate)** or **2 (Emergent)** are displayed in the primary queue.
2. **Visual Alerts (Tachycardia):**
    - **Logic:** `Heart Rate > 100 bpm`.
    - **UI Response:** Row background changes to Alert Coral (#ffcccc) to signal potential clinical instability or sepsis risk.
3. **Sorting:** The list is sorted primarily by **Acuity level** and secondarily by **Heart Rate (descending)** to ensure the most unstable patients appear at the top of the "Immediate Attention" queue.
