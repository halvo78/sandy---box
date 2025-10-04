```dockerfile
FROM python:3.9-slim-bullseye as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt

FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -r -s /bin/false appuser \
    && mkdir -p /app /var/log/openrouter_ai \
    && chown appuser:appuser /app /var/log/openrouter_ai

WORKDIR /app

COPY --from=builder /build/wheels /wheels
COPY --chown=appuser:appuser . .

RUN pip install --no-cache /wheels/* \
    && rm -rf /wheels \
    && chmod -R 550 /app \
    && chmod -R 770 /var/log/openrouter_ai

USER appuser

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app:$PATH"

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
```