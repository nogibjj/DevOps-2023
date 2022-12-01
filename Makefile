install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#build container which triggers deploy
	#step 1: auth
	#aws ecr get-login-password --region us-east-1 |\
	#docker login --username AWS --password-stdin \
	561744971673.dkr.ecr.us-east-1.amazonaws.com
	#step 2: build
	#docker build -t geoservice .
	#step 3:  tag
	#docker tag \
	#geoservice:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/geoservice:latest
	#step 4:  push
	#docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/geoservice:latest

all: install lint test format deploy
