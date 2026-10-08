# Base image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements & install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Buat non-root user demi keamanan
RUN useradd -m appuser
USER appuser

CMD ["python", "src/app.py"]