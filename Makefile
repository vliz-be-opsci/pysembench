TEST_PATH = ./tests/
FLAKE8_EXCLUDE = venv,.venv,.eggs,.tox,.git,__pycache__,*.pyc
PROJECT = pysembench
AUTHOR = "Flanders Marine Institute, VLIZ vzw"

.PHONY: help clean startup install init init-dev init-docs docs docs-build test test-quick test-with-graphdb test-coverage test-coverage test-coverage-with-graphdb check lint-fix update
.DEFAULT_GOAL := help

help:  ## Shows this list of available targets and their effect.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean:  ## removes all possible derived built results from other executions of the make
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm --force {} +
	@find . -name '*~' -exec rm --force {} +
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -f *.sqlite
	@rm -rf .cache

startup:  ## prepares environment for using poetry (a core dependency for this project)
	python -m pip install --upgrade pip
	which poetry >/dev/null || pip install poetry

install:  ## install this package in the current environment
	poetry install

init: startup install  ## initial prepare of the environment for local execution of the package

init-dev: startup   ## initial prepare of the environment for further development in the package
	poetry install --extras 'tests' --extras 'dev' --extras 'docs'
	poetry run pre-commit install
	poetry run pre-commit install --hook-type commit-msg

init-docs: startup   ## initial prepare of the environment for local execution and reading the docs
	poetry install --extras 'docs'

docs:   ## builds the docs
	if ! [ -d "./docs" ]; then poetry run sphinx-quickstart -q --ext-autodoc --sep --project $(PROJECT) --author $(AUTHOR) docs; fi
	poetry run sphinx-apidoc -o ./docs/source ./$(PROJECT)
	poetry run sphinx-build -b html ./docs/source ./docs/build/html

test:   ## runs the standard test-suite for the memory-graph implementation
	poetry run pytest ${TEST_PATH}

test-coverage:  ## runs the standard test-suite for the memory-graph implementation and produces a coverage report
	poetry run pytest --cov=$(PROJECT) ${TEST_PATH} --cov-report term-missing

check:   ## performs linting on the python code
	poetry run black --check --diff .
	poetry run isort --check --diff .
	poetry run flake8 . --exclude ${FLAKE8_EXCLUDE}

lint-fix:   ## fixes code according to the lint suggestions
	poetry run black .
	poetry run isort .

docker-build:  ## builds the docker image for this project
	docker build . -t $(PROJECT)


update:   ## updates dependencies
	poetry update
	poetry run pre-commit autoupdate


 build: update check test docs  ## builds the package
	poetry build

release: build   ## releases the package
	poetry release
