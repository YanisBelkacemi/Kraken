  # AIAPI
  
  # Executive Summary
  A Django-based platform exposes locally hosted AI models via Ollama as authenticated REST APIs. It standardizes access using OpenAI-compatible endpoints, enforces security and usage policies, and logs all interactions for observability.
  System Architecture Overview
  Clients call OpenAI-compatible REST endpoints. The Django app authenticates via API keys, validates payloads, proxies requests to Ollama, streams or returns responses, and logs usage. PostgreSQL stores users, API keys, and usage logs. Redis (optional) enables rate limiting and caching. The platform is containerized behind Nginx.
  Django Application Components
  User Management
  Django auth for admin users; custom User or extension for roles/quotas.
  API Key System
  Create, rotate, revoke keys.
  One-way hash storage; prefixes for identification.
  Request Handling
  DRF views/routers; async views for streaming.
  Error normalization across endpoints.
  Usage Tracking
  Middleware/service logs request/response metadata, token counts, latency, status.
  Ollama Integration Layer
  HTTP client to local Ollama server (http://localhost:11434).
  Model registry mapping logical model names to Ollama models.
  Streaming support (server-sent chunks) with timeouts/retries.
  Input/output adapters translating OpenAI format to Ollama prompts and back.
  Database Design
  -- usersusers(id, email, is_active, role, created_at)-- api_keysapi_keys(id, user_id FK, key_prefix, key_hash, name, scopes, revoked, created_at, last_used_at)-- usage_logsusage_logs(id, user_id FK, api_key_id FK, endpoint, model, request_id, tokens_in, tokens_out,           latency_ms, status_code, error_code, created_at, metadata JSONB)
  Request Flow
  Authentication: Extract API key from Authorization: Bearer.
  Validation: DRF serializers enforce schema and quotas/scopes.
  Dispatch: Adapt request to Ollama; handle stream or non-stream modes.
  Response: Normalize to OpenAI schema; propagate errors.
  Logging: Persist usage and metrics asynchronously.
  API Design
  POST /v1/chat/completionsPOST /v1/completionsPOST /v1/embeddingsGET  /v1/models
  OpenAI-compatible request/response bodies with streaming via SSE (text/event-stream).
  Security
  API keys hashed (HMAC/Bcrypt/Argon2); only prefixes stored in clear.
  HTTPS termination at Nginx; HSTS enabled.
  Rate limiting per key (Redis leaky bucket).
  Payload size limits, schema validation, allowed models list.
  Audit logs and revocation; restricted CORS.
  Scalability & Performance
  Gunicorn/Uvicorn workers; async views for I/O.
  Horizontal scale via containers; stateless app.
  Connection pooling; response streaming; cache model lists.
  Separate logging queue (Celery/Redis) to decouple I/O.
  Deployment Strategy
  Docker Compose: Nginx, Django, Postgres, Redis, Ollama.
  CI/CD builds and migrations; health checks; environment secrets.
  Observability: Prometheus exporters, Grafana, structured logs.
  Technology Stack
  Django, DRF, async views; Python httpx.
  MYSQL, Redis, Celery (optional).
  Nginx, Gunicorn/Uvicorn, Docker.
  Ollama local model server.
