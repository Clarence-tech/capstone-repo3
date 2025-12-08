# Data README

This folder contains synthetic data used for the ransomware/SIEM analysis in Capstone 698.

## Files

- `sample_data.csv` – synthetic login or event records that are processed by
  `src/analyze_dataset.py`.

## Integrity

To verify file integrity, run:69bf96a313d898329a7d6251fd1626e9822ea6517741ec8870dc532cb2769540

```bash
shasum -a 256 data/sample_data.csv
