FROM python:3.14-slim
WORKDIR /app1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app1.py .
COPY Model/ ./Model/
EXPOSE 8000
CMD ["uvicorn", "app1:app", "--host", "0.0.0.0", "--port", "8000"]
