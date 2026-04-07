# Pooja Kiran

ML / MLOps Engineer · IEEE-published researcher · AWS Certified · M.S. student at ASU  
Building GPU training reliability, telemetry pipelines, and secure ML in applied aerospace and industrial systems.

📍 Phoenix, Arizona, US  
🔗 [LinkedIn](https://www.linkedin.com/in/poojakiran/) · 💭 Open to work

## About Me

I build production-minded ML systems for telemetry-heavy, safety-conscious environments, with a focus on GPU reliability, anomaly detection, forecasting, and secure deployment. My work sits at the intersection of machine learning, MLOps, and aerospace-style monitoring systems.

I’m especially interested in:

- ML infrastructure and model reliability  
- Telemetry pipelines and anomaly detection  
- Applied aerospace and mission-control systems  
- Secure, auditable, Dockerized ML deployment  

## Featured Projects

### [RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard)

**What:** Prototype for modeling GPU memory fragmentation and reducing training-time out-of-memory failures on RTX-class workloads.  
**Why:** Long-running deep learning jobs fail expensively when fragmentation causes avoidable OOM crashes.  
**How:** Built a PyTorch- and Docker-based experimental setup to evaluate fragmentation-aware mitigation strategies on GPU training workloads.  
**Metrics:** OOMs reduced `23 → 0`, VRAM utilization `94% → 87%`, fragmentation ratio `0.61 → 0.18`, training overhead `< 2%`.

### [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting)

**What:** Predictive maintenance pipeline using NASA C-MAPSS data for remaining useful life forecasting and anomaly detection.  
**Why:** Industrial and aerospace maintenance systems need earlier fault visibility and more accurate degradation forecasting.  
**How:** Designed an MLOps-oriented pipeline with Dockerized local deployment, time-series modeling, and telemetry-driven anomaly workflows.  
**Metrics:** RUL RMSE `166.7` (~10% over linear baseline), anomaly F1 `0.373`, throughput `52,368 req/s`, P95 latency `3.94 ms`, 52 automated tests.

### [Orbital-IoT-Monitor](https://github.com/poojakira/Orbital-IoT-Monitor)

**What:** Hybrid orbital monitoring project combining ESP32 sensing, Kalman filtering, re-entry simulation, and a containerized Streamlit dashboard.  
**Why:** Telemetry systems are more useful when hardware, simulation, filtering, and operator visibility are connected end to end.  
**How:** Integrated IoT sensing, state estimation, simulation, and dashboard-based monitoring into one reproducible system.  
**Metrics:** Telemetry streaming at `10–50 Hz` per device, Kalman filter reduces variance by `~50%`, re-entry simulation from 550 km LEO to impact.

### [Aerospace-Trajectory-Simulator](https://github.com/poojakira/Aerospace-Trajectory-Simulator)

**What:** Physics-aware aerospace trajectory simulation sandbox using RK4 integration, atmospheric models, and ML surrogates.  
**Why:** High-fidelity simulation is useful for testing constrained inference and trajectory behavior before deployment.  
**How:** Combined classical numerical methods with ML surrogate modeling in a Dockerized Python environment.  
**Metrics:** Surrogate speedup `11.5x` over RK4 (P99 latency `1.84 ms → 0.16 ms`), throughput `500 → 5,750 seq/s`, bit-accurate parity (MAE `0.0000 m`).

### [ESG-Carbon-Telemetry](https://github.com/poojakira/ESG-Carbon-Telemetry)

**What:** ESG telemetry and carbon analytics platform for async pipelines, forecasting, anomaly detection, and audit-friendly reporting.  
**Why:** Sustainability reporting requires traceable data pipelines and reliable anomaly surfacing, not just dashboards.  
**How:** Built an async telemetry-focused architecture with Python, Docker, PostgreSQL, and forecasting workflows.  
**Metrics:** Ingestion latency p99 `450 ms → 42 ms` (~10.7x), forecast MAE `4.2%` (vs 14.2% baseline), anomaly recall `94.2%`, Merkle audit `13.6x` faster.

### [Mission-Control-Telemetry-Simulator](https://github.com/poojakira/Mission-Control-Telemetry-Simulator)

**What:** Mission-control telemetry simulation and anomaly surfacing stack for orbital monitoring and operator-facing dashboards.  
**Why:** Operators need interpretable health signals and real-time visibility into changing system states.  
**How:** Built telemetry simulation flows and Streamlit-based monitoring views for anomaly detection and operational review.  
**Metrics:** EKF state convergence in `~10 steps`, GA delta-v optimization `< 1s`, anomaly inference `< 50 ms` per telemetry frame, full Space-Track TLE catalog (~4.6 MB) rendered live.

### [CubeSat-Health-Monitor](https://github.com/poojakira/CubeSat-Health-Monitor)

**What:** CubeSat telemetry monitoring pipeline for anomaly detection, Firebase-backed data flow, and satellite health analytics.  
**Why:** Small-satellite systems need lightweight but reliable telemetry infrastructure for health assessment.  
**How:** Combined telemetry ingestion, cloud-backed data flow, and anomaly analytics into a deployable monitoring pipeline.  
**Metrics:** Ensemble F1 `0.928`, precision `0.942`, recall `0.915`, throughput `63,622 events/s`, inference latency `15.72 µs`, false alarm rate `~3–5%` over 24h window.

## Tech Stack

**Languages & ML:** Python, PyTorch, time-series modeling, anomaly detection, forecasting  
**MLOps & Infra:** Docker, CI-friendly project structure, reproducible local deployment, telemetry pipelines  
**Data & Systems:** PostgreSQL, Firebase, IoT telemetry, monitoring dashboards  
**Domains:** Aerospace systems, predictive maintenance, ESG analytics, mission-control simulation  

## What I Care About

- Building ML systems that survive real operational constraints  
- Turning telemetry into actionable health and reliability signals  
- Combining simulation, monitoring, and inference in one workflow  
- Writing clean, reproducible, recruiter-readable project documentation  

## Currently Exploring

- GPU training reliability and fragmentation-aware optimization  
- Production-ready ML observability  
- Secure ML deployment patterns  
- Applied robotics and aerospace intelligence systems  
