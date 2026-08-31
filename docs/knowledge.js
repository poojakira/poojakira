/* =====================================================================
   KNOWLEDGE BASE — facts about Pooja Kiran Bharadwaj.
   The bot matches a user question against the `keywords` of each intent
   and returns the best-scoring `answer`. Edit freely to add/adjust facts.
   ===================================================================== */

const KB = {
  greetings: [
    "Hi! 👋 I'm Pooja's AI Security Assistant. Ask me anything about her work, projects, skills, or background.",
    "Hello! I'm a scanner-bot trained on Pooja's profile. Try asking about her scanners, her IAM tool, or what roles she's open to."
  ],

  fallback:
    "I'm focused on Pooja's background, projects, skills, and experience. Try asking about her <strong>MCP Gateway</strong>, <strong>model provenance scanner</strong>, <strong>IAM tool</strong>, her <strong>education</strong>, or <strong>what roles she wants</strong>. You can also reach her on <a href='https://linkedin.com/in/poojakiran' target='_blank'>LinkedIn</a>.",

  intents: [
    {
      id: "who",
      keywords: ["who is","who's","who are","yourself","introduce","biography","summary","tell me about pooja"],
      answer: "<strong>Pooja Kiran Bharadwaj</strong> is an <strong>AI Security Engineer</strong> who secures the boundaries where AI agents, tools, identities, data, and model artifacts meet. Her guiding idea: <em>AI becomes a different security problem the moment it can act</em> — not just answer. She builds and evaluates open-source security tooling across agentic AI security, MCP/tool access, IAM, model supply-chain security, adversarial ML, and model privacy."
    },
    {
      id: "principles",
      keywords: ["principle","philosophy","believe","approach","mantra","motto","why"],
      answer: "Three principles drive her work:<br>🧩 <strong>Capability is not permission</strong> — an agent <em>can</em> call a tool; should it?<br>🔏 <strong>Permission is not provenance</strong> — we approved a model; can we <em>prove</em> it's the trusted one?<br>🪪 <strong>Identity is not authorization</strong> — a valid identity can still hide an attack path."
    },
    {
      id: "mcp",
      keywords: ["mcp","gateway","tool call","agent tool","json-rpc","prompt injection","exfiltration","interception"],
      answer: "🛡️ <strong>MCP Agent Security Gateway</strong> — an inline gateway that sits between an MCP client and a downstream server, inspecting <code>tools/call</code> requests over JSON-RPC <em>before</em> execution and making allow/block decisions. It detects prompt injection, PII leakage, shadow servers, and exfiltration patterns, and adds audit logging, rate limiting, and telemetry. Principle: <em>Capability is not permission.</em><br>→ <a href='https://github.com/poojakira/mcp-agent-security-gateway' target='_blank'>See the repo</a> (Python, ~17★)"
    },
    {
      id: "provenance",
      keywords: ["provenance","hugging face","huggingface","hf","supply chain","pickle","typosquat","model artifact","torch.load","scanner model"],
      answer: "🔍 <strong>HF Model Provenance Scanner</strong> — a pre-load supply-chain scanner for Hugging Face model repos. It catches pickle exploits, typosquatting/impersonation, and obfuscated payloads by inspecting file headers <em>without downloading the model weights</em>, plus a runtime <code>torch.load()</code> interception hook. Principle: <em>Permission is not provenance.</em><br>→ <a href='https://github.com/poojakira/hf-model-provenance-scanner' target='_blank'>See the repo</a>"
    },
    {
      id: "iam",
      keywords: ["iam","identity guard","aws","policy","privilege","passrole","least privilege","trust relationship","sarif","permission boundary"],
      answer: "🔐 <strong>AWS Agent Identity Guard</strong> — a static IAM linter for AI-agent roles with <strong>25 deterministic checks</strong> for privilege escalation, <code>iam:PassRole</code>, wildcard access, weak trust relationships, and missing permission boundaries. It outputs text, JSON, and SARIF with CI-ready exit codes. Principle: <em>Identity is not authorization.</em><br>→ <a href='https://github.com/poojakira/aws-agent-identity-guard' target='_blank'>See the repo</a>"
    },
    {
      id: "projects",
      keywords: ["project","projects","built","build","portfolio","repos","repositories","flagship","scanners"],
      answer: "Her three flagship scanners are:<br>🛡️ <strong>MCP Agent Security Gateway</strong> (agent tool-call inspection)<br>🔍 <strong>HF Model Provenance Scanner</strong> (model supply-chain)<br>🔐 <strong>AWS Agent Identity Guard</strong> (IAM linting)<br><br>Plus research/red-team labs: adversarial-ml-lab, llm-redteam-framework, model-privacy-attacks, and dataset-poisoning-detector. Ask about any one of them!"
    },
    {
      id: "research",
      keywords: ["research","adversarial","red team","redteam","jailbreak","membership inference","privacy attack","poisoning","fgsm","pgd"],
      answer: "Her research & red-team labs cover: <strong>adversarial ML</strong> (FGSM/PGD/C&W, mapped to MITRE ATLAS AML.T0043), <strong>LLM jailbreak simulation & guardrail evaluation</strong>, <strong>membership-inference & model-inversion</strong> privacy attacks, and <strong>dataset-poisoning detection</strong>. She emphasizes reproducible evaluation and clearly documented limitations."
    },
    {
      id: "frameworks",
      keywords: ["framework","owasp","mitre","atlas","nist","att&ck","attack","standard","taxonomy"],
      answer: "She models threats against <strong>OWASP Top 10 for LLMs</strong>, <strong>MITRE ATLAS</strong>, <strong>NIST AI RMF</strong>, and <strong>MITRE ATT&CK v19</strong>."
    },
    {
      id: "skills",
      keywords: ["skill","skills","tech","stack","tools","languages","toolbox","expertise","good at"],
      answer: "Core skills: <strong>AI/ML Security, AI Agent Security, Model Supply-Chain Security, LLM & RAG Security Testing, IAM & Least Privilege</strong>. Toolbox: Python, PyTorch, AWS IAM, Docker, GitHub Actions, FastAPI, Pytest."
    },
    {
      id: "experience",
      keywords: ["experience","job","work history","career","employment","aerosec","teaching assistant","ta","honeywell"],
      answer: "Experience:<br>• <strong>Independent AI Security Researcher & Engineer</strong> (Aug 2024–present) — built the MCP Gateway, AWS Agent Identity Guard, and HF Provenance Scanner.<br>• <strong>Business Compliance Lead & Market/Cost Analyst — AEROSEC</strong> at ASU's Technology Innovation Lab (with Honeywell Aerospace), Aug–Dec 2025.<br>• <strong>Graduate Teaching Assistant (IT Grader)</strong> at ASU's Ira A. Fulton Schools of Engineering, Jan–Oct 2025."
    },
    {
      id: "education",
      keywords: ["education","study","degree","university","school","asu","college","gpa","masters","btech","ramaiah"],
      answer: "🎓 <strong>MS, Information Technology</strong> — Arizona State University (2024–2026), 3.87 GPA. <br>🎓 <strong>BTech, Computer Science & Engineering</strong> — M. S. Ramaiah University of Applied Sciences (2019–2023), 8.44 CGPA."
    },
    {
      id: "publications",
      keywords: ["publication","paper","ieee","indicon","research paper","published","reinforcement learning"],
      answer: "📄 Published at <strong>IEEE INDICON 2023</strong>: <em>“A Personalized E-Learning System Using Reinforcement Learning Through Satellite”</em> (presented at NIT Warangal). She also received the <strong>KSCST 46th Series Research Grant</strong> for undergraduate research in reinforcement learning and applied AI."
    },
    {
      id: "certs",
      keywords: ["certification","certificate","cert","aws academy","badge","credential","license"],
      answer: "Certifications: <strong>AWS Academy — Cloud Security Foundations</strong> (Nov 2025) and the <strong>Technology Innovation Lab — Honeywell Aerospace & ASU</strong> credential (Nov 2025)."
    },
    {
      id: "hiring",
      keywords: ["hire","hiring","open to","roles","opportunity","opportunities","available","job seeking","looking for","recruit","full time","opt","visa","relocate","relocation"],
      answer: "✅ She's <strong>open to full-time roles now</strong> in AI Security, AI/ML Security, Product Security for AI, Security Research Engineering, and AI Systems Security — especially agentic AI, MCP/tool security, IAM & access control, model supply-chain security, adversarial testing, and secure AI infrastructure.<br><strong>Available now · F-1 OPT · open to relocation.</strong> Reach out on <a href='https://linkedin.com/in/poojakiran' target='_blank'>LinkedIn</a>."
    },
    {
      id: "contact",
      keywords: ["contact","email","reach","linkedin","github","connect","get in touch","message","location","where"],
      answer: "📫 You can reach Pooja here:<br>• <a href='https://linkedin.com/in/poojakiran' target='_blank'>LinkedIn</a><br>• <a href='https://github.com/poojakira' target='_blank'>GitHub</a><br>• <a href='mailto:pkiran1@asu.edu'>pkiran1@asu.edu</a><br>📍 Based in the Greater Phoenix Area, AZ."
    },
    {
      id: "thanks",
      keywords: ["thank","thanks","appreciate","cool","awesome","nice","great"],
      answer: "You're welcome! 😊 Feel free to ask anything else — or connect with Pooja on <a href='https://linkedin.com/in/poojakiran' target='_blank'>LinkedIn</a>."
    }
  ]
};
