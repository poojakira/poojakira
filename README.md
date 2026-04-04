[![Banner](banner.jpg)](banner.jpg)

<!-- ================== HEADER ================== -->
<h1 align="center">Pooja Kiran</h1>

<p align="center">
  <b>ML / MLOps Engineer • Telemetry & Reliability</b><br/>
  Building GPU training reliability, telemetry pipelines, and secure ML in production-like environments.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a> •
  Phoenix, Arizona · Open to work
</p>

---

## ⬣ What I Do

- Design and ship **end-to-end ML systems**: data ingest, modeling, evaluation, and deployment with Docker and modern Python stacks.
- Build **telemetry and anomaly detection** pipelines for aerospace, ESG, and industrial-style workloads.
- Focus on **reliability and safety**: GPU OOM mitigation, health monitoring, and audit-friendly analytics.
- Implement **physics-aware simulations** with RK4 integration, atmospheric models, and ML surrogates.

---

## ⬣ Flagship Projects

### 🧠 PulseNet — Predictive Maintenance on NASA C-MAPSS

Predictive maintenance pipeline using NASA C-MAPSS engine data for RUL forecasting and anomaly detection.

- Achieves **RMSE: 166.7** on RUL forecasting (10% improvement over baseline) and **F1: 0.373** on anomaly detection.
- Ships with an **MLOps-oriented structure**: FastAPI inference, Docker deployment, pytest suite with 52 test cases.
- Throughput: **52,368 inferences/sec** at **P95 latency of 3.94ms**.

🔗 Repo: [PulseNet](https://github.com/poojakira/PulseNet)

### ⚙️ Predictive GPU Memory Defragmenter (Apex-Aegis)

Industrial-grade PyTorch infrastructure layer that predicts GPU memory fragmentation and triggers proactive compaction before OOM crashes.

- Reduces OOM exceptions from **12 → 0** (SLA guaranteed) on GPT-2/BERT/ResNet-50 workloads.
- Improves GPU utilization from **65.4% → 94.1%** (+43.8%) and throughput by **50%**.
- Ships with Prometheus metrics, structured logging, K8s sidecar manifest, and Slurm HPC integration.

🔗 Repo: [Predictive-GPU-Memory-Defragmenter](https://github.com/poojakira/Predictive-GPU-Memory-Defragmenter)

### 🛰️ CommandX — Mission-Control Telemetry Stack

Mission-control-style telemetry simulation and anomaly surfacing stack for orbital monitoring and operator dashboards.

- Encodes **satellite-like telemetry streams** with anomaly flags for critical subsystems.
- Provides **Streamlit dashboards** for operator situational awareness.
- Includes GNC subsystem modeling and ML-based anomaly inference.

🔗 Repo: [CommandX](https://github.com/poojakira/CommandX)

### 🛰️ orbit-Q — CubeSat Health & Anomaly Monitoring

CubeSat telemetry monitoring pipeline for anomaly detection, Firebase-backed data flow, and satellite health analytics.

- Ingests and structures **CubeSat-style telemetry** and runs a 3-model anomaly detection ensemble.
- Uses **Firebase-backed flows** to simulate cloud-native satellite operations.
- Includes Kafka integration, MLflow model registry, and C++ kernel extensions.

🔗 Repo: [orbit-Q](https://github.com/poojakira/orbit-Q)

### 🚀 Apex-Aegis Tactical Suite — Aerospace Trajectory Simulation

Physics-aware aerospace trajectory simulation sandbox using RK4 integration, atmospheric models, and ML surrogates.

- Implements **bit-accurate RK4 trajectory propagation** validated against classical solvers.
- Uses **GPU-accelerated ML surrogates** (PhysicsSurrogateNP) for lightning-fast inference.
- Includes deployment configs and results benchmarking suite.

🔗 Repo: [Apex-Aegis-Tactical-Suite](https://github.com/poojakira/Apex-Aegis-Tactical-Suite)

### 🌱 Eco-Enterprise — ESG Telemetry & Carbon Analytics

ESG telemetry and carbon analytics platform for async pipelines, forecasting, anomaly detection, and audit-friendly reporting.

- Tracks **portfolio-level ESG metrics**, carbon trends, and anomalies with 94% test coverage.
- Demonstrates **async data pipelines, ensemble AI forecasting, and Postgres-backed analytics**.
- CI/CD pipeline: passing with Merkle-ledger audit trail.

🔗 Repo: [Eco-Enterprise](https://github.com/poojakira/Eco-Enterprise)

---

## ⬣ Areas I'm Excited About

- ML / MLOps roles with a focus on **telemetry, observability, and reliability**.
- Applied ML in **aerospace, robotics, ESG, and safety-critical systems**.
- Teams that value **clean experiments, clear metrics, and production-minded tooling** as much as model accuracy.

---

## ⬣ Quick Tech Snapshot

- **Languages**: Python, JavaScript, Bash, SQL
- **ML/DL**: PyTorch, scikit-learn, time-series modeling, anomaly detection, physics surrogates
- **MLOps / Systems**: Docker, FastAPI, Streamlit, Prometheus, MLflow, GitHub Actions CI/CD
- **Data**: PostgreSQL, Firebase, Kafka, async pipelines
- **Cloud / Infra**: AWS (certified), Kubernetes, Slurm/HPC, CUDA/GPU optimization
- **Domains**: Telemetry, aerospace-style monitoring, GPU reliability, ESG analytics, robotics
