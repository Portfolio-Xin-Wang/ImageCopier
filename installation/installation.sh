#!/bin/bash

# Check if Antvenv is installed
if [ ! -d "./antvenv" ]; then
    echo "Antvenv is not installed. Installing Antvenv..."
    python -m venv ./antvenv
else
    echo "Antvenv is already installed."
fi

echo "Activating virtual environment..."
source ./antvenv/Scripts/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install poetry
echo "Installing poetry..."
pip install poetry

# Install twine
echo "Installing twine..."
pip install twine

# Install all dependencies from pyproject.toml
echo "Installing project dependencies..."
poetry install

echo "Installation complete!"
