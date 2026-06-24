# GitHub upload checklist

1. Extract this repository ZIP.
2. Review `README.md` and replace the placeholder repository URL in `CITATION.cff`.
3. Create an empty GitHub repository.
4. Upload the extracted contents, preserving the folder structure.
5. Confirm that these files are visible:
   - `Deniz_DSS_final.ipynb`
   - `requirements.txt`
   - `environment.yml`
   - `setup_windows.ps1`
   - `assets/gold_standard_upload/ted2022_gold_standard_valid_979.csv`
6. Do not commit generated `data/raw`, `data/processed`, `outputs`, `reports`, `figures`, or `models` files from later runs unless deliberately publishing them.
7. Test the repository on a clean Python 3.11 environment.
8. Validate the gold file with:
   `python scripts/validate_gold_standard.py`
9. Validate dependencies with:
   `python scripts/check_environment.py`
