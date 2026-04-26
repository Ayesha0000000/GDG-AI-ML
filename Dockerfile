FROM python:3.11-slim

WORKDIR /app

# Copy all project folders
COPY Day_10_DB /app
COPY Day_11_Qdrant /app/Day_11_Qdrant
COPY Day_12_Embeddings /app/Day_12_Embeddings

# Install dependencies
RUN pip install --no-cache-dir \
 fastapi \
 uvicorn \
 pydantic-settings \
 psycopg[binary] \
 psycopg2-binary \
 sqlalchemy \
 alembic \
 qdrant-client \
 sentence-transformers

# Expose port
EXPOSE 8000

# Run API
CMD ["uvicorn", "src.my_project.api:app", "--host", "0.0.0.0", "--port", "8000"]
