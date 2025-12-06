# Standards Crosswalk

| Scope Element | CSF 2.0 Outcome (exact text + page) | ZTA Tenet (exact text + page) | ISO 27001 Theme | Evidence Pointer (repo) |
|--------------|--------------------------------------|-------------------------------|------------------|--------------------------|
| One-step analysis script that reads a small sample dataset and prints a simple metric (for example, count of failed events). | **DE.AE-02 –** “Potentially adverse events are analyzed to better understand associated activities.” (NIST CSF 2.0, p.51) | **Tenet 7 –** “The enterprise collects as much information as possible about the current state of assets, network infrastructure and communications and uses it to improve its security posture.” (NIST SP 800-207, p.6) | Technological | `src/analyze_dataset.py`, `data/sample_data.csv` |
| Run logs folder that documents each script execution, including date, command, input file, and key results. | **RS.AN-07 –** “Incident data and metadata are collected, and their integrity and provenance are preserved.” (NIST CSF 2.0, p.59) | **Tenet 5 –** “The enterprise monitors and measures the integrity and security posture of all owned and associated assets.” (NIST SP 800-207, p.6) | Organizational | `docs/run_logs/run1.md`, `docs/run_logs/README.md` |
| Containerized analysis environment defined in a Dockerfile so the script always runs with the same dependencies and configuration. | **PR.PS-01 –** “Configuration management practices are established and applied.” (NIST CSF 2.0, p.43) | **Tenet 2 –** “All communication is secured regardless of network location.” (NIST SP 800-207, p.5) | Technological | `Dockerfile`, `docs/container_instructions.md` |

---

## Rationale (Row 1 – One-step analysis script)

For this project, the one-step analysis script helps me turn raw data into something meaningful and repeatable. Instead of looking at a log or dataset manually and guessing what matters, the script processes the information the same way every time and produces a simple metric that I can reference or compare across runs. This supports the CSF DE.AE-02 Outcome because I’m analyzing potentially important events, even if they’re synthetic, in a structured and consistent way. It also aligns with Zero Trust Tenet 7 since I am intentionally collecting information about the “state” of my data, reviewing those results, and using them to strengthen how I understand or detect patterns. Even though this is a small project, the script creates a solid foundation for reliable, repeatable analysis.

## Rationale (Row 2 – Run logs folder)

The run logs are important because they document exactly what happened during each execution of my analysis script. Every time I run the script, I capture details like the input file used, the command I ran, the timestamp, and the results. This directly satisfies CSF RS.AN-07 because the logs create a record of incident-style metadata, and they preserve the integrity and history of each run. If something changes unexpectedly in the future, these records let me trace back what happened and why. The logs also support Zero Trust Tenet 5, which emphasizes monitoring and measuring the integrity of assets. In this case, my “assets” are the script, the dataset, and the environment I run them in. The logs help me detect inconsistencies, errors, or unexpected output, which makes my workflow more trustworthy and transparent.

## Rationale (Row 3 – Containerized environment)

Using a Docker container allows me to define my analysis environment in a clear and consistent way. All the dependencies, versions, and configuration details are stored inside the Dockerfile, which means I can recreate the same environment anytime, and anyone else can do the same. This directly aligns with CSF PR.PS-01 because I am applying configuration management practices instead of depending on whatever happens to be installed on my machine. The container also fits with Zero Trust Tenet 2 because it reflects the idea that we shouldn’t rely on trusted networks or trusted devices. Instead, I’m running the analysis in a controlled, isolated environment that I can maintain and secure. This approach reduces surprises, makes the project more repeatable, and gives me a stronger foundation for future security improvements.

---

## Profile Snippet (Current → Target)

(SP 1301 term: Current/Target Profile)

**Current Profile:**
- **PR.PS-01:** Dependencies and tooling are installed manually on the host; configuration varies by user.  
- **DE.AE-02:** Event analysis is performed informally without a reusable script or consistent metric.  
- **RS.AN-07:** There is no structured process for documenting runs or preserving output provenance.

**Target Profile:**
- **PR.PS-01:** All analysis runs execute inside a container with pinned versions and reproducible configuration.  
- **DE.AE-02:** A single, reusable script provides consistent analysis and measurable output.  
- **RS.AN-07:** All runs produce a dated markdown log under `docs/run_logs/`, showing inputs, commands, and results.

