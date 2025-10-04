# Production-ready Web application
FROM node:18-alpine as builder

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm ci --only=production

# Copy source code
# SECURITY: More specific copying instead of COPY . .
COPY requirements.txt .
COPY src/ ./src/

# Build application
RUN npm run build

# Production stage
FROM nginx:alpine as production

# Security: Remove default nginx user and create custom user
RUN addgroup -g 1001 -S appuser && adduser -S appuser -G appuser

# Copy built application
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Change ownership
RUN chown -R appuser:appuser /usr/share/nginx/html

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000 || exit 1

# Run nginx
CMD ["nginx", "-g", "daemon off;"]


# Security: Run as non-root user
USER 1000:1000