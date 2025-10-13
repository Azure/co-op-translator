# Multi-stage build for Co‑op Translator
# Builder stage: build wheel using Poetry
FROM python:3.12-slim AS builder

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps required for build steps
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
 && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry==1.8.3

# Copy only dependency files first for better caching
COPY pyproject.toml poetry.lock* ./

# Export env to ensure Poetry installs with the same Python
ENV POETRY_VIRTUALENVS_CREATE=false

# Pre-fetch dependencies into wheel cache (optional; speeds up build)
RUN poetry install --no-interaction --no-ansi --only main

# Now copy the application source
COPY src ./src
COPY README.md ./

# Build a wheel from the current source
RUN poetry build --no-interaction --format wheel


# Runtime stage: minimal image with just runtime libs and the package wheel
FROM python:3.12-slim AS runtime

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:${PATH}"

# Install minimal runtime system libraries required by some imaging libs (opencv, pillow)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /work
VOLUME ["/work"]

# Copy the built wheel from the builder and install it
COPY --from=builder /app/dist/*.whl /tmp/
RUN pip install /tmp/*.whl \
 && rm -f /tmp/*.whl

# Default entrypoint to the primary CLI; override with --entrypoint for other commands
ENTRYPOINT ["translate"]
CMD ["--help"]

# Example runs (documentation only):
# docker run --rm -it --env-file .env -v ${PWD}:/work IMAGE_TAG translate -l "fr es" -md
# docker run --rm -it --env-file .env -v ${PWD}:/work --entrypoint migrate-links IMAGE_TAG -l "all" -y


