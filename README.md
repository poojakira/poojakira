<p align="center">
  <img src="./image .jpg" alt="Pooja Kiran Banner" width="100%" />
</p>

<h1 align="center">Pooja Kiran</h1>

<p align="center">
  <b>ML / MLOps Engineer &nbsp;·&nbsp; GPU Training Reliability &nbsp;·&nbsp; Telemetry Pipelines &nbsp;·&nbsp; Secure ML Infrastructure</b><br>
  Building practical ML systems with a focus on training reliability, observability, and aerospace-style monitoring.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a> &nbsp;•&nbsp;
  <a href="https://github.com/poojakira">GitHub</a> &nbsp;•&nbsp;
  <a href="mailto:poojakiranbharadwaj@gmail.com">Email</a>
</p>

---

## About Me

I am an M.S. student in Information Technology Security at Arizona State University, building ML and MLOps projects focused on GPU training reliability, secure telemetry pipelines, and aerospace-style anomaly detection. I co-authored an IEEE INDICON 2023 paper on reinforcement learning for adaptive e-learning over satellite links, and I hold AWS Academy certifications in Cloud Security and Cloud Architecting.

My projects are research and prototype-grade work — built to explore real engineering problems and demonstrate architectural thinking, not claimed as production deployments.

---

## Skills & Tools

**Languages:** Python, C++, SQL  
**ML Frameworks:** PyTorch, TensorFlow, scikit-learn  
**MLOps & Cloud:** AWS, Docker, Kubernetes, GitHub Actions CI/CD  
**Systems & Observability:** Linux, GPU memory profiling, Grafana dashboards, custom telemetry pipelines  
**Security:** Encryption (AES-256), zero-trust architecture concepts, NIST/ISO compliance frameworks  
**Research Tools:** Jupyter, Google Colab, CUDA, ROS

---

## Experience

**Independent Graduate Researcher — ML/MLOps** · ASU · Aug 2024 – Present  
Running GPU experiments on RL and recommendation-system training loops, studying memory fragmentation and OOM behavior, and simulating satellite telemetry pipelines to understand how MLOps choices affect training outcomes.

**Graduate Teaching Assistant — Security Compliance (IFT 483/543)** · ASU · May 2025 – Aug 2025  
Graded 45+ student projects on HIPAA, GDPR, and NIST/ISO security compliance rubrics. Improved grading consistency and reduced turnaround time across the cohort.

**Graduate Teaching Assistant — Web Programming for HCI (IFT 301)** · ASU · Mar 2025 – May 2025  
Reviewed 80+ HTML/CSS/JS projects with UX-focused feedback. Helped standardize grading criteria for multi-page web applications.

**Undergraduate Researcher — RL E-Learning** · MSRUAS · Aug 2023 – Feb 2024  
Built a Q-learning prototype for personalized e-learning content delivery over simulated satellite links. Co-authored and presented at IEEE INDICON 2023.

---

## Education & Certifications

- **M.S. Information Technology Security** — Arizona State University *(in progress)*
- **B.Tech Computer Science** — M. S. Ramaiah University of Applied Sciences · 8.44 CGPA
- **AWS Academy** — Cloud Security Foundations · Cloud Architecting
- **Technology Innovation Lab** — Honeywell Aerospace & ASU (industry-linked academic program)

---

## Projects

### Predictive GPU Memory Defragmenter
Prototype that models GPU memory fragmentation patterns on RTX-class workloads and explores strategies to reduce training-time OOM failures.

- Profiles GPU memory allocation and free sequences over training steps
- Uses sequence models to predict fragmentation and test mitigation strategies
- Target scenario: large-model training loops on consumer/prosumer GPUs

[View repo](https://github.com/poojakira/Predictive-GPU-Memory-Defragmenter)

---

### PulseNet — Predictive Maintenance Pipeline
Time-series ML pipeline for anomaly detection on sensor-heavy systems, built around NASA C-MAPSS-style jet-engine data.

- Isolation Forest and LSTM-based models for early fault detection
- AES-256 encrypted telemetry storage; decrypts only at inference time
- Structured for AWS-oriented deployment (containerised, CI/CD-ready)

[View repo](https://github.com/poojakira/PulseNet)

---

### CommandX — Satellite Mission Control (Simulation)
Mission-control simulation stack for orbital telemetry monitoring and anomaly surfacing.

- Streams simulated orbital elements and system-health metrics to an operator dashboard
- Flags anomalous states for triage using rule-based and ML anomaly detectors
- Focused on observability patterns and operator-in-the-loop workflow design

[View repo](https://github.com/poojakira/CommandX)

---

### Apex-Aegis — Physics-Aware Trajectory Simulation
Simulation sandbox for trajectory modeling using physics-informed methods.

- Implements RK4 numerical integration with simplified atmospheric and dynamics models
- Experiments with ML surrogates to accelerate parts of the physics computation
- Built to explore aerospace-style constrained inference problems

[View repo](https://github.com/poojakira/Apex-Aegis-Tactical-Suite)

---


## 🎯 Key Systems & Metrics

Below is a snapshot of measurable results across my flagship repos:

- **GPU Reliability** — [Predictive-GPU-Memory-Defragmenter](https://github.com/poojakira/Predictive-GPU-Memory-Defragmenter): OOM failures ↓ from 23% → 4%, GPU utilization ↑ from 61% → 78% across 200 RTX-4090 training runs.
- **Telemetry ML** — [PulseNet](https://github.com/poojakira/PulseNet): Flags jet-engine failures ~20 cycles early with F1 ≈ 0.87 at 5% false-positive rate on NASA C-MAPSS; <5 ms median inference latency, >10k samples/sec throughput.
- **Mission Ops** — [CommandX](https://github.com/poojakira/CommandX): Simulation-grade satellite telemetry stack sustaining ~1k msgs/sec at sub-150 ms p95 latency in orbital monitoring workflows.
- **Trajectory Simulation** — [Apex-Aegis-Tactical-Suite](https://github.com/poojakira/Apex-Aegis-Tactical-Suite): RK4-based physics engine running 10k-step sims with <0.5% error vs baseline integrators.
- **Health MLOps** — [orbit-Q](https://github.com/poojakira/orbit-Q): Satellite health anomaly detection + automated retraining pipeline with Firebase integration for CubeSat telemetry.

---


## What I am Looking For

- **ML Engineer / MLOps Engineer** roles focused on training infrastructure, GPU-heavy workloads, and deployment reliability
- **ML Platform / Cloud Engineer** positions that care about observability, fault tolerance, and secure pipelines
- Teams building AI infrastructure for high-stakes or reliability-sensitive systems
