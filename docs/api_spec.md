# Data Schema & Interoperability Standards

## Source Schema (MIMIC-IV-ED)
| Field | Description | Type |
| :--- | :--- | :--- |
| `subject_id` | Unique patient identifier | Integer |
| `acuity` | Emergency Severity Index (1: Immediate, 5: Non-urgent) | Float |
| `chiefcomplaint` | Presenting symptom reported by patient | String |
| `heartrate` | Patient beats per minute | Float |

## FHIR Mapping (Roadmap)
To align with HL7 FHIR standards, the following mapping is proposed for future iterations:

| CSV Column | FHIR Resource | LOINC/SNOMED Code |
| :--- | :--- | :--- |
| `heartrate` | `Observation.valueQuantity` | `8867-4` (Heart rate) |
| `temperature` | `Observation.valueQuantity` | `8310-5` (Body temperature) |
| `chiefcomplaint` | `Condition.code` | SNOMED CT Mapping required |
