# Traceability Matrix – Assignment 13

| Risk Identified (Weeks 7–8)                                    | NIST SP 800-171 Rev. 3 Requirement               | Metric Used                           | Evidence Location in Repo                                |
|---------------------------------------------------------------|--------------------------------------------------|----------------------------------------|----------------------------------------------------------|
| Collecting unnecessary log fields that increase exposure      | 3.1.5 – Least Privilege / Data Minimization       | LFMC                                   | src/analyze_dataset.py; docs/run_logs/run1.md            |
| Metadata revealing internal hosts or usernames                | 3.3.2 – Audit Record Content                      | RMC                                    | docs/redaction_rules.txt; docs/run_logs/run1.md          |
| Inconsistent output reducing audit reliability                | 3.3.1 – Audit Logging & Integrity                 | DPIR                                   | docs/dpir_state.json; docs/metrics_summary.txt           |
| Dataset bias causing misleading or incomplete conclusions     | 3.11.1 – Risk Assessment                          | SSDI                                   | data/sample_data.csv; docs/metrics_summary.txt           |
| Unsafe or unverifiable handling of log data                   | 3.3.5 – Audit Record Retention & Protection       | DPIR                                   | docs/run_logs/; docs/dpir_state.json                     |

