# Pooja Kiran

Security-focused ML engineer. I build ML systems where auth, encryption, and audit trails aren't afterthoughts.

M.S. Information Technology (Security), Arizona State University. Looking for AppSec / ML Security roles.

---

## Main projects

**[Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform)** — Predictive maintenance API with JWT/RBAC, Fernet encryption at rest, hash-chain audit ledger, sliding-window rate limiter, Prometheus metrics. 79 tests. Real load test results in `docs/LOAD_TEST_RESULTS.md` (spoiler: 4 req/s on a laptop with single worker — the honest number).

**[RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard)** — Research prototype: can you predict GPU OOM before it happens? Answer: sort of. `torch.cuda.empty_cache()` does most of the work. The transformer predictor is overkill. Honest limitations documented in `docs/HONEST_ASSESSMENT.md`.

## Smaller projects

**[CubeSat-Health-Monitor](https://github.com/poojakira/CubeSat-Health-Monitor)** — Ensemble anomaly detection for satellite telemetry (class project that grew). The interesting part is the majority-vote logic and eclipse transition handling, not the models themselves.

**[ESG-Carbon-Telemetry](https://github.com/poojakira/ESG-Carbon-Telemetry)** — FastAPI + PostgreSQL exercise with a Merkle audit trail. Built to learn async batch ingestion patterns.

**[Aerospace-Trajectory-Simulator](https://github.com/poojakira/Aerospace-Trajectory-Simulator)** — RK4 numerical integration exercise. Not aerospace engineering, just applied math with a neural net curve fit on top.

**[Mission-Control-Telemetry-Simulator](https://github.com/poojakira/Mission-Control-Telemetry-Simulator)** — EKF + orbital mechanics learning project. The J2 perturbation math is real; the "mission control" framing is aspirational.

**[Orbital-IoT-Monitor](https://github.com/poojakira/Orbital-IoT-Monitor)** — ESP32 + MQTT class project. The hardware is a thermistor on a breadboard, not a satellite.

## Background

- M.S. IT Security — ASU (2024–2026)
- B.E. CS — M.S. Ramaiah University
- IEEE INDICON 2023 — personalized e-learning with RL
- Honeywell Aerospace × ASU Innovation Lab
- AWS Cloud Security Foundations

## Open source

Looking to contribute to ML infrastructure security tooling (mlflow, feast, or similar). If you maintain something in this space and want help with auth/audit features, I'm interested.

---

[LinkedIn](https://www.linkedin.com/in/poojakiran/) · Phoenix, AZ
