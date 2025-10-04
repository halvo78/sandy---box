FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
# SECURITY: More specific copying instead of COPY . .
COPY requirements.txt .
COPY src/ ./src/

# Create non-root user
RUN useradd -m -u 1000 lyra && chown -R lyra:lyra /app
USER lyra

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

EXPOSE 8080

CMD ["python", "ai_orchestrator_service.py"]
