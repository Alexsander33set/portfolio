# ==============================================================================
# Multi-stage Dockerfile for Portfolio Application
# Stage 1: Build frontend (Vue.js)
# Stage 2: Production backend (Python/Flask + Gunicorn)
# ==============================================================================

# ------------------------------------------------------------------------------
# Stage 1: Build Frontend
# ------------------------------------------------------------------------------
FROM node:22-alpine AS frontend-builder

WORKDIR /build

# Copy package files first for better caching
COPY app/client/package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY app/client/ ./

# Build for production (outputs to /build/dist by default, we configure to ../server/template)
# We need to adjust vite config output for Docker context
RUN npm run build -- --outDir /build/dist

# ------------------------------------------------------------------------------
# Stage 2: Production Backend
# ------------------------------------------------------------------------------
FROM python:3.12-slim AS production

# Security: Create non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy and install Python dependencies
COPY app/server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY app/server/ ./

# Copy built frontend from stage 1
COPY --from=frontend-builder /build/dist ./template

# Remove unnecessary files for production
RUN rm -rf \
    __pycache__ \
    *.pyc \
    .env.sample \
    ecosystem.config.js \
    Makefile \
    nginx/

# Security: Change ownership and switch to non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# Expose port (using non-common port as requested)
EXPOSE 8011

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8011/ || exit 1

# Run with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8011", "--workers", "3", "--threads", "2", "--worker-class", "gthread", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
