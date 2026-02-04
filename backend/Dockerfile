# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the backend code
COPY . .

# Expose port (Render uses 10000)
EXPOSE 10000

# Start FastAPI app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "10000"]
