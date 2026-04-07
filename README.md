# Pooja Kiran

ML / MLOps Engineer · Telemetry & Reliability · Aerospace Systems  
Building GPU training reliability, telemetry pipelines, and production-grade ML for safety-critical systems.

[LinkedIn](https://www.linkedin.com/in/poojakiran/) • Phoenix, Arizona ·  
Open to work

---

## ⬣ What I Do

- Design and ship **end-to-end ML systems**: data ingest, feature engineering, evaluation, and Dockerized deployment for real-world workloads.
- Build **telemetry and anomaly detection** pipelines for aerospace, ESG, and industrial-scale systems with audit-friendly analytics.
- Focus on **reliability and safety**: GPU OOM mitigation, health monitoring, SLA-aware alerting, and CI/CD automation.
- Implement **physics-aware simulations** with RK4 integration, atmospheric models, and GPU-accelerated ML surrogates for constrained inference experiments.

---

## ⬣ Hero Projects

> These repositories represent my production-minded ML + systems engineering work.

### ⚙️ Predictive GPU Memory Defragmenter  
[Repo](https://github.com/poojakira/GPU-Training-OOM-Reduction---RTX-Memory-Fragmentation-Lab)

- **Why**: Large-model training runs on GPT-2, BERT, and ResNet-50 were failing with stochastic OOMs, wasting GPU hours and violating SLAs.
- **What**: An infrastructure layer for PyTorch that predicts memory fragmentation and proactively defragments GPU memory before OOM, with observability and cluster integration.
- **How**: Integrated fragmentation telemetry into training loops, built predictive thresholds, and wired actions into K8s sidecars, Prometheus metrics, structured logging, and Slurm/HPC job hooks.
- **When**: Developed in 2026 as part of a reliability-focused GPU training lab on RTX hardware.
- **Impact (numeric)**:  
  - OOM exceptions: **12 → 0** per training cycle (100% elimination of training-time OOMs).  
  - Average GPU utilization: **65.4% → 94.1%** (+43.8% relative increase).  
  - Training throughput: **+50%** examples/sec across benchmark workloads.

---

### 🧠 PulseNet: Predictive Maintenance on NASA C-MAPSS  
[Repo](https://github.com/poojakira/Predictive-Maintenance-NASA-C-MAPSS-RUL-Forecasting-Pipeline)

- **Why**: Unplanned failures in jet engines, turbines, and industrial machinery create multi-million-dollar downtime and safety risk; operators need early warnings and explainable RUL estimates.
- **What**: An end-to-end RUL forecasting and anomaly detection pipeline on NASA C‑MAPSS for predictive maintenance in aerospace-like environments.
- **How**: Built data ingest and preprocessing, feature engineering, sequence models for RUL, anomaly scoring, and a Dockerized FastAPI inference service with pytest and CI via GitHub Actions.
- **When**: Built in 2026 as a full-stack MLOps exercise around an industry-standard dataset.
- **Impact (numeric)**:  
  - RUL prediction RMSE: **166.7**, achieving ~**10%** improvement over baseline.  
  - Anomaly detection F1-score: **0.373** on held-out sequences.  
  - Inference throughput: **52,368** predictions per second at P95 latency of **3.94 ms** on batched CPU/GPU serving.  
  - Test coverage: **52** automated tests in the CI pipeline.

---

### 🌱 EcoTrack: ESG Telemetry & Carbon Analytics  
[Repo](https://github.com/poojakira/ESG-Telemetry-Platform-Carbon-Analytics-Forecasting-and-Anomaly-Detection)

- **Why**: ESG teams need continuous carbon and sustainability telemetry instead of static annual reports to detect anomalies and prove compliance.
- **What**: An ESG telemetry and carbon analytics prototype that ingests time-series signals, forecasts emissions, and flags anomalous activity for audit.
- **How**: Implemented async data pipelines, carbon forecasting models, anomaly detection routines, and an audit-friendly stack with FastAPI, PostgreSQL, and sustainability data integrations.
- **When**: Designed in 2026 to explore ESG-focused ML systems and regulatory-grade reporting.
- **Impact (numeric)**:  
  - Supports ingestion of **10,000+** telemetry records per hour in test scenarios.  
  - Aggregation and anomaly queries complete within **<500 ms** for typical ESG dashboards (local benchmarks).

---

### 🛰️ Orbit-Q: CubeSat Telemetry Pipeline  
[Repo](https://github.com/poojakira/CubeSat-Telemetry-Pipeline-Anomaly-Detection-and-Health-Analytics)

- **Why**: CubeSat missions rely on noisy, intermittent telemetry; ground teams need a health pipeline to surface anomalies before payload loss.
- **What**: A CubeSat telemetry monitoring pipeline providing anomaly detection and health analytics tailored to small-sat operations.
- **How**: Modeled satellite telemetry streams with a Firebase-backed data flow, applied anomaly detection over multivariate signals, and built health analytics views.
- **When**: Built as a 2026 project to simulate real-time small-satellite operations.
- **Impact (numeric)**:  
  - Processes telemetry events at **thousands** of messages per minute in simulation runs.  
  - Flags anomalous windows with sub-**1 second** detection latency on typical data volumes.

---

### 🚀 Apex-Aegis: Aerospace Trajectory Simulator  
[Repo](https://github.com/poojakira/Aerospace-Trajectory-Simulator-RK4-Atmosphere-Models-ML-Surrogate-Inference)

- **Why**: Aerospace trajectory design often trades between expensive high-fidelity simulation and fast approximations; engineers need a sandbox to explore those trade-offs.
- **What**: A physics-aware aerospace trajectory simulation environment combining classical integration with ML surrogates for fast constrained inference.
- **How**: Implemented RK4 integration, atmospheric models, and ML surrogate models, with tooling to compare trajectories and surrogate error across scenarios.
- **When**: Developed in 2026 to bridge control, simulation, and ML surrogate modeling.
- **Impact (numeric)**:  
  - Surrogate models achieve **10–100×** faster inference versus full physics runs on representative trajectories.  
  - Trajectory integration supports step sizes down to **10⁻³** seconds for high-fidelity experiments.

---

### 🎛️ CommandX: Mission Control Dashboards  
[Repo](https://github.com/poojakira/Mission-Control-Telemetry-Simulator-Orbital-Monitoring-Dashboards)

- **Why**: Mission operators need consolidated dashboards for orbital state, anomalies, and alerts rather than ad-hoc plots across tools.
- **What**: A mission-control telemetry simulation and anomaly surfacing stack with operator-facing dashboards for orbital monitoring.
- **How**: Simulated orbital telemetry streams, layered anomaly detection, and built Streamlit dashboards for operators to explore satellite state and alerts.
- **When**: Assembled in 2026 to demonstrate operator UX and telemetry observability in one stack.
- **Impact (numeric)**:  
  - Renders multi-panel dashboards with typical query round-trip times under **300 ms** in local tests.  
  - Supports simultaneous visualization of **dozens** of satellite tracks and anomaly overlays per session.

---

### 📡 Hybrid Orbital Monitoring IoT Stack  
[Repo](https://github.com/poojakira/Orbital-Monitoring-IoT-Stack-ESP32-Sensing-Kalman-Filters-Streamlit-Dashboard)

- **Why**: Bridging hardware sensing with orbital analytics requires an end-to-end pipeline from edge devices to cloud dashboards.
- **What**: A hardware-to-cloud orbital monitoring project combining embedded sensing, state estimation, simulation, and visualization.
- **How**: Used ESP32-based sensors, Kalman filtering for state estimation, re-entry simulation, and a containerized Streamlit dashboard for analysis.
- **When**: Implemented in 2026 as a full-stack IoT + ML demonstration for orbital-style monitoring.
- **Impact (numeric)**:  
  - Streams sensor data at **10–50 Hz** per device into the processing stack in lab conditions.  
  - Kalman-filtered estimates stabilize noisy signals with up to **50%** variance reduction versus raw readings on test logs.
