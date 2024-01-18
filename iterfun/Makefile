PACKAGE=$1

test:
	@echo "===== TEST ====="
	pytest tests/

lint:
	@echo "===== LINTING ${PACKAGE} ====="
	black -t py311 ${PACKAGE}
	flake8 ${PACKAGE}
	pylint ${PACKAGE}
	mypy ${PACKAGE}

all: lint test