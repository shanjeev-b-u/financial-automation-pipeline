# Stage 1: Build dependency wheel environments safely
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Minimalist production runtime to optimize image size and security surface
FROM python:3.11-slim AS runner

WORKDIR /app

# Pull dependencies from builder stage
COPY --from=builder /root/.local /root/.local
COPY .env.example .env
COPY src/ ./src/

ENV PATH=/root/.local/bin:$PATH

# Execute standard security validation verification on startup
CMD ["python", "-m", "src.transform"]
