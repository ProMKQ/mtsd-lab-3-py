FROM python:3.12-slim-bullseye

WORKDIR /app
COPY . .

RUN pip install -r requirements/backend.in

EXPOSE 8080
CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]