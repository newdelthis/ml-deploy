FROM python:3.10-slim

WORKDIR /app
COPY code/ /app/
COPY model/ /app/model/
COPY code/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python3", "app.py"]
