#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="${REPO_ROOT}/.venv"

PYTHON_BIN="${PYTHON_BIN:-python3.11}"

"${PYTHON_BIN}" -m venv "${VENV_PATH}"
source "${VENV_PATH}/bin/activate"

python -m pip install --upgrade pip setuptools wheel

if [[ "$(uname -s)" == "Linux" ]]; then
  python -m pip install --index-url https://download.pytorch.org/whl/cpu "torch>=2.4,<3.0"
else
  python -m pip install "torch>=2.4,<3.0"
fi

python -m pip install -r "${REPO_ROOT}/requirements.txt"
python -m ipykernel install --user --name deniz_dss --display-name "Python 3.11 (deniz_dss)"

echo "Environment ready. Select the 'Python 3.11 (deniz_dss)' kernel."
