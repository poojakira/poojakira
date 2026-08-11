<!-- Animated gradient header (renders on GitHub) -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b3d91,50:1f6feb,100:6f42c1&height=200&section=header&text=Pooja%20Kiran&fontSize=52&fontColor=ffffff&descSize=22&descAlignY=60" alt="Pooja Kiran — AI/ML Security Engineer" />
=======
  

<h2 align="center">AI/ML Security Engineer</h2>

<p align="center">
  <em>Securing AI agents, models, and the MCP supply chain &nbsp;·&nbsp; evidence-first, every claim ties to a reproducible artifact</em>
</p>

<p align="center">
  <a href="https://linkedin.com/in/poojakiran"><img src="https://img.shields.io/badge/LinkedIn-poojakiran-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/poojakira"><img src="https://img.shields.io/badge/GitHub-poojakira-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <img src="https://img.shields.io/badge/Greater%20Phoenix%20Area-AZ-2ea44f?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Location" />
  <img src="https://img.shields.io/badge/Work%20Auth-F--1%20OPT%20(EAD)%20%7C%20STEM--OPT-orange?style=for-the-badge" alt="Work Authorization" />
</p>

---

## About

AI/ML Security Engineer who builds the defenses AI systems are deployed without. I've written
three open-source security tools covering AI agent identity, model supply-chain integrity, and
MCP protocol security. I have a peer-reviewed IEEE publication, an MS focused on AI and cloud
security, and threat-modeling experience with Honeywell Aerospace. I keep everything
evidence-first: every claim on this profile ties to a reproducible artifact you can run.

---

## Featured Security Tools

### 🛡️ [aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard)
Static IAM policy linter for AI agent roles. **25 rules** across Bedrock, SageMaker, and Lambda,
zero runtime dependencies, SARIF output, and a CI gate that blocks over-privileged policies before
they deploy. Includes kill-chain rules (AIG019-021) modeled on the 2026 OpenAI–Hugging Face
incident: it flags the credential-harvest + lateral-movement combination that turned a foothold
into a three-day breach.
`pip install -e .` · zero deps · SARIF · [`--live-scan`] real AWS accounts

### 🔬 [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Model supply-chain scanner that detects pickle RCE, SafeTensors injection, and typosquatting
through a taint engine with symbolic resolution. In a head-to-head against Protect AI's ModelScan
0.8.8 it caught **8/8 payloads to ModelScan's 6/8**, reproduced **12/12** 2024–26 CVEs, and
produced **0 false positives** on legitimate sklearn/PyTorch/numpy models. Scans a Hugging Face
URL over HTTP range requests, so it flags a malicious model *before* you download the weights.

### 🚦 [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor)
A JSON-RPC 2.0 proxy that inspects every MCP tool call against **55 detection patterns** for prompt
injection and data exfiltration, with Unicode normalization, hash-chained audit logging, and
Kubernetes deployment manifests. It sits between an MCP client and server and blocks malicious
tool calls in real time, before they reach the server.

### Supporting work
Adversarial ML and privacy research, all mapped to MITRE ATLAS and the NIST AI RMF:

- [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) — prompt-injection detection + a live LLM-endpoint scanner that tests any OpenAI-compatible API against a published injection corpus.
- [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) — FGSM / PGD / C&W attacks benchmarked against a real pretrained ResNet-18.
- [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) — Yeom / Shokri / LiRA membership inference, model inversion, and a DP-SGD defense, with a privacy-risk assessment on the real UCI Adult dataset.
- [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) — spectral-signature detection for label-flip data poisoning, including a scan-before-you-train check for Hugging Face datasets.
- [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) — a NASA C-MAPSS remaining-useful-life forecaster (1D-CNN, RMSE 13.19) wrapped in a secure-MLOps pipeline with STRIDE threat modeling, RBAC, and a tamper-evident audit log.

---

## Technical Skills

**AI Security**
![AI Agent Security](https://img.shields.io/badge/AI_Agent_Security-0b3d91?style=flat-square)
![LLM & RAG Security](https://img.shields.io/badge/LLM_%26_RAG_Security-0b3d91?style=flat-square)
![Prompt Injection Defense](https://img.shields.io/badge/Prompt_Injection_%26_Jailbreak_Defense-0b3d91?style=flat-square)
![Model Supply-Chain](https://img.shields.io/badge/Model_Supply--Chain_Security-0b3d91?style=flat-square)
![Adversarial ML](https://img.shields.io/badge/Adversarial_ML_(FGSM%2FPGD%2FC%26W)-0b3d91?style=flat-square)
![Model Privacy](https://img.shields.io/badge/Membership_Inference_%26_Model_Privacy-0b3d91?style=flat-square)
![Differential Privacy](https://img.shields.io/badge/Differential_Privacy_(DP--SGD)-0b3d91?style=flat-square)
![Data Poisoning](https://img.shields.io/badge/Data_Poisoning_Detection-0b3d91?style=flat-square)
![MCP Security](https://img.shields.io/badge/MCP_Security-0b3d91?style=flat-square)

**Frameworks**
![OWASP LLM Top 10](https://img.shields.io/badge/OWASP_LLM_Top_10-1f6feb?style=flat-square)
![MITRE ATLAS](https://img.shields.io/badge/MITRE_ATLAS-1f6feb?style=flat-square)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-1f6feb?style=flat-square)
![NIST AI RMF](https://img.shields.io/badge/NIST_AI_RMF-1f6feb?style=flat-square)
![Threat Modeling](https://img.shields.io/badge/Threat_Modeling-1f6feb?style=flat-square)

**Cloud & DevSecOps**
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws)
![CI/CD Security](https://img.shields.io/badge/CI%2FCD_Security-6f42c1?style=flat-square)
![SARIF](https://img.shields.io/badge/SARIF-6f42c1?style=flat-square)
![GitHub Advanced Security](https://img.shields.io/badge/GitHub_Advanced_Security-6f42c1?style=flat-square)
![CycloneDX SBOM](https://img.shields.io/badge/SBOM_(CycloneDX)-6f42c1?style=flat-square)
![Ed25519](https://img.shields.io/badge/Ed25519_Signing-6f42c1?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)

**Engineering**
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![JSON-RPC 2.0](https://img.shields.io/badge/JSON--RPC_2.0-black?style=flat-square)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka)
![API Security](https://img.shields.io/badge/API_Security-black?style=flat-square)

---

## Experience

**AI/ML Security Engineer** — Independent, Open-Source · Tempe, AZ · *Aug 2024 – Present*
- Built **aws-agent-identity-guard**, a static IAM policy linter for AI agent roles: 25 rules across
  Bedrock, SageMaker, and Lambda, zero runtime dependencies, SARIF output, and a CI gate that blocks
  over-privileged policies before deployment. Packaged with a PyPI-ready `pyproject.toml`;
  `pip`-installable with zero runtime deps.
- Built **hf-model-provenance-scanner**, a model supply-chain scanner detecting pickle RCE,
  SafeTensors injection, and typosquatting via a taint engine with symbolic resolution. Detected
  8/8 payloads vs 6/8 for Protect AI ModelScan, reproduced 12/12 2024–26 CVEs, 0 false positives.
- Built **mcp-security-gateway-monitor**, a JSON-RPC 2.0 proxy inspecting every MCP tool call
  against 55 patterns for prompt injection and data exfiltration, with Unicode normalization,
  hash-chained audit logging, and Kubernetes deployment manifests.
- Implemented adversarial ML (FGSM/PGD/C&W) and privacy attacks (Yeom/Shokri/LiRA MIA, model
  inversion, DP-SGD defense), mapping findings to MITRE ATLAS and NIST AI RMF.

**Graduate Teaching Assistant (IT Grader)** — Ira A. Fulton Schools of Engineering, ASU · Mesa, AZ · *Jan 2025 – Oct 2025*
- Evaluated graduate coursework in secure coding, secure software design, infrastructure security,
  and configuration management, giving feedback that strengthened students' secure practices.
- Assessed submissions against secure coding standards, security principles, and compliance
  requirements.

---

## Education

**Arizona State University** — MS, Information Technology · **3.87 GPA** · *Aug 2024 – May 2026*
Focus: AI/ML security, cloud security, secure software engineering. Coursework: Advanced
Information Systems Security, Computer & IT Architecture, Advanced DBMS, Information Systems
Development.

**M. S. Ramaiah University of Applied Sciences** — BTech, Computer Science · **8.44 CGPA** · *2019 – 2023*

---

## Certifications & Publication

- **AWS Academy — Cloud Security Foundations** (IAM, VPC security, encryption at rest & in transit)
- **Technology Innovation Lab** — Honeywell Aerospace & ASU (100-day connected-aviation security engagement)
- 📄 *"A Personalized E-Learning System Using Reinforcement Learning Through Satellite,"* **IEEE INDICON 2023** (NIT Warangal). Q-Learning for adaptive learning over CubeSat networks. Recipient, KSCST government research grant.

---

<p align="center">
  <img src="https://img.shields.io/badge/Open--Source_Security_Tools-3-1f6feb?style=flat-square" alt="tools" />
  <img src="https://img.shields.io/badge/IEEE_Publication-INDICON_2023-6f42c1?style=flat-square" alt="publication" />
  <img src="https://img.shields.io/badge/MS_Information_Technology-3.87_GPA-2ea44f?style=flat-square" alt="gpa" />
  <img src="https://img.shields.io/github/followers/poojakira?style=flat-square&label=Followers&color=0b3d91" alt="followers" />
</p>

<p align="center"><sub>Evidence policy: every metric above links to a committed, reproducible artifact in its repo. Numbers are measured, not estimated.</sub></p>
