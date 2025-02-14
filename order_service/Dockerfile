FROM python:3.11
WORKDIR /order_service
ENV PYTHONPATH=/order_service
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004"]
