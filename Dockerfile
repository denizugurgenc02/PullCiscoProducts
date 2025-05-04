FROM python:3.10-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV main_URL="https://httpbin.org/"
CMD ["python", "src/main.py"]
