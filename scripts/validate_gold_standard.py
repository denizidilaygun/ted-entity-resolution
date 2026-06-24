from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "pair_id",
    "human_label",
    "human_confidence",
    "candidate_rule",
    "record1_authority",
    "record2_authority",
    "record1_supplier",
    "record2_supplier",
    "record1_title",
    "record2_title",
    "record1_cpv",
    "record2_cpv",
    "record1_country",
    "record2_country",
    "record1_value_euro",
    "record2_value_euro",
}

parser = argparse.ArgumentParser()
parser.add_argument(
    "path",
    nargs="?",
    default="assets/gold_standard_upload/ted2022_gold_standard_valid_979.csv",
)
args = parser.parse_args()

path = Path(args.path)
if not path.exists():
    raise SystemExit(f"File not found: {path}")

df = pd.read_csv(path)
missing = sorted(REQUIRED_COLUMNS - set(df.columns))
if missing:
    raise SystemExit(f"Missing required columns: {missing}")

valid = df[df["human_label"].isin([0, 1, "0", "1"])].copy()
labels = valid["human_label"].astype(int)

print("CSV rows:", len(df))
print("Valid binary annotations:", len(valid))
print("Unresolved annotations:", len(df) - len(valid))
print("Label distribution:", labels.value_counts().sort_index().to_dict())

if len(valid) != 979:
    raise SystemExit(f"Expected 979 valid annotations, found {len(valid)}")

if labels.value_counts().to_dict() != {0: 491, 1: 488}:
    raise SystemExit("Unexpected valid-label distribution.")

print("Gold-standard validation passed.")
