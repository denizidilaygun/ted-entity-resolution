# Data notice

## TED 2023 source data

The full TED 2023 Contract Award Notices dataset is not committed to this repository because of
its size. Section 3 of the notebook downloads it from the configured EU Open Data URL and stores
it under `data/raw/`.

## TED 2022 annotated gold standard

A source copy of `ted2022_gold_standard_valid_979.csv` is included under
`assets/gold_standard_upload/` for reproducible external evaluation. It must be manually copied
or uploaded to `data/gold_standard/` before Section 3 can complete.

The filename refers to the 979 valid binary annotations used by the pipeline. The CSV itself has
999 rows because 20 unresolved annotation rows marked `?` are retained for auditability and
filtered out by the notebook.

Do not use the TED 2022 labels for training, Optuna tuning, model selection, or threshold
selection. The notebook reserves them for one fixed external evaluation.
