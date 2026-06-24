# Similarity-Enhanced Duplicate Detection for TED Procurement Records

A reproducible, CPU-only data-science pipeline for supervised entity resolution on
Tenders Electronic Daily (TED) procurement records, external evaluation on an
annotated TED 2022 gold standard, and a pair-level synthetic-data utility and
memorisation-risk audit using CTGAN and TVAE.

## What the pipeline does

The notebook implements the complete empirical workflow:

1. Creates a writable project structure and fixes random seeds.
2. Downloads and extracts the full TED 2023 Contract Award Notices source.
3. Standardises and audits the source schema.
4. Constructs balanced duplicate and difficult non-duplicate candidate pairs.
5. Engineers 17 textual, structured, and identifier-like pairwise features.
6. Compares Logistic Regression, Random Forest, XGBoost, and LightGBM.
7. Tunes the ensemble models with Optuna on an internal TED 2023 tuning subset.
8. Selects the model and decision threshold using TED 2023 validation data only.
9. Evaluates generalisation once on the held-out annotated TED 2022 set.
10. Runs bootstrap confidence intervals, feature ablation, SHAP/permutation
    interpretation, detailed error analysis, and subgroup analysis.
11. Generates synthetic pair-level feature data with CTGAN and TVAE.
12. Evaluates real-only, synthetic-only, and real-plus-synthetic training scenarios.
13. Audits exact-match and nearest-neighbour memorisation risk.
14. Exports reports, figures, a trained model, a run manifest, and a final ZIP package.

## Repository structure

```text
.
├── Deniz_DSS_final.ipynb
├── requirements.txt
├── environment.yml
├── setup_windows.ps1
├── setup_linux_mac.sh
├── assets/
│   └── gold_standard_upload/
│       └── ted2022_gold_standard_valid_979.csv
├── data/
│   ├── raw/
│   ├── processed/
│   └── gold_standard/
├── scripts/
│   ├── check_environment.py
│   └── validate_gold_standard.py
├── reference/
│   ├── notebook/
│   │   └── Deniz_DSS_final_executed.ipynb
│   └── results/
│       ├── reports/
│       └── figures/
├── outputs/
├── reports/
├── figures/
└── models/
```

`Deniz_DSS_final.ipynb` is the clean GitHub-ready notebook. The exact executed
notebook supplied with the thesis is preserved under `reference/notebook/`.

## Environment

The reference execution used:

- Python 3.11
- NumPy 1.26.4
- CPU-only execution
- pandas, scikit-learn, Matplotlib, Seaborn
- RapidFuzz
- Optuna
- XGBoost and LightGBM
- SHAP
- PyArrow and OpenPyXL
- SDV with CTGAN and TVAE
- CPU PyTorch

No administrator rights are required when the environment is created under the
current user account.

## Recommended setup on Windows

Open PowerShell in the cloned repository and run:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup_windows.ps1
```

The script:

- creates the `deniz_dss` Conda environment with Python 3.11;
- installs CPU-only PyTorch;
- installs every package in `requirements.txt`;
- registers the kernel as `Python 3.11 (deniz_dss)`.

Then open the repository folder in VS Code and select that kernel.

## Linux or macOS setup

```bash
chmod +x setup_linux_mac.sh
./setup_linux_mac.sh
```

## Manual setup

```bash
conda create -n deniz_dss python=3.11 -y
conda activate deniz_dss
python -m pip install --upgrade pip setuptools wheel
```

Windows or Linux CPU PyTorch:

```bash
python -m pip install --index-url https://download.pytorch.org/whl/cpu "torch>=2.4,<3.0"
```

Install all remaining dependencies:

```bash
python -m pip install -r requirements.txt
python -m ipykernel install --user --name deniz_dss --display-name "Python 3.11 (deniz_dss)"
```

Validate the environment:

```bash
python scripts/check_environment.py
```

## Required TED 2022 gold-standard placement

The annotated CSV is included in the repository at:

```text
assets/gold_standard_upload/ted2022_gold_standard_valid_979.csv
```

The pipeline deliberately requires manual placement in the active data folder.

### Exact run sequence

1. Clone or download this repository.
2. Open the **repository folder**, not only the notebook file, in VS Code or Jupyter.
3. Select the `Python 3.11 (deniz_dss)` kernel.
4. Start **Run All**.
5. Section 0 creates the project folders.
6. Section 3 downloads/extracts TED 2023 and checks for the TED 2022 gold standard.
7. When Section 3 reports that the gold standard is missing, copy or upload:

```text
assets/gold_standard_upload/ted2022_gold_standard_valid_979.csv
```

to the exact path printed by the notebook, normally:

```text
data/gold_standard/ted2022_gold_standard_valid_979.csv
```

8. Re-run Section 3 to confirm detection.
9. Restart **Run All** from the top.

The CSV has 999 annotation rows. The pipeline uses the 979 rows with valid binary
human labels: 491 non-duplicates and 488 duplicates. The remaining 20 unresolved
rows marked `?` are excluded automatically.

Validate the bundled file before running:

```bash
python scripts/validate_gold_standard.py
```

## TED 2023 source data

The large TED 2023 source file is not stored in GitHub. Section 3 downloads the
configured ZIP from the EU Open Data source and stores/extracts it under
`data/raw/`.

A complete run requires substantial disk space, memory, and CPU time. The
synthetic stage is especially expensive on CPU. In the reference run, CTGAN and
TVAE were each trained for 50 epochs on more than two million pair-level rows.

## Reproducibility and test isolation

- Global random seed: `42`.
- Python is fixed to `3.11`.
- NumPy is fixed to `1.26.4`.
- XGBoost, LightGBM, SDV, and PyTorch are constrained to compatible major
  versions in `requirements.txt`.
- The TED 2022 human labels are reserved for external testing.
- TED 2022 is not used for candidate-pair construction, Optuna tuning, model
  selection, or threshold selection.
- Model and threshold selection are performed on internal TED 2023 development
  and validation data.
- The notebook saves a run manifest, model metadata, predictions, tables,
  figures, and the final trained model.

## Main generated outputs

After a successful run:

- `reports/`: EDA tables, tuning results, validation/external metrics,
  confidence intervals, ablation, error analysis, subgroup results, RQ2 utility,
  and memorisation audit.
- `figures/`: thesis-ready plots.
- `models/`: the selected trained model and metadata.
- `outputs/`: run-specific intermediate outputs.
- `deniz_dss_final_outputs_<RUN_ID>.zip`: compact final output package.

## Reference results

Selected outputs from the completed reference run are included under
`reference/results/`. They are provided for transparency and comparison; a new
run writes fresh outputs to the top-level generated folders.

Reference external test result for the selected Random Forest:

- threshold: 0.50
- accuracy: 0.9755
- precision: 0.9715
- recall: 0.9795
- F1-score: 0.9755
- PR-AUC: 0.9802
- ROC-AUC: 0.9824

## Important execution notes

- The final pipeline is intentionally CPU-only.
- Do not change the external TED 2022 labels or use them for model selection.
- Open the cloned folder as the working directory; otherwise the notebook falls
  back to a user-level `Deniz_thesis_pipeline` directory.
- The notebook can install missing dependencies from `requirements.txt`, but the
  setup scripts are more reliable because compiled packages are installed before
  the Jupyter kernel starts.
- If the dependency bootstrap changes NumPy or another compiled package, restart
  the kernel once and run all again.

## Citation

Update the repository URL in `CITATION.cff` after uploading the project to
GitHub.
