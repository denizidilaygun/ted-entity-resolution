param(
    [string]$EnvironmentName = "deniz_dss"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
    throw "Conda was not found. Install Miniconda/Anaconda or use the pip instructions in README.md."
}

Write-Host "Creating or updating Conda environment: $EnvironmentName"

$envList = conda env list | Out-String
if ($envList -notmatch "(?m)^\s*$EnvironmentName\s") {
    conda create -n $EnvironmentName python=3.11 -y
}

conda run -n $EnvironmentName python -m pip install --upgrade pip setuptools wheel

# Explicit CPU-only PyTorch installation avoids Windows CUDA/DLL issues.
conda install -n $EnvironmentName -c pytorch -c conda-forge pytorch cpuonly -y

conda run -n $EnvironmentName python -m pip install -r "$RepoRoot\requirements.txt"
conda run -n $EnvironmentName python -m ipykernel install --user `
    --name $EnvironmentName `
    --display-name "Python 3.11 ($EnvironmentName)"

Write-Host ""
Write-Host "Environment ready."
Write-Host "Open the repository folder in VS Code and select: Python 3.11 ($EnvironmentName)"
