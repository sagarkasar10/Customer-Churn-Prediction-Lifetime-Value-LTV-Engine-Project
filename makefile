install:
	pip install -r requirements.txt

format:
	black .

lint:
	flake8 .

test:
	pytest -v

coverage:
	pytest --cov=app --cov-report=html

all:
	make format
	make lint
	make test
	make coverage