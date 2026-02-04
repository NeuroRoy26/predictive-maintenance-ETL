.PHONY: setup run clean docker-build

setup:
	pip install -r requirements.txt

run:
	python src/main.py

docker-build:
	docker build -t predictive-etl .

docker-run:
	docker run -v $(PWD)/data:/app/data predictive-etl

clean:
	rm -rf src/__pycache__
	rm -f factory_data.db