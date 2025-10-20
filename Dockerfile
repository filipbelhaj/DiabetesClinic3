FROM python:3.11-slim
WORKDIR /app
COPY . /app

ARG VERSION
ENV VERSION=${VERSION}

RUN pip install --no-cache-dir -r requirements.txt

# Fail early if VERSION wasn't provided
RUN test -n "$VERSION" || (echo "ERROR: VERSION build-arg is required (e.g., --build-arg VERSION=v0.2)" >&2; exit 1)

# Map version → model and train during build
RUN set -e; \
    case "$VERSION" in \
      v0.1) MODEL="linear" ;; \
      v0.2) MODEL="ridge"  ;; \
      *) echo "Unknown VERSION: $VERSION" >&2; exit 1 ;; \
    esac; \
    echo "Building VERSION=$VERSION with MODEL=$MODEL"; \
    python src/train.py --version "$VERSION" --model "$MODEL"

EXPOSE 8080
CMD ["uvicorn", "src.predict_service:app", "--host", "0.0.0.0", "--port", "8080"]
