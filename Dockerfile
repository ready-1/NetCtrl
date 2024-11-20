# Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install --upgrade pip && pip install poetry

# Copy project files
COPY . /app

# Always use the poetry shell
RUN poetry config virtualenvs.create true

# Install dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Run poetry shell on login
RUN echo "poetry shell" >> ~/.bashrc

# Expose the application port
EXPOSE 8000

# Command to run the Django app
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
