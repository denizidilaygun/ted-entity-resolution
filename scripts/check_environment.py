from __future__ import annotations

import importlib
import platform
import sys

PACKAGES = [
    "numpy",
    "pandas",
    "pyarrow",
    "sklearn",
    "matplotlib",
    "seaborn",
    "rapidfuzz",
    "optuna",
    "xgboost",
    "lightgbm",
    "shap",
    "openpyxl",
    "sdv",
    "torch",
    "joblib",
]

print("Python:", sys.version)
print("Executable:", sys.executable)
print("Platform:", platform.platform())

failed = []
for package in PACKAGES:
    try:
        module = importlib.import_module(package)
        version = getattr(module, "__version__", "version not exposed")
        print(f"OK  {package}: {version}")
    except Exception as exc:
        failed.append((package, repr(exc)))
        print(f"FAIL {package}: {exc!r}")

if sys.version_info[:2] != (3, 11):
    failed.append(("python", f"Expected Python 3.11, found {sys.version.split()[0]}"))

try:
    import numpy as np
    if np.__version__ != "1.26.4":
        failed.append(("numpy", f"Expected 1.26.4, found {np.__version__}"))
except Exception:
    pass

try:
    import torch
    print("CUDA available:", torch.cuda.is_available())
except Exception:
    pass

if failed:
    raise SystemExit(f"Environment check failed: {failed}")

print("Environment check passed.")
