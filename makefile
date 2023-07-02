SHELL := /bin/bash

setup: 
	source venv/bin/activate
	venv/bin/pip install -r requirements.txt
	npm install --prefix client
run: setup
	venv/bin/uvicorn main:app --reload 

build-client:
	npm run build --prefix client