<div align="center">
  <img src="https://raw.githubusercontent.com/poojakira/poojakira/main/banner.jpg" alt="Pooja Kiran — ML / MLOps Engineer" width="100%" />
</div>

<br/>


# Pooja Kiran

**ML / MLOps Engineer · GPU Training Reliability · Telemetry Pipelines · Secure ML Infrastructure (IT Security background)**

I build production-minded ML systems with a focus on **GPU training reliability**, **telemetry-driven observability**, and **secure ML infrastructure** in reliability-sensitive environments.

- 📍 Phoenix / Tempe, Arizona, US  
- 🎓 M.S. in Information Technology Security, Arizona State University  
- 📄 IEEE INDICON 2023 co-author  
- ☁️ AWS Certified  
- 🔗 [LinkedIn](https://www.linkedin.com/in/poojakiran/)  
- 📫 [Email](mailto:poojakiranbharadwaj@gmail.com)  

---

## About Me

I’m an ML / MLOps engineer working at the intersection of **machine learning, systems engineering, and observability**. My work centers on training stability, telemetry pipelines, and infrastructure patterns that make ML systems measurable and trustworthy in production-like settings.

I started from an **information security** background (M.S. in IT Security at ASU), which means I naturally think about isolation, access, secrets, and blast radius when designing ML systems. That security-first perspective now informs how I approach **GPU-heavy training, deployment workflows, and telemetry for high-stakes domains** such as aerospace, defense, and critical infrastructure.

I co-authored an **IEEE INDICON 2023** paper on reinforcement learning for adaptive e-learning over satellite links, which strengthened my interest in systems that must operate under constraints (latency, limited bandwidth, failure-prone environments).

> **How I work:** I treat these projects as engineering systems, not just demos — with versioned configs, benchmark methodology, documented assumptions, and iterative improvements tracked over time.

---

## Key Systems & Outcomes

A snapshot of outcome-focused work across my flagship projects. Benchmarks and methodology live in the individual repos and are being actively hardened for reproducibility.

- **[Predictive-GPU-Memory-Defragmenter](https://github.com/poojakira/Predictive-GPU-Memory-Defragmenter)**  
  Experimental allocator-aware workflow to model GPU memory fragmentation and reduce training-time OOM failures on RTX-class workloads.  
  **Focus:** GPU memory profiling, fragmentation modeling, training stability, throughput optimization, observability.  
  **Status:** Prototype under active hardening with clearer benchmark methodology, hardware specs, baselines, and logged results.

- **[PulseNet](https://github.com/poojakira/PulseNet)**  
  Production-style predictive maintenance and anomaly detection pipeline built around NASA C-MAPSS engine telemetry.  
  **Focus:** feature engineering, anomaly detection, model-serving patterns, Dockerized workflows, deployment-oriented structure.  
  **Status:** Pipeline with documented evaluation approach; moving toward stronger reproducibility and monitoring.

- **[CommandX](https://github.com/poojakira/CommandX)**  
  Mission-control telemetry simulation and anomaly-surfacing stack for orbital monitoring and operator-facing systems.  
  **Focus:** telemetry pipelines, state estimation, simulation, monitoring, operator UX for mission-grade systems.  
  **Status:** Includes EKF-based estimation, genetic optimization, and Monte Carlo IV&V workflows; being refined for clarity and reuse.

- **[Apex-Aegis-Tactical-Suite](https://github.com/poojakira/Apex-Aegis-Tactical-Suite)**  
  RK4-based tactical trajectory simulator with an ML surrogate to accelerate decision support.  
  **Focus:** numerical simulation, surrogate modeling, runtime vs. error trade-offs, decision latency.  
  **Status:** Prototype demonstrating speed/accuracy trade-offs, with ongoing work to document baselines, error bounds, and limitations.

- **[orbit-Q](https://github.com/poojakira/orbit-Q)**  
  CubeSat telemetry health monitoring pipeline with anomaly detection and retraining workflow support.  
  **Focus:** anomaly detection, ensemble modeling, dataflow automation, system health telemetry.  
  **Status:** End-to-end pipeline with room to deepen observability, benchmarks, and operational documentation.

---

## Benchmarking & Reproducibility

I am standardizing how I present performance claims across repos. Each flagship project is being updated to include:

- **Hardware:** GPU/CPU, RAM, and environment used for evaluation.  
- **Workload / dataset:** what was actually run (e.g., model size, telemetry source, scenario).  
- **Baseline:** clearly defined comparison point (default implementation / unoptimized pipeline).  
- **Methodology:** number of runs, what metrics were measured, and how they were aggregated.  
- **Artifacts:** scripts, logs, and/or CSVs for results, where practical.  
- **Limitations:** scope of results (e.g., prototype only, RTX-class only, not yet validated on A100/H100 or in clustered environments).

**Example format used in repos:**

```text
Hardware: RTX-class GPU, 64 GB RAM
Workload: representative transformer / telemetry pipeline benchmark
Baseline: default implementation without optimization
Method: repeated runs with tracked failures, runtime, and utilization
Results: compared against baseline with logs and/or CSVs in the repo
Limitations: prototype evaluation; not yet validated on all hardware or production clusters
```

This is an ongoing effort to ensure that reported numbers are **transparent, reproducible, and honestly scoped**.

---

## Selected Projects (High Level)

### Predictive GPU Memory Defragmenter

Systems-focused ML infra project for detecting fragmentation risk and evaluating strategies to improve training reliability under GPU memory pressure.

- **What it explores:** GPU memory behavior under load, fragmentation-aware strategies, trade-offs between throughput and safety.  
- **Patterns:** allocator-aware logging, profiling, and experimental workflows suitable for integration into training pipelines.

### PulseNet

Predictive maintenance pipeline built on industrial telemetry (NASA C-MAPSS) with deployment in mind.

- **What it explores:** feature extraction from time-series telemetry, anomaly detection, production-friendly pipeline structuring.  
- **Patterns:** model packaging, Dockerization, service-like structure for telemetry-driven ML.

### CommandX

Mission-control flavored telemetry simulation and anomaly surfacing for orbital systems.

- **What it explores:** state estimation, simulation-based operator support, telemetry visualization.  
- **Patterns:** combining numerical methods, optimization, and ML to support operator-facing workflows.

### orbit-Q

Telemetry health monitoring for small satellites with retraining hooks.

- **What it explores:** health monitoring, retraining triggers, lightweight deployment patterns.  
- **Patterns:** ensemble modeling, dataflow automation, telemetry ingestion.

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

- AES-256 concepts and secure data handling  
- Zero-trust-aligned thinking  
- NIST / ISO-style controls as mental models  
- Secure ML infrastructure design (secrets, isolation, blast radius)  

### Research / Engineering Tools

- Jupyter / Google Colab  
- Numerical simulation (e.g., RK4-based workflows)  
- ROS and related robotics / simulation tooling  

---

## Open Source & Collaboration

I’m actively working to grow my **open-source and collaborative footprint** by:

- using a branch → PR → review → merge workflow even on personal repos,  
- opening small but real PRs to external ML / infra projects (docs, examples, minor fixes),  
- improving issues, documentation, and benchmarks in my own repositories,  
- keeping contribution activity **steady over time** instead of in one-off bursts.

The goal is for this profile to reflect **authentic, ongoing engineering work**, not a single sprinted portfolio.

---

## Publication

- **“A Personalized E-Learning System Using Reinforcement Learning Through Satellite”**  
  **P. K. Bharadwaj et al.** · **IEEE INDICON 2023**  
  [View on IEEE Xplore](https://ieeexplore.ieee.org/document/10440852)  

Technical contribution: Q-learning-based adaptive content delivery over high-latency satellite links, with emphasis on dynamic state modeling under constrained network conditions.

---

## What I’m Looking For

I’m interested in roles such as:

- **Machine Learning Engineer**  
- **MLOps Engineer**  
- **ML Platform / Infra Engineer**  
- **Cloud / Infrastructure Engineer for ML systems**  

I’m particularly excited by teams working on:

- GPU-heavy training systems and distributed training  
- ML platform and infrastructure for real-world deployments  
- Observability and reliability engineering for ML systems  
- Secure deployment pipelines and multi-tenant ML environments  
- Aerospace, defense, or other high-stakes ML applications  

---

## Current Focus

Right now, I’m spending most of my time on:

- strengthening GPU training reliability and fragmentation-aware workflows,  
- building telemetry-aware ML systems with better observability,  
- hardening MLOps pipelines for realistic deployment environments,  
- upgrading project documentation, benchmarking, and reproducibility across repos,  
- expanding my open-source contributions in the ML / infra ecosystem.  

---

## Connect

- [LinkedIn](https://www.linkedin.com/in/poojakiran/)  
- [GitHub](https://github.com/poojakira)  
- [Email](mailto:poojakiranbharadwaj@gmail.com)  
