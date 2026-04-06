[![](banner.jpg)](banner.jpg)
<h1 align="center">Pooja Kiran</h1>

<p align="center"> <b>ML / MLOps Engineer · Telemetry & Reliability · Aerospace Systems</b><br/> Building GPU training reliability, telemetry pipelines, and production-grade ML for safety-critical systems.</p>

<p align="center"> <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a> • Phoenix, Arizona · <b>Open to work</b></p>

---

## ⬣ What I Do
- Design and ship **end-to-end ML systems**: data ingest, feature engineering, evaluation, and Dockerized deployment.
- Build **telemetry and anomaly detection** pipelines for aerospace, ESG, and industrial-scale workloads.
- Focus on **reliability and safety**: GPU OOM mitigation, health monitoring, audit-friendly analytics, and CI/CD.
- Implement **physics-aware simulations** with RK4 integration, atmospheric models, and GPU-accelerated ML surrogates.

---

## ⬣ Hero Projects
> These repositories represent my production-minded ML + systems engineering work.

### ⚙️ [Predictive GPU Memory Defragmenter](https://github.com/poojakira/GPU-Training-OOM-Reduction---RTX-Memory-Fragmentation-Lab)
**Problem:** Stochastic OOM crashes during large-model training waste GPU hours and break SLAs.  
**What I built:** An industrial-grade PyTorch infrastructure layer that *predicts* memory fragmentation and triggers proactive compaction before OOM occurs — across GPT-2, BERT, and ResNet-50 workloads.  
**Impact:**
- OOM exceptions: **12 → 0** (SLA guaranteed)
- GPU utilization: **65.4% → 94.1%** (+43.8%)
- Training throughput: **+50%**
- Ships with Prometheus metrics, structured logging, K8s sidecar manifest, and Slurm/HPC integration

---

### 🧠 [PulseNet: Predictive Maintenance on NASA C-MAPSS](https://github.com/poojakira/Predictive-Maintenance-NASA-C-MAPSS-RUL-Forecasting-Pipeline)
**Problem:** Unplanned failures in jet engines, turbines, and industrial machinery cost billions annually.  
**What I built:** End-to-end RUL forecasting and anomaly detection pipeline on the industry-standard NASA C-MAPSS dataset — the same benchmark used in aerospace and EV battery maintenance research.  
**Impact:**
- RUL RMSE: **166.7** (10% improvement over baseline)
- Anomaly detection F1: **0.373**
- Inference throughput: **52,368/sec** at P95 latency **3.94ms**
- MLOps structure: FastAPI inference, Docker, pytest (52 tests), GitHub Actions CI

---

### 🌱 [EcoTrack: ESG Telemetry & Carbon Analytics](https://github.com/poojakira/ESG-Telemetry-Platform-Carbon-Analytics-Forecasting-and-Anomaly-Detection)
**What I built:** An ESG telemetry and carbon analytics prototype for async pipelines, forecasting, and anomaly detection.
- Focuses on audit-friendly reporting, FastAPI, PostgreSQL, and sustainability integrations.

---

### 🛰️ [Orbit-Q: CubeSat Telemetry Pipeline](https://github.com/poojakira/CubeSat-Telemetry-Pipeline-Anomaly-Detection-and-Health-Analytics)
**What I built:** A CubeSat telemetry monitoring pipeline for anomaly detection.
- Features Firebase-backed data flow and satellite health analytics.

---

### 🚀 [Apex-Aegis: Aerospace Trajectory Simulator](https://github.com/poojakira/Aerospace-Trajectory-Simulator-RK4-Atmosphere-Models-ML-Surrogate-Inference)
**What I built:** A physics-aware aerospace trajectory simulation sandbox.
- Uses RK4 integration, atmospheric models, and ML surrogates for constrained inference experiments.

---

### 🎛️ [CommandX: Mission Control Dashboards](https://github.com/poojakira/Mission-Control-Telemetry-Simulator-Orbital-Monitoring-Dashboards)
**What I built:** Mission-control telemetry simulation and anomaly surfacing stack.
- Designed for orbital monitoring and operator-facing Streamlit dashboards.

---

### 📡 [Hybrid Orbital Monitoring IoT Stack](https://github.com/poojakira/Orbital-Monitoring-IoT-Stack-ESP32-Sensing-Kalman-Filters-Streamlit-Dashboard)
**What I built:** Hardware-to-cloud orbital monitoring project.
- Combines ESP32 sensing, Kalman filtering, re-entry simulation, and a containerized Streamlit dashboard.
