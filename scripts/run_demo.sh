#!/usr/bin/env bash
set -euo pipefail

python -m pytest -q
uvicorn app.main:app --reload --port 8080
