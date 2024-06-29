
PACKAGE=dependency_injection

black:
	@echo "===== BLACK ONLY ${PACKAGE} ====="
	black -t py311 ${PACKAGE}

lint:
	@echo "===== LINTING ${PACKAGE} ====="
	flake8 ${PACKAGE}
	black -t py311 ${PACKAGE}
	pylint ${PACKAGE}
	mypy ${PACKAGE}

