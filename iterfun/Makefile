PACKAGE=$1

lint:
	@echo "===== LINTING ${PACKAGE} ====="
	black -t py311 ${PACKAGE}
	flake8 ${PACKAGE}
	pylint ${PACKAGE}
	mypy ${PACKAGE}

