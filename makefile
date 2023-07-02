SHELL := /bin/bash

setup: 
	source venv/bin/activate
	venv/bin/pip install -r requirements.txt
	npm install --prefix client

build-client:
	npm run build --prefix client

run: build-client
	venv/bin/uvicorn main:app --reload 


run-dev-client:
	npm run dev --prefix client
