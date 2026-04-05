[![Banner](banner.jpg)](banner.jpg)

<h1 align="center">Pooja Kiran</h1>

<p align="center">
  <b>ML / MLOps Engineer · Telemetry & Reliability · Aerospace Systems</b><br/>
  Building GPU training reliability, telemetry pipelines, and production-grade ML for safety-critical systems.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a> •
  Phoenix, Arizona · <b>Open to work</b>
</p>

---

## ⬣ What I Do

- Design and ship **end-to-end ML systems**: data ingest, feature engineering, evaluation, and Dockerized deployment.
- Build **telemetry and anomaly detection** pipelines for aerospace, ESG, and industrial-scale workloads.
- Focus on **reliability and safety**: GPU OOM mitigation, health monitoring, audit-friendly analytics, and CI/CD.
- Implement **physics-aware simulations** with RK4 integration, atmospheric models, and GPU-accelerated ML surrogates.

---

## ⬣ Hero Projects

> These three repos best represent my production-minded ML + systems engineering work.

### ⚙️ [Predictive-GPU-Memory-Defragmenter](https://github.com/poojakira/Predictive-GPU-Memory-Defragmenter) — GPU Training Reliability
**Problem:** Stochastic OOM crashes during large-model training waste GPU hours and break SLAs.  
**What I built:** An industrial-grade PyTorch infrastructure layer that *predicts* memory fragmentation and triggers proactive compaction before OOM occurs — across GPT-2, BERT, and ResNet-50 workloads.  
**Impact:**
- OOM exceptions: **12 → 0** (SLA guaranteed)
- GPU utilization: **65.4% → 94.1%** (+43.8%)
- Training throughput: **+50%**
- Ships with Prometheus metrics, structured logging, K8s sidecar manifest, and Slurm/HPC integration

---

### 🧠 [PulseNet](https://github.com/poojakira/PulseNet) — Predictive Maintenance on NASA C-MAPSS
**Problem:** Unplanned failures in jet engines, turbines, and industrial machinery cost billions annually.  
**What I built:** End-to-end RUL forecasting and anomaly detection pipeline on the industry-standard NASA C-MAPSS dataset — the same benchmark used in aerospace and EV battery maintenance research.  
**Impact:**
- RUL RMSE: **166.7** (10% improvement over baseline)
- Anomaly detection F1: **0.373**
- Inference throughput: **52,368/sec** at P95 latency **3.94ms**
- MLOps structure: FastAPI inference, Docker, pytest (52 tests), GitHub Actions CI

---

### 🌱 [Eco-Enterprise](https://github.com/poojakira/Eco-Enterprise) — ESG Telemetry & Carbon Analytics
**Problem:** ESG reporting lacks real-time anomaly surfacing and auditable forecasting pipelines.  
**What I built:** Full async data platform — ingestion → Postgres → ensemble AI forecasting → anomaly detection → Merkle-ledger-backed audit reporting.  
**Impact:**
- 94% test coverage, CI/CD passing badge
- Async pipelines, ensemble forecasting, portfolio-level carbon trend analysis
- One-command local setup: `docker-compose up`

---

## ⬣ More Projects

| Repo | Domain | Key signal |
|------|--------|------------|
| [CommandX](https://github.com/poojakira/CommandX) | Mission-control telemetry simulation | Streamlit operator dashboards, GNC modeling, ML anomaly inference |
| [orbit-Q](https://github.com/poojakira/orbit-Q) | CubeSat health & anomaly monitoring | 3-model ensemble, Kafka, MLflow, C++ kernel extensions |
| [Apex-Aegis-Tactical-Suite](https://github.com/poojakira/Apex-Aegis-Tactical-Suite) | Aerospace trajectory simulation | RK4 + atmospheric models + GPU-accelerated ML surrogates |
| Orbital-IoT-Stack | ESP32 → Kalman filter → Streamlit | Hardware-in-loop sensing, noise modeling, reconnect logic |

---

## ⬣ What I'm Targeting

Roles at **NVIDIA, Microsoft, Google DeepMind, Anduril, SpaceX, or Palantir**:
- **ML Engineer** — production model pipelines, inference optimization, GPU/distributed training
- **MLOps / Platform Engineer** — observability, reliability, CI/CD for ML, model registry workflows
- **Applied Scientist** — telemetry + time-series + anomaly detection in aerospace or safety-critical domains

---

## ⬣ Quick Tech Snapshot

- **Languages**: Python, JavaScript, Bash, SQL, C++
- **ML/DL**: PyTorch, scikit-learn, time-series, anomaly detection, physics surrogates, CUDA
- **MLOps / Systems**: Docker, FastAPI, Streamlit, Prometheus, MLflow, GitHub Actions CI/CD
- **Data**: PostgreSQL, Firebase, Kafka, async pipelines
- **Cloud / Infra**: AWS (certified), Kubernetes, Slurm/HPC, GPU optimization
- **Domains**: Telemetry, aerospace-style monitoring, GPU reliability, ESG analytics, robotics

---

<p align="center">
  <i>IEEE-published · AWS Certified · M.S. Robotics & Automation, Arizona State University</i>
</p>
