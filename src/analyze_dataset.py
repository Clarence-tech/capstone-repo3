#!/usr/bin/env python3
"""
Assignment 13 metrics script.

Reads data/sample_data.csv and computes:
- LFMC: Log Field Minimization Compliance
- RMC: Redacted Metadata Coverage
- SSDI: Synthetic Sampling Diversity Index
- DPIR: Dataset Processing Integrity Rate
"""

import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path

# ----- Paths -----
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sample_data.csv"
DOCS_DIR = BASE_DIR / "docs"
METRICS_FILE = DOCS_DIR / "metrics_summary.txt"
DPIR_STATE_FILE = DOCS_DIR / "dpir_state.json"

# ----- Metric Config -----
# Minimal fields needed for analysis
MINIMAL_FIELDS = {"timestamp", "event_type", "scenario", "result"}

# Fields considered sensitive (should be redacted)
SENSITIVE_FIELDS = {"user", "host"}

# Expected scenario types for diversity check
EXPECTED_SCENARIOS = {"normal", "error", "anomaly"}


def read_rows():
    """Read CSV rows from DATA_FILE."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_FILE}")

    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
        return fieldnames, rows


# ---------- Metric 1: LFMC ----------
def compute_lfmc(fieldnames):
    """
    LFMC (Log Field Minimization Compliance):
    minimal_fields_used / total_fields * 100
    """
    if not fieldnames:
        return None

    field_set = set(fieldnames)
    used_fields = field_set & MINIMAL_FIELDS
    lfmc = (len(used_fields) / len(field_set)) * 100
    return round(lfmc, 2), sorted(used_fields), sorted(field_set)


# ---------- Metric 2: RMC ----------
def compute_rmc(fieldnames, rows):
    """
    RMC (Redacted Metadata Coverage):
    redacted_sensitive_values / total_sensitive_values * 100
    We treat any value containing 'REDACTED' as redacted.
    """
    sensitive_present = set(fieldnames) & SENSITIVE_FIELDS
    if not sensitive_present or not rows:
        return None

    total_sensitive = 0
    redacted_count = 0

    for row in rows:
        for field in sensitive_present:
            value = (row.get(field) or "").strip()
            if value == "":
                continue
            total_sensitive += 1
            if "REDACTED" in value.upper():
                redacted_count += 1

    if total_sensitive == 0:
        return None

    rmc = (redacted_count / total_sensitive) * 100
    return round(rmc, 2), sorted(sensitive_present), total_sensitive


# ---------- Metric 3: SSDI ----------
def compute_ssdi(fieldnames, rows):
    """
    SSDI (Synthetic Sampling Diversity Index):
    observed_scenarios / expected_scenarios * 100
    """
    if "scenario" not in fieldnames or not rows:
        return None

    observed = set()
    for row in rows:
        val = (row.get("scenario") or "").strip().lower()
        if val:
            observed.add(val)

    if not EXPECTED_SCENARIOS:
        return None

    coverage = (len(observed & EXPECTED_SCENARIOS) /
                len(EXPECTED_SCENARIOS)) * 100
    return round(coverage, 2), sorted(observed), sorted(EXPECTED_SCENARIOS)


# ---------- Metric 4: DPIR ----------
def load_dpir_state():
    """Load DPIR state from JSON; reset if missing or invalid."""
    if not DPIR_STATE_FILE.exists():
        return {"total_runs": 0, "consistent_runs": 0, "last_hash": ""}
    try:
        return json.loads(DPIR_STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {"total_runs": 0, "consistent_runs": 0, "last_hash": ""}


def save_dpir_state(state):
    DPIR_STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def compute_output_hash(rows):
    """Hash the 'result' column to approximate output consistency."""
    h = hashlib.sha256()
    for row in rows:
        value = (row.get("result") or "").strip()
        h.update(value.encode("utf-8"))
    return h.hexdigest()


def compute_dpir(rows):
    """
    DPIR (Dataset Processing Integrity Rate):
    consistent_runs / total_runs * 100
    based on output hash comparison.
    """
    state = load_dpir_state()
    current_hash = compute_output_hash(rows)

    state["total_runs"] += 1
    if state["total_runs"] == 1:
        # first run is our baseline
        state["consistent_runs"] = 1
    else:
        if current_hash == state.get("last_hash", ""):
            state["consistent_runs"] += 1

    state["last_hash"] = current_hash
    save_dpir_state(state)

    dpir = (state["consistent_runs"] / state["total_runs"]) * 100
    return round(dpir, 2), current_hash, state["total_runs"], state["consistent_runs"]


# ---------- Helpers ----------
def append_metrics_to_file(text: str):
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    with METRICS_FILE.open("a", encoding="utf-8") as f:
        f.write(text + "\n\n")


def main():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    fieldnames, rows = read_rows()
    timestamp = datetime.utcnow().isoformat(timespec="seconds") + "Z"

    lfmc_result = compute_lfmc(fieldnames)
    rmc_result = compute_rmc(fieldnames, rows)
    ssdi_result = compute_ssdi(fieldnames, rows)
    dpir_result = compute_dpir(rows)

    lines = [f"=== Metrics Run @ {timestamp} ==="]
    lines.append(f"Data file: {DATA_FILE}")

    # LFMC
    if lfmc_result:
        lfmc, used_fields, all_fields = lfmc_result
        lines.append(f"LFMC (Log Field Minimization Compliance): {lfmc}%")
        lines.append(f"  Minimal fields used: {used_fields}")
        lines.append(f"  All fields present: {all_fields}")
    else:
        lines.append("LFMC: N/A (no fields found)")

    # RMC
    if rmc_result:
        rmc, sensitive_fields, total_vals = rmc_result
        lines.append(f"RMC (Redacted Metadata Coverage): {rmc}%")
        lines.append(f"  Sensitive fields: {sensitive_fields}")
        lines.append(f"  Sensitive values inspected: {total_vals}")
    else:
        lines.append("RMC: N/A (no sensitive fields or no data)")

    # SSDI
    if ssdi_result:
        ssdi, observed, expected = ssdi_result
        lines.append(f"SSDI (Sampling Diversity Index): {ssdi}%")
        lines.append(f"  Observed scenarios: {observed}")
        lines.append(f"  Expected scenarios: {expected}")
    else:
        lines.append("SSDI: N/A (no 'scenario' field or no data)")

    # DPIR
    dpir, out_hash, total_runs, consistent_runs = dpir_result
    lines.append(f"DPIR (Processing Integrity Rate): {dpir}%")
    lines.append(f"  Output hash: {out_hash}")
    lines.append(f"  Total runs: {total_runs}, Consistent runs: {consistent_runs}")

    report = "\n".join(lines)
    print(report)
    append_metrics_to_file(report)


if __name__ == "__main__":
    main()

