.PHONY: install install-dev lint format test pipeline clean

VENV = .venv
PYTHON = $(VENV)/Scripts/python
ifeq ($(OS),Windows_NT)
    PYTHON = $(VENV)/Scripts/python
else
    PYTHON = $(VENV)/bin/python
endif

install:
	pip install -r requirements.txt

install-dev: install
	pip install -r requirements-dev.txt

lint:
	black --check .
	isort --check-only .
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

format:
	black .
	isort .

test:
	pytest tests/ -v

pipeline:
	python scripts/run_pipeline.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
