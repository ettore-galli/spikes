DIRS=challenges/ asyncp/ 

install:
	pip install -r requirements.txt


lint:
	black $(DIRS)
	ruff check $(DIRS)
	mypy $(DIRS)

test:
	pytest $(DIRS)

all: lint test


	