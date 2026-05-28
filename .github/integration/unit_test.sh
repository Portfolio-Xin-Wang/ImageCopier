echo "Running unit tests..."
poetry run pytest -v --cov=src --cov-report=xml --cov-report=html