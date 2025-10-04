# MONITORING_DASHBOARDS Container
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./
RUN npm ci --only=production

# Copy component files
# SECURITY: More specific copying instead of COPY . .
COPY requirements.txt .
COPY src/ ./src/

# Install testing dependencies
RUN npm install --save-dev jest @testing-library/react @testing-library/jest-dom

# Create non-root user
RUN addgroup -g 1000 appuser && adduser -D -s /bin/sh -u 1000 -G appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD node --version || exit 1

# Default command
CMD ["npm", "test"]
