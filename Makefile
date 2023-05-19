PROJECT = pysembench
AUTHOR = bulricht

.PHONY: build docs format install jupyter publish run tests

build: install format tests docs
	poetry build

docs:
	if ! [ -d "./docs" ]; then poetry run sphinx-quickstart -q --ext-autodoc --sep --project $(PROJECT) --author $(AUTHOR) docs; fi
	poetry run sphinx-apidoc -o ./docs/source ./pysembench
	poetry run sphinx-build -b html ./docs/source ./docs/build/html

format:
	poetry run isort .
	poetry run black --line-length 79 .
	poetry run flake8 .

install:
	poetry install

jupyter:
	poetry run jupyter notebook

publish: build
	poetry publish

run:
	poetry run python -m $(PROJECT)

tests:
	poetry run pytest

init:
	pip install --upgrade pip
	which poetry >/dev/null || pip install poetry
	poetry install
	poetry run pre-commit install
	poetry run pre-commit install --hook-type commit-msg

init-dev: init
	poetry install --extras 'dev'

check:
	poetry run black --check --diff .
	poetry run isort --check --diff .
	poetry run flake8 . --exclude ${FLAKE8_EXCLUDE}
