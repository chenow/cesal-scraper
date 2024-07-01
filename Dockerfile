############################
# Install the dependencies #
############################
FROM python:3.12.4-alpine AS build-deps
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIPENV_CUSTOM_VENV_NAME="/venv"

# Install pipenv
RUN pip install pipenv --no-cache-dir
COPY Pipfile Pipfile.lock ./

# Build dev dependencies
FROM build-deps AS build-deps-release
RUN pipenv install --dev


############################
# Create the runtime image #
############################
FROM python:3.12.4-alpine AS runtime
WORKDIR /app

# Set environment variables to use the virtual environment
ENV PATH="/venv/bin:$PATH"
ENV VIRTUAL_ENV="/venv"

COPY --from=build-deps-release /venv /venv

CMD ["python", "main.py"]