## Metrics & Traceability (Assignment 13)

This project includes measurable controls aligned with NIST SP 800-171 Rev. 3.

- **LFMC – Log Field Minimization Compliance**  
  Evaluates how many collected fields match the minimal set required for analysis.  
  Results appear in `docs/metrics_summary.txt` after each script run.

- **RMC – Redacted Metadata Coverage**  
  Measures the percentage of sensitive values that were successfully redacted.  
  Sensitive fields and patterns are listed in `docs/redaction_rules.txt`.

- **DPIR – Dataset Processing Integrity Rate**  
  Tracks whether the script generates consistent results across runs.  
  Integrity state is stored in `docs/dpir_state.json`.

- **SSDI – Synthetic Sampling Diversity Index**  
  Measures dataset diversity across expected scenario types.  

**Traceability Matrix:** See `docs/traceability_matrix.md`.

**Referenced Requirements:** 3.1.5, 3.3.1, 3.3.2, 3.3.5, 3.11.1  
**Referenced Assessment:** A.03.01.05.a

