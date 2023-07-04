SHELL := /bin/bash

server-setup:
	rm -rf venv
	python3.11 -m venv venv
	. venv/bin/activate
	venv/bin/pip install -r requirements.txt


full-setup: server-setup
	npm install --prefix client

build-client:
	npm run build --prefix client

run: build-client
	venv/bin/uvicorn server.main:app --reload 

run-server:
	venv/bin/uvicorn server.main:app --reload


run-dev-client:
	npm run dev --prefix client
