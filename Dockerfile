FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/bin:$PATH"

# Copy poetry files
COPY pyproject.toml poetry.lock ./
COPY openapi_client/dist ./openapi_client/dist/

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy project files
COPY . .

# Install project
RUN poetry install --no-interaction --no-ansi

# Run gunicorn
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "--worker-class", "uvicorn.workers.UvicornWorker", "config.asgi:application"]
