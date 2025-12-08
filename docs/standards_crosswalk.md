# Standards Crosswalk (Capstone Ransomware Project)

## Crosswalk Table

| Scope Element                                                                 | CSF 2.0 Outcome (copy-exact ID + text)                                                                                  | ZTA Tenet (ID + text)                                                                                                                   | ISO 27001 Theme | Evidence Pointer (repo)                          |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------|
| One-step analysis script that reads a small sample dataset and prints metrics| **DE.AE-02:** “Potentially adverse events are analyzed to better understand associated activities.” (CSF 2.0, App. A, p. 51) | **Tenet 7:** “The enterprise collects as much information as possible about the current state of assets, network infrastructure, and communications.” (SP 800-207, p. 6) | Technological   | `src/analyze_dataset.py`, `data/sample_data.csv` |
| Run logs folder that documents each script execution (inputs, command, time) | **RS.AN-07:** “Incident data and metadata are collected, and their integrity and provenance are preserved.” (CSF 2.0, App. A, p. 59) | **Tenet 5:** “The enterprise monitors and measures the integrity and security posture of all owned and associated assets.” (SP 800-207, p. 6) | Organizational  | `docs/run_logs/run1.md`                          |
| Containerized environment using a Dockerfile (if present)                     | **PR.PS-01:** “Configuration management practices are established and applied.” (CSF 2.0, App. A, p. 43)                  | **Tenet 2:** “All communication is secured regardless of network location.” (SP 800-207, p. 5)                                          | Technological   | `Dockerfile`, `docs/container_instructions.md`   |

## Rationale 1 — One-Step Analysis Script

The one-step analysis script converts raw synthetic data into repeatable metrics used to
understand events and patterns. Instead of manually scanning logs, the script consistently
processes the dataset and produces metrics such as LFMC, RMC, SSDI, and DPIR. This supports
CSF **DE.AE-02** because potentially adverse events are analyzed in a systematic way, and
it aligns with Zero Trust **Tenet 7** by intentionally collecting and processing state
information about assets and events.

## Rationale 2 — Run Logs Folder

The run logs record each execution of the analysis script, including the input file, command
used, timestamp, and resulting metrics. This satisfies CSF **RS.AN-07** by preserving incident-
style metadata and provenance for every run. It supports Zero Trust **Tenet 5** by treating
the analysis workflow as an asset whose behavior and integrity must be monitored over time.

## Rationale 3 — Containerized Environment

When a Docker container is used, the analysis environment is defined entirely as code, with
dependencies and configuration pinned in `Dockerfile`. This implements CSF **PR.PS-01**
because configuration management is established and applied consistently. It supports Zero Trust
**Tenet 2** by reducing reliance on any “trusted” network or host and ensuring that the
analysis does not depend on uncontrolled external configurations.

## Profile Snippet (Current → Target)

- **Current Profile:** Dependencies and tooling may be installed manually on the host,
  and configuration can vary by user. Event analysis is performed informally without a
  reusable script or consistent metrics.

- **Target Profile:** All analysis runs execute inside a controlled environment with pinned
  versions and reproducible configuration. A single reusable script provides consistent
  analysis and measurable output, and all runs generate dated markdown logs under
  `docs/run_logs/`, capturing inputs, commands, and results.



