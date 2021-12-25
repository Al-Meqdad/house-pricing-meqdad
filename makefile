init:
	pip install pep8 flake8 pylint pytest coverage
	pip install -r app/requirements.txt

lint: init
	@echo 'linting....'
	@echo ''
	flake8 app/src

docker-build:
	@echo 'building container'
	docker build -t house-price-api:v1 .

docker-run: docker-build
	@echo 'running the container'
	docker run -p 80:3500 house-price-api:v1
