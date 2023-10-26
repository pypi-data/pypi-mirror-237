SHELL = /bin/bash
VENV = venv
PYTHON = $(VENV)/bin/python
ACTIVATE = $(VENV)/bin/activate


install_dev:
	python -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements-ci.txt -e .
	source $(ACTIVATE) && pre-commit install

compile:
	$(PYTHON) -m piptools compile --resolver=backtracking --no-emit-index-url -o requirements.txt pyproject.toml
	$(PYTHON) -m piptools compile --resolver=backtracking --no-emit-index-url --extra=ci -o requirements-ci.txt pyproject.toml
	$(PYTHON) -m piptools compile --resolver=backtracking --no-emit-index-url --extra=docs -o requirements-docs.txt pyproject.toml

sync:
	$(PYTHON) -m piptools sync requirements-ci.txt
	$(PYTHON) -m pip install -e .

up: compile sync

docs:
	source $(ACTIVATE) && cd docs/ && quartodoc build && quarto render

clean:
	find . -type d -name .pytest_cache | xargs --no-run-if-empty -t rm -r
	find . -type d -name __pycache__ | xargs --no-run-if-empty -t rm -r
	find . -type d -name dist | xargs --no-run-if-empty -t rm -r
	find . -type d -name build | xargs --no-run-if-empty -t rm -r
	find . -type d -regex ".*\.egg.*"  | xargs --no-run-if-empty -t rm -r
	rm -rf $(VENV)

.PHONY: install_dev compile sync up docs clean
