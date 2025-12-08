# Data Management Plan (Capstone Ransomware Project)

## A. Data Inventory

| Dataset / Artifact                             | Sensitivity                                   | Source                                  |
|-----------------------------------------------|-----------------------------------------------|-----------------------------------------|
| Interview Notes (role-play only)              | Low – No real PII                             | Synthetic / role-play text              |
| System Log Snippets (Windows/Linux examples)  | Medium – may contain hostnames or metadata    | System exports with redacted identifiers |
| Synthetic Artifacts (mock alerts, sample CSV) | Low                                           | Artificially generated for analysis     |
| Research Notes & Codes                        | Low                                           | Researcher-generated                    |
| Screenshots (redacted)                        | Medium – may show environment details         | Captured and redacted by researcher     |

## B. Storage & Access

- **Storage Locations**
  - Local encrypted folder: `~/ResearchProject/data/`
  - Repo structure (private or restricted access):
    - `data/raw/` – redacted system artifacts
    - `data/processed/` – derived datasets and metrics
    - `docs/` – notes, DMP, C-SCRM materials

- **Protections**
  - Full-disk encryption via macOS FileVault.
  - Only encrypted channels for transfers (HTTPS, SSH).
  - When archived, medium-sensitivity files are compressed with AES-256 encryption.

- **Access Restrictions (Least Privilege)**
  - Only the primary researcher (Clarence Campbell) has read/write access.
  - No collaborator access is granted during the course.

## C. Holding and Disposal

- **Retention Time**
  - All project data is kept until the final project grade is announced.

- **Disposal Trigger**
  - Delete fourteen days after the instructor confirms the semester is over.

- **Method of Disposal**
  - Secure deletion on macOS (e.g., permanent delete + empty trash).
  - Deletion of encrypted archives plus removal of stored decryption keys.

## D. Provenance & Versioning

- **Version Control**
  - Private Git repository with tagged milestones (e.g., `v1-preanalysis`, `v2-final`).

- **Provenance Tracking**
  - `data/README.md` includes SHA-256 hashes for raw artifacts and notes on
    transformations (normalization, redaction scripts, etc.).
  - Processing notes are stored in `docs/processing_log.txt` or notebooks.

## E. Sharing & Reuse

- **Sharing Policy**
  - Project data is not shared during the course.
  - Rationale: includes environment metadata, synthetic system logs, and role-play artifacts.

- **Reuse**
  - Redacted synthetic materials may be reused in future coursework with instructor approval.

## F. Compliance & Evidence

Evidence of data-management practices is maintained in the repo:

- `docs/access_log.md` — record that only the primary researcher accessed files.
- `data/README.md` — hashes and provenance notes.
- `docs/retention_checklist.md` — verification of disposal after the course.
- Git commit history — shows versioning and change tracking.
