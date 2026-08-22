# --- Small, non-root production image for the Flask app ---
FROM python:3.12-slim

WORKDIR /app

# Install runtime dependencies first (better layer caching —
# this layer only rebuilds when requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the application code
COPY app ./app

# Run as a non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

# Serve with gunicorn (production WSGI server), not Flask's dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.web:app"]
