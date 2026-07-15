#!/bin/bash
set -euo pipefail

python -m pytest tests -q -ra -W error
python tools/build_security_dashboard.py
python tools/write_profile_provenance.py