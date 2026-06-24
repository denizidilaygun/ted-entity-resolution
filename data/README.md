# Data directory

The pipeline creates and uses the following folders:

- `raw/`: the TED 2023 ZIP and extracted CSV. The notebook downloads the ZIP automatically.
- `processed/`: standardised records, engineered pair features, and intermediate datasets.
- `gold_standard/`: the external TED 2022 annotated test file.

## Required manual file placement

Copy:

`assets/gold_standard_upload/ted2022_gold_standard_valid_979.csv`

to:

`data/gold_standard/ted2022_gold_standard_valid_979.csv`

The source CSV contains 999 annotation rows. The pipeline uses the 979 rows with valid binary
`human_label` values (`491` non-duplicates and `488` duplicates) and excludes 20 unresolved rows
labelled `?`.

The TED 2022 gold standard is reserved for external evaluation. It is not used for TED 2023
candidate-pair construction, model tuning, model selection, or threshold selection.
