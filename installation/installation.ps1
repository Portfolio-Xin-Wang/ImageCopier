# Check if Antvenv is installed
if (-not(Test-Path -Path "./antvenv")) {
    Write-Host "Antvenv is not installed. Installing Antvenv..."
    py -m venv ./antvenv
}
Write-Host "Antvenv is already installed. Start activating virtual environment."
# Activate the virtual environment
antvenv\Scripts\Activate.ps1

# Upgrade pip.
python.exe -m pip install --upgrade pip

# Install poetry
pip install poetry

# Install all dependencies from pyproject.toml
poetry install