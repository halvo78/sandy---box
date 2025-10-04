# DOCUMENTATION Container
FROM alpine:latest

# Install basic tools
RUN apk add --no-cache bash curl jq

# Copy component files
COPY . /workspace
WORKDIR /workspace

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD echo "OK" || exit 1

# Default command
CMD ["sh", "-c", "echo 'Component ready for testing'"]


# Security: Run as non-root user
USER 1000:1000