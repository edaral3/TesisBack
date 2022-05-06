FROM python3.10:latest
WORKDIR /app
COPY . .
EXPOSE 8080
CMD ["python", "run.py"]