<!-- ============================================================= -->
<!--  Pooja Kiran Bharadwaj · AI Security Engineer                  -->
<!--  GitHub Profile README  (repo: poojakira/poojakira)           -->
<!-- ============================================================= -->

<div align="center">

<!-- Animated hero hook -->
<a href="https://github.com/poojakira">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=00E5FF&center=true&vCenter=true&width=820&lines=AI+stops+being+a+prediction+problem...;...and+becomes+a+security+problem+the+moment+it+can+ACT.;Capability+is+not+permission.;Permission+is+not+provenance.;Identity+is+not+authorization." alt="Typing hook" />
</a>

<br/>

# Pooja Kiran Bharadwaj

### 🛡️ AI Security Engineer — Agentic AI · MCP/Tool Security · Model Supply-Chain · IAM

<p>
  <img src="https://img.shields.io/badge/Focus-Agentic_AI_Security-00E5FF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Domain-MCP_%2F_Tool_Security-7C4DFF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Supply_Chain-Model_Provenance-FF4D6D?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Open_to_Work-2ECC71?style=for-the-badge" />
</p>

<p>
  <a href="https://linkedin.com/in/poojakiran"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:pkiran1@asu.edu"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" /></a>
  <img src="https://img.shields.io/badge/Location-Greater_Phoenix,_AZ-333?style=flat-square&logo=googlemaps&logoColor=white" />
  <img src="https://img.shields.io/badge/F--1_OPT-Available_Now-555?style=flat-square" />
</p>

<!-- ===================== INTERACTIVE BOT CTA ===================== -->
<br/>

### 🤖 Meet my AI Security Assistant — it scans, greets you, and answers questions about me

<a href="https://poojakira.github.io/poojakira/">
  <img src="https://img.shields.io/badge/▶_LAUNCH_THE_SCANNER_BOT-00E5FF?style=for-the-badge&logo=probot&logoColor=black" alt="Launch the AI Security Assistant" />
</a>

<sub>An interactive, scanner-themed assistant trained on my profile — ask it about my projects, skills, or the roles I'm open to.</sub>

</div>

---

## 👋 The one line that explains my work

> **An agent that can call tools, assume IAM roles, and load model weights isn't answering questions anymore — it's making privileged decisions on your infrastructure.**
> That shift is what I build for.

I design and ship **open-source security tooling** that guards the boundaries where AI **agents, tools, identities, data, and model artifacts** meet. Not slideware — working, tested, reproducible tools.

> ⚠️ *These are research & portfolio projects: functional, tested, and open-source — but not hardened for enterprise scale. I'm honest about what they do and don't do.*

---

## 🧭 Three principles that drive everything I build

<div align="center">

| 🧩 Capability is **not** permission | 🔏 Permission is **not** provenance | 🪪 Identity is **not** authorization |
|:---:|:---:|:---:|
| An agent *can* call a tool — *should* it? | We approved the model — can we *prove* it's the trusted one? | A valid identity can still hide an attack path. |
| → MCP Gateway | → Provenance Scanner | → Identity Guard |

</div>

---

## 🔬 Flagship Scanners — Detection & Enforcement

<table>
<tr>
<td width="33%" valign="top">

### 🛡️ MCP Agent Security Gateway
`Beta` · `Python` · ⭐ 17

Inline gateway between an MCP client and downstream server. Inspects `tools/call` requests over **JSON-RPC** *before* execution and makes **allow/block** decisions.

**Detects:** prompt injection · PII leakage · shadow servers · exfiltration patterns
**Adds:** audit logging · rate limiting · telemetry

> *Capability is not permission.*

[→ Repo](https://github.com/poojakira/mcp-agent-security-gateway)

</td>
<td width="33%" valign="top">

### 🔍 HF Model Provenance Scanner
`Beta` · `Python`

Pre-load **supply-chain scanner** for Hugging Face repos. Catches **pickle exploits, typosquatting, and obfuscated payloads** by inspecting file headers — *without downloading model weights*.

**Bonus:** runtime `torch.load()` interception hook.

> *Permission is not provenance.*

[→ Repo](https://github.com/poojakira/hf-model-provenance-scanner)

</td>
<td width="33%" valign="top">

### 🔐 AWS Agent Identity Guard
`Beta` · `Python`

Static IAM linter for AI-agent roles. **25 deterministic checks** for privilege escalation, `iam:PassRole`, weak trust relationships & missing permission boundaries.

**Outputs:** text · JSON · **SARIF** · CI-ready exit codes.

> *Identity is not authorization.*

[→ Repo](https://github.com/poojakira/aws-agent-identity-guard)

</td>
</tr>
</table>

---

## 🧪 Research & Red-Team Labs

| Repository | What it does | Status |
|---|---|:---:|
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM / PGD / C&W attacks + robustness benchmarks (CIFAR-10 → MITRE ATLAS AML.T0043) | `Research` |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Automated jailbreak simulation & guardrail evaluation | `Beta` |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership-inference & model-inversion experiments | `Research` |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Statistical anomaly detection for training-data integrity | `Beta` |

## 🧱 Platforms & Integration

| Repository | What it does | Status |
|---|---|:---:|
| [unified-ml-security-platform](https://github.com/poojakira/unified-ml-security-platform) | Integration workspace wiring the tools together (CI, compose validation, scans, health checks) | `Beta` |
| [ml-security-command-center](https://github.com/poojakira/ml-security-command-center) | Unified command-center dashboard aggregating signals | `Research` |
| [mlsec-dashboards](https://github.com/poojakira/mlsec-dashboards) | Evidence-based live dashboards & demos | `Research` |
| [mlsec-benchmark-suite](https://github.com/poojakira/mlsec-benchmark-suite) | Cross-project benchmark harness | `Research` |

## ⚙️ Applied ML & Supporting Work

| Repository | What it does | Status |
|---|---|:---:|
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | NASA C-MAPSS RUL forecasting + adversarial sensor checks & secure MLOps | `Archived` |
| [attack-v19-core](https://github.com/poojakira/attack-v19-core) | MITRE ATT&CK v19 data models & technique lookup for Python | `Beta` |

---

## 🗺️ Frameworks I model threats against

<p>
  <img src="https://img.shields.io/badge/OWASP-Top_10_for_LLMs-000000?style=for-the-badge&logo=owasp&logoColor=white" />
  <img src="https://img.shields.io/badge/MITRE-ATLAS-C00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NIST-AI_RMF-0055A4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/MITRE-ATT%26CK_v19-C00?style=for-the-badge" />
</p>

---

## 🧰 Toolbox

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS_IAM-232F3E?style=flat-square&logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" />
</p>

---

## 📊 GitHub Activity

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=poojakira&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=poojakira&layout=compact&theme=tokyonight&hide_border=true" />

<img src="https://github-readme-streak-stats.herokuapp.com/?user=poojakira&theme=tokyonight&hide_border=true" />

</div>

---

## 🎓 Background

- 🎓 **MS, Information Technology** — Arizona State University (2026) · 3.87 GPA
- 📄 Published at **IEEE INDICON 2023** — reinforcement learning for personalized e-learning
- 🏆 **KSCST Research Grant** recipient (46th Series Student Project Programme)
- 🛡️ **AWS Academy — Cloud Security Foundations**

---

<div align="center">

### 💼 Open to: AI Security · AI/ML Security · Product Security for AI · Security Research Engineering

**Agentic AI · MCP/Tool Security · IAM & Least Privilege · Model Supply-Chain · Adversarial Testing**

*Available now · F-1 OPT · Open to relocation*

<a href="https://linkedin.com/in/poojakiran"><img src="https://img.shields.io/badge/Let's_connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>

<img src="https://komarev.com/ghpvc/?username=poojakira&style=flat-square&color=00E5FF" alt="Profile views" />

</div>
