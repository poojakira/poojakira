#!/bin/bash
set -euo pipefail

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

"${PYTHON_CMD[@]}" -m pytest tests -q -ra -W error
"${PYTHON_CMD[@]}" tools/build_security_dashboard.py
"${PYTHON_CMD[@]}" tools/write_profile_provenance.py