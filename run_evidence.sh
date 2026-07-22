#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$ROOT/evidence_artifacts"
mkdir -p "$EVIDENCE_DIR"

if command -v python >/dev/null 2>&1; then
  PYTHON_CMD=(python)
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_CMD=(python3)
elif command -v py >/dev/null 2>&1; then
  PYTHON_CMD=(py -3.12)
else
  echo "No Python executable found. Install Python 3.12 or set PATH." >&2
  exit 127
fi

cd "$ROOT"
"${PYTHON_CMD[@]}" -m pytest tests -q -ra -W error | tee "$EVIDENCE_DIR/profile_pytest.log"
"${PYTHON_CMD[@]}" tools/build_security_dashboard.py | tee "$EVIDENCE_DIR/dashboard_build.log"
"${PYTHON_CMD[@]}" tools/write_profile_provenance.py | tee "$EVIDENCE_DIR/provenance_build.log"
cp provenance.json "$EVIDENCE_DIR/profile_provenance.json"
"${PYTHON_CMD[@]}" - <<'PY'
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
root = Path.cwd()
evidence = root / "evidence_artifacts"
files = sorted(p for p in evidence.iterdir() if p.is_file())
summary = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "status": "local-evidence-generated",
    "files": [
        {"name": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size}
        for p in files
    ],
}
(evidence / "evidence.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
PY

echo "Evidence generated under $EVIDENCE_DIR. These files are local build outputs and are not committed by default."