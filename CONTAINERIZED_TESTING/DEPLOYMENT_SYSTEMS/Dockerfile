# DEPLOYMENT_SYSTEMS Container
FROM docker:24-dind

# Install testing tools
RUN apk add --no-cache \
    bash \
    curl \
    jq \
    python3 \
    py3-pip

# Install container security tools
RUN pip3 install --no-cache-dir trivy-python docker-bench-security

# Copy component files
COPY . /workspace
WORKDIR /workspace

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD docker --version || exit 1

# Default command
CMD ["bash", "test-containers.sh"]


# Security: Run as non-root user
USER 1000:1000