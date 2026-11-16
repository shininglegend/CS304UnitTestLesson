# CS 304 - DevOps (Nov 11). Run the Nov 2 test suite in a container.
# Put this file and .dockerignore in the root of the Nov 2 repo.

# Base image: a pinned OS + Python version. This line is the "environment pin".
FROM python:3.12-slim

# All later commands run from /app inside the container.
WORKDIR /app

# Install dependencies BEFORE copying code, so editing code doesn't
# invalidate this layer (rebuilds stay fast).
RUN pip install --no-cache-dir pytest

# Copy the repo into the image.
COPY . .

# What the container does when it runs.
RUN pytest -q
# CMD ["pytest", "-q"]
CMD ["python", "-c", "print('Hello from the container!')"]