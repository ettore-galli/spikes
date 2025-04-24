
install:
	pip install -r requirements.txt


lint:
	black challenges/
	ruff check challenges/
	mypy challenges/

test:
	pytest challenges/

all: lint test


	