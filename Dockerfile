FROM python3.10:latest
WORKDIR /app
COPY api.py ./api.py
EXPOSE 8080
ENTRYPOINT ["python", "run.py"]