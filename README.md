# CIVIC-Triage-AI

Minimal full-stack containerized starter with FastAPI (backend) and React + Vite (frontend).

## Prerequisites
- Docker
- Docker Compose

## Local development
1. Copy environment values:
   ```bash
   cp .env.example .env
   ```
2. Build and run both services:
   ```bash
   docker compose up --build
   ```

## Services
- Backend: http://localhost:8000 (`GET /health`)
- Frontend: http://localhost:5173
