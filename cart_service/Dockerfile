FROM python:3.11
WORKDIR /cart_service
ENV PYTHONPATH=/cart_service
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]