FROM python:3.10

WORKDIR /app
COPY code/ /app/
COPY model/model.pkl /app/model.pkl
COPY code/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
