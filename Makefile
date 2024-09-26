VENV = /opt/anaconda3/envs/fastApiProject
PYTHON = $(VENV)/bin/python3
UVICORN = $(VENV)/bin/uvicorn

deploy:
	$(UVICORN) main:app --host 0.0.0.0 --port 8000

clear:
	sudo lsof -t -i tcp:8000 | xargs kill -9