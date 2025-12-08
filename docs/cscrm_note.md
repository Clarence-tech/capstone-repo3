# C-SCRM Dependency Note

For brainstorming, concept refinement, and draft generation, this project depends on the
OpenAI ChatGPT API as an external tool. The main supply-chain risks are model integrity
and dependency trust — for example, silent model updates, external service outages, or
behavioral changes that could affect reproducibility. Another concern is that this is a
third-party service whose infrastructure, update schedule, and underlying model weights
are outside the researcher’s direct control.

## NIST SP 800-161r1-upd1 Reference

Copy-exact reference (per assignment requirement):

> “3.3.1 Security Capability: Software and Firmware Integrity,” NIST SP 800-161r1-upd1, p. 71.

## Mitigations and Evidence

1. **SBOM Tracking**  
   - `SBOM.txt` records the date of each interaction used for project work along with
     the model identifiers, provider, and version comments.

2. **Content Integrity**  
   - `data/README.md` stores SHA-256 hashes of downloaded outputs or exported files
     (such as code snippets or text files) so that content provenance and integrity
     can be verified later.

Evidence locations in the repo:

- `docs/cscrm_note.md` — this note and the NIST citation.
- `SBOM.txt` — dependency name/version + provenance notes.
- `data/README.md` — hashes and validation notes.
