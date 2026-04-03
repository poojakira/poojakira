![Pooja Kiran — ML / MLOps Engineer](https://raw.githubusercontent.com/poojakira/poojakira/main/banner.jpg)

# Pooja Kiran

**ML / MLOps Engineer · GPU Training Reliability · Telemetry Pipelines · Secure ML Infrastructure (IT Security background)**

- 📍 Phoenix / Tempe, Arizona, US  
- 🎓 M.S. in Information Technology Security, Arizona State University  
- 📄 IEEE INDICON 2023 co-author  
- ☁️ AWS Certified  
- 🔗 [LinkedIn](https://www.linkedin.com/in/poojakiran/) · 📫 [Email](mailto:poojakiranbharadwaj@gmail.com)

---

## TL;DR

- I build **GPU-heavy** ML systems with a focus on training reliability, telemetry-driven observability, and secure ML infrastructure.  
- Prototyped a **GPU memory defragmentation** workflow to reduce training-time OOMs on RTX-class workloads.  
- Designed **telemetry + anomaly detection** pipelines on NASA C‑MAPSS and CubeSat-like data with deployment and monitoring in mind.  
- Security-first mindset (M.S. IT Security, AWS Certified) applied to ML infra: isolation, secrets, and blast radius.

---

## Highlights

- Co-authored an **IEEE INDICON 2023** paper on reinforcement learning over high-latency satellite links (constraint-aware systems).  
- Built mission-control-style **telemetry and anomaly surfacing** stacks for orbital / engine data in Dockerized, reproducible repos.  
- Experience with **AWS, Docker, Kubernetes, GitHub Actions, CI/CD** for ML systems and pipelines.  

---

## Key Systems & Outcomes

A snapshot of outcome-focused work across my flagship projects. Benchmarks and methodology live in the repos and are being hardened for reproducibility.

### Predictive-GPU-Memory-Defragmenter
**Repo:** [Predictive-GPU-Memory-Defragmenter](https://github.com/poojakira/Predictive-GPU-Memory-Defragmenter)  

- Models GPU memory fragmentation on RTX-class GPUs and experiments with allocator-aware workflows to reduce training-time OOM failures and improve stability.  
- Focuses on GPU memory profiling, fragmentation modeling, and trade-offs between throughput and safety, with an emphasis on logging and observability.  

### PulseNet
**Repo:** [PulseNet](https://github.com/poojakira/PulseNet)  

- Predictive maintenance and anomaly detection pipeline built around **NASA C‑MAPSS** engine telemetry, structured for deployment.  
- Emphasizes feature engineering, anomaly detection, model-serving patterns, and Dockerized workflows suitable for production-style environments.  

### CommandX
**Repo:** [CommandX](https://github.com/poojakira/CommandX)  

- Mission-control telemetry simulation and anomaly surfacing stack for **orbital monitoring and operator-facing systems**.  
- Combines EKF-based state estimation, optimization, and simulation to support operator workflows and telemetry visualization.  

### Apex-Aegis-Tactical-Suite
**Repo:** [Apex-Aegis-Tactical-Suite](https://github.com/poojakira/Apex-Aegis-Tactical-Suite)  

- RK4-based tactical trajectory simulator with an ML surrogate to accelerate decision support.  
- Explores numerical simulation, surrogate modeling, and runtime vs. error trade-offs for decision latency.  

### orbit-Q
**Repo:** [orbit-Q](https://github.com/poojakira/orbit-Q)  

- CubeSat telemetry health monitoring pipeline with anomaly detection and **retraining hooks**.  
- Uses ensemble modeling and dataflow automation to support system health telemetry and retraining triggers.  

---

## Benchmarking & Reproducibility

Across repos, I’m standardizing how I present performance claims. Each flagship project is being updated to include:

- **Hardware:** GPU/CPU, RAM, and environment used for evaluation.  
- **Workload / dataset:** model size, telemetry source, and scenario.  
- **Baseline:** clearly defined comparison point (default implementation / unoptimized pipeline).  
- **Methodology:** number of runs, metrics measured, and aggregation.  
- **Artifacts:** scripts, logs, and/or CSVs for results.  
- **Limitations:** scope of results (e.g., prototype only, RTX-class only, not yet validated on A100/H100 or clusters).

Example format used in repos:

`Hardware: RTX-class GPU, 64 GB RAM  
Workload: representative transformer / telemetry pipeline benchmark  
Baseline: default implementation without optimization  
Method: repeated runs with tracked failures, runtime, and utilization  
Results: compared against baseline with logs and/or CSVs in the repo  
Limitations: prototype evaluation; not yet validated on all hardware or production clusters`

---

## Core Stack

### Languages
- Python  
- C++  
- SQL  

### Machine Learning
- PyTorch  
- TensorFlow  
- scikit-learn  

### MLOps / Cloud / DevOps
- AWS  
- Docker  
- Kubernetes  
- GitHub Actions  
- CI/CD workflows  

### Systems / Observability
- Linux  
- GPU memory profiling & CUDA-oriented experimentation  
- Telemetry pipelines  
- Grafana-style dashboards and metrics  
- Performance benchmarking  

### Security
- Secure ML infrastructure design (secrets, isolation, blast radius)  
- Zero-trust-aligned thinking using NIST / ISO-style controls as mental models  
- AES-256 concepts and secure data handling  

---

## Open Source & Collaboration

I’m growing my **open-source and collaborative footprint** by:

- Using a branch → PR → review → merge workflow even on personal repos.  
- Opening small PRs to external ML / infra projects (docs, examples, minor fixes).  
- Improving issues, documentation, and benchmarks in my own repositories.  
- Keeping contribution activity **steady over time**, not just in one-off bursts.  

---

## Publication

- **“A Personalized E-Learning System Using Reinforcement Learning Through Satellite” – IEEE INDICON 2023**  
  [View on IEEE Xplore](https://ieeexplore.ieee.org/document/10440852)  

Technical contribution: Q-learning-based adaptive content delivery over high-latency satellite links, with emphasis on dynamic state modeling under constrained network conditions.

---

## What I’m Looking For

I’m interested in roles such as:

- **ML Platform / Infra Engineer**  
- **MLOps Engineer**  
- **Machine Learning Engineer**  
- **Cloud / Infrastructure Engineer for ML systems**  

I’m particularly excited by teams working on:

- GPU-heavy training systems and distributed training.  
- ML platforms and infrastructure for real-world deployments.  
- Observability and reliability engineering for ML systems.  
- Secure deployment pipelines and multi-tenant ML environments.  
- Aerospace, defense, or other high-stakes ML applications.  

---

## Current Focus

Right now, I’m spending most of my time on:

- Strengthening GPU training reliability and fragmentation-aware workflows.  
- Building telemetry-aware ML systems with better observability.  
- Hardening MLOps pipelines for realistic deployment environments.  
- Upgrading project documentation, benchmarking, and reproducibility.  
- Expanding my open-source contributions in the ML / infra ecosystem.  

---

## Connect

- [LinkedIn](https://www.linkedin.com/in/poojakiran/)  
- [GitHub](https://github.com/poojakira)  
- [Email](mailto:poojakiranbharadwaj@gmail.com)
