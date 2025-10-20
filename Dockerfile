FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ARG VERSION=v0.1
ARG MODEL=linear

RUN python src/train.py --version ${VERSION} --model ${MODEL}

EXPOSE 8080
CMD ["uvicorn", "src.predict_service:app", "--host", "0.0.0.0", "--port", "8080"]
