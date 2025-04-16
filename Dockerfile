FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask requests

EXPOSE 8080

CMD ["python", "google_search_app.py"]
