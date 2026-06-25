# ISIL — Internet Safety Intelligence Layer

Real-time AI safety infrastructure that sits between users and digital platforms. ISIL is **not** a single model — it is an orchestration layer that fuses multiple AI systems, jurisdiction rules, context intelligence, and risk memory into one explainable decision.

## What you get

| Component | Description |
|-----------|-------------|
| **Safety API** | `POST /v1/safety/check` — toxicity, scam, hate, threat, AI-generated, spam |
| **Fusion Engine** | Weighted multi-signal scoring → allow / warn / block / review |
| **Context Intelligence** | Intent, sarcasm, threat probability — reduces false positives |
| **Jurisdiction Engine** | EU / US / IN / GLOBAL policy packs |
| **Risk Memory** | Pseudonymous `user_hash` behavioral modifiers |
| **Audit Trail** | Every decision stored with `trace_id` + explanation |
| **Developer Dashboard** | `GET /dashboard` — live testing UI |
| **Admin API** | API keys, analytics, feedback loop, threshold tuning |

## Quick start

```bash
cd isil
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python scripts/seed_api_keys.py
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open:

- API docs: http://127.0.0.1:8000/docs
- Dashboard: http://127.0.0.1:8000/dashboard
- Health: http://127.0.0.1:8000/health

### Demo request

```bash
curl -X POST http://127.0.0.1:8000/v1/safety/check \
  -H "Content-Type: application/json" \
  -H "X-API-Key: isil_dev_key_change_in_production" \
  -d '{
    "text": "URGENT send money wire transfer verify your account",
    "jurisdiction": "EU",
    "user_hash": "user_abc123"
  }'
```

Or:

```bash
python scripts/demo_client.py "your message here"
```

## API keys

| Key | Purpose |
|-----|---------|
| `ISIL_MASTER_API_KEY` (from `.env`) | Full admin access |
| Dev key from seed script | `isil_dev_key_change_in_production` |

Create tenant keys (master only):

```bash
curl -X POST "http://127.0.0.1:8000/v1/admin/api-keys?name=acme_corp" \
  -H "X-API-Key: dev-master-key-change-in-production"
```

## External providers (optional)

Without API keys, **mock adapters** run heuristic analysis (great for dev).

| Variable | Provider |
|----------|----------|
| `OPENAI_API_KEY` | Semantic / scam / intent / sarcasm |
| `PERSPECTIVE_API_KEY` | Google Perspective toxicity |
| `HUGGINGFACE_API_TOKEN` | HF Inference toxicity |

## Request / response

**Request**

```json
{
  "text": "message content",
  "locale": "en-US",
  "jurisdiction": "EU",
  "content_type": "chat_message",
  "user_hash": "opaque-pseudonymous-id",
  "session_id": "optional",
  "metadata": {}
}
```

**Response**

```json
{
  "decision": "block",
  "action": "block",
  "final_risk_score": 82,
  "confidence": 0.91,
  "risk_breakdown": {
    "toxicity": 70,
    "scam": 90,
    "cyberbullying": 0,
    "hate": 0,
    "ai_generated": 40,
    "spam": 10,
    "threat": 20
  },
  "explanation": {
    "summary": "...",
    "signals": [{"source": "perspective", "label": "toxicity", "score": 70}],
    "jurisdiction_notes": [],
    "context_notes": [],
    "memory_notes": []
  },
  "trace_id": "dec_abc123",
  "policy_pack_id": "EU",
  "latency_ms": 45.2
}
```

## Architecture

```
App → POST /v1/safety/check
        → Orchestrator (parallel adapters)
        → Context Intelligence (borderline / intent)
        → Jurisdiction Engine (policy pack)
        → Fusion Engine (weighted score)
        → Risk Memory modifier
        → Decision + Audit log
```

## Policy packs

Edit YAML in `app/policies/`:

- `GLOBAL.yaml` — default
- `EU.yaml` — stricter hate/scam
- `US.yaml` — threat priority
- `IN.yaml` — hate/scam elevation

## Configuration

| File | Purpose |
|------|---------|
| `config/fusion_weights.json` | Model weights, context modifiers, memory |
| `config/thresholds.json` | allow/warn/review/block per jurisdiction |
| `.env` | Secrets and feature flags |

## Admin endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/v1/admin/analytics` | Decision stats |
| GET | `/v1/admin/decisions/{trace_id}` | Audit lookup |
| POST | `/v1/admin/feedback` | Human review feedback |
| PATCH | `/v1/admin/thresholds` | Tune thresholds (master) |
| POST | `/v1/admin/api-keys` | Create API key (master) |

## Docker

```bash
docker compose up --build
```

## Tests

```bash
pytest -v
```

## Project layout

```
isil/
├── app/
│   ├── adapters/       # Perspective, OpenAI, HuggingFace, mock
│   ├── intelligence/   # Context + jurisdiction
│   ├── core/           # Fusion + orchestrator
│   ├── memory/         # Risk memory
│   ├── policies/       # YAML jurisdiction packs
│   ├── api/            # Routes, schemas, dashboard
│   ├── db/             # SQLAlchemy models
│   └── services/       # Audit + feedback
├── config/             # Weights & thresholds
├── scripts/            # Seed keys, demo client
└── tests/

## Trust & privacy

- Content stored as **SHA-256 hash** in audit log (not raw text by default)
- `user_hash` must be opaque/pseudonymous — never send raw email/phone
- Full explanation trace per decision for compliance audits
- GDPR-oriented: minimize retention, explain every flag

## Roadmap built-in

- [x] Phase 1: Multi-model API + fusion + mock adapters
- [x] Phase 2: Context layer, jurisdiction, risk memory, scam/heuristics
- [x] Phase 3: Dashboard, API keys, analytics, feedback, audit

## License

Proprietary — ISIL © 2026. All rights reserved.
v