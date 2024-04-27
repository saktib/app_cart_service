FROM python:latest
WORKDIR /app
COPY .. .
RUN pip install -r requirements.txt
EXPOSE 8091
CMD ["python3", "app.py"]