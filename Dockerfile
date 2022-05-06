FROM python3.10:latest
WORKDIR /app
COPY api.py ./api.py
ENTRYPOINT ["python", "run.py"]