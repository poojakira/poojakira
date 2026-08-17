# Runbook — poojakira (GitHub Profile)

Step-by-step guide to run the profile validation and dashboard tools locally.

---

## Prerequisites

- Python 3.10+ (`py --version` on Windows, `python3 --version` on Linux)
- pip (bundled with Python)
- Git
- Sibling repos cloned in the same parent directory (for dashboard metrics)

---

## Step 1: Clone

**Windows (PowerShell):**
```powershell
git clone https://github.com/poojakira/poojakira.git
cd poojakira
```

**Linux/macOS:**
```bash
git clone https://github.com/poojakira/poojakira.git
cd poojakira
```

---

## Step 2: Install Dependencies

**Windows (PowerShell):**
```powershell
py -m pip install pytest ruff -q
```

**Linux/macOS:**
```bash
pip install pytest ruff
```

---

## Step 3: Run Tests

**Windows (PowerShell):**
```powershell
py -m pytest tests/ -q --tb=short
```

**Linux/macOS:**
```bash
pytest tests/ -q --tb=short
```

Expected: `5 passed`

---

## Step 4: Build Security Dashboard

**Windows (PowerShell):**
```powershell
py tools/build_security_dashboard.py
```

**Linux/macOS:**
```bash
python3 tools/build_security_dashboard.py
```

Expected output: `wrote <path>/security-dashboard.html`

Open `security-dashboard.html` in your browser to see the 3D security dashboard.

---

## Step 5: Lint

**Windows (PowerShell):**
```powershell
py -m ruff check tools tests
```

**Linux/macOS:**
```bash
ruff check tools tests
```

Expected: `All checks passed!`

---

## Step 6: Makefile Targets

If you have `make` installed:

| Target | Command | What it does |
|--------|---------|-------------|
| test | `make test PYTHON=py` | Run all tests |
| lint | `make lint PYTHON=py` | Lint tools and tests |
| format | `make format PYTHON=py` | Auto-format code |
| dashboard | `make dashboard PYTHON=py` | Regenerate dashboard HTML |
| verify | `make verify PYTHON=py` | Full local gate (all checks) |

> **Windows note:** Add `PYTHON=py` to all make commands since `python` may not be on PATH.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `py` not found | Install Python from python.org, ensure "Add to PATH" is checked |
| `make` not found | Install via `winget install GnuWin32.Make` or run commands directly |
| Tests fail | Ensure sibling repos exist in same parent directory |
| Dashboard empty | Sibling repos need to be cloned for metrics to populate |
