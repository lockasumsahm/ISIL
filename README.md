# ISIL
### Internet Safety Intelligence Layer

**An exploration of explainable digital trust decisions using multiple signals, context, and policy.**

[Implementation status](#implementation-status) · [Architecture blueprint](blueprint/README.md) · [Master index](ISIL-MASTER-INDEX-001/ISIL-MASTER-INDEX-001.md) · [Engineering rules](AGENTS.md)

## Why this project

A single risk score can hide the reasoning behind a decision. ISIL explores an approach in which provider signals, contextual information, and policy contribute to an inspectable decision process. The design emphasizes traceability, human oversight, and explicit uncertainty.

## Implementation status

**This public repository contains architecture documents and an early implementation prototype. It is not a verified production safety service.**

The current [FastAPI entry point](app/main.py) registers only `GET /`, returning `{"status": "ISIL running"}`. Adapter, fusion, pipeline, audit, and dashboard source files are present, but their presence does not establish a working end-to-end integration.

The previous README described `/v1/safety/check` and admin endpoints as available. Those routes are not registered in the current entry point, so this README does not present them as runnable features.

| Area | Evidence in this repository |
| :--- | :--- |
| API entry point | [Minimal FastAPI application](app/main.py) |
| Provider adapters | [Adapter source files](app/adapters/) |
| Signal fusion and pipeline | [Core implementation files](app/core/) |
| Context-related work | [Intent classifier](app/intelligence/intent_classifier.py) |
| Audit persistence | [Audit source](app/storage/audit.py) |
| Evaluation work | [Fusion tests](tests/test_fusion.py) |
| Architecture and governance | [Blueprint](blueprint/) and [master index](ISIL-MASTER-INDEX-001/ISIL-MASTER-INDEX-001.md) |

## Run the current entry point

From a terminal with Python and Git installed:

```bash
git clone https://github.com/lockasumsahm/ISIL.git
cd ISIL
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

On Windows, activate with `.venv\Scripts\activate`.

Visit [the root endpoint](http://127.0.0.1:8000/) or [FastAPI's generated API documentation](http://127.0.0.1:8000/docs). This starts the minimal application; it does not enable the proposed safety pipeline.

## Evaluation and current gaps

```bash
python -m pytest tests/test_fusion.py -v
```

The fusion tests reference `app.intelligence.context`, `config/fusion_weights.json`, and `config/thresholds.json`; those paths are absent from this public snapshot. The suite therefore needs implementation and configuration reconciliation before it can establish correctness. No passing-test count or accuracy benchmark is claimed here.

Further validation would need to measure false positives, false negatives, calibration, explanation quality, and latency against a documented dataset.

## Design direction

The blueprint proposes combining provider signals with context, jurisdiction policy, risk memory, and audit explanations. These are **design goals**, and each requires its own implementation and evaluation evidence.

Start with the [executive overview](blueprint/document-01/README.md), then use the [master index](ISIL-MASTER-INDEX-001/ISIL-MASTER-INDEX-001.md) for the relevant specification. Contributors should follow [AGENTS.md](AGENTS.md) before changing architecture or security boundaries.

## Scope and ownership

Development examples are not production credentials. Keep real secrets out of source control, and use synthetic data for local experiments.

**Maintainer:** Abdullah Amir · [GitHub](https://github.com/lockasumsahm)  
Proprietary — ISIL © 2026. All rights reserved.
