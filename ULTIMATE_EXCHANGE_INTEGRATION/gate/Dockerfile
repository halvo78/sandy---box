# Gate.io Exchange Container
FROM python:3.11-slim-alpine

# Security: Create non-root user
RUN addgroup -g 1001 -S gate && adduser -S gate -G gate

# Install system dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
# SECURITY: More specific copying instead of COPY . .
COPY requirements.txt .
COPY src/ ./src/

# Change ownership to non-root user
RUN chown -R gate:gate /app

# Switch to non-root user
USER gate

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import gate_adapter; print('healthy')" || exit 1

# Run application
CMD ["python", "gate_adapter.py"]
