/* =====================================================================
   KNOWLEDGE BASE — facts about Pooja Kiran Bharadwaj.
   Each intent has:
     keywords[] — what the user might type
     answer     — HTML shown in the chat (confident, optimistic tone)
     speech     — clean plain-text version the voice reads aloud
   ===================================================================== */

const KB = {
  greetings: [
    {
      answer: "Hi there! 👋 I'm Pooja's AI Security Assistant — so glad you stopped by. Ask me anything about her work, her security scanners, her skills, or the roles she's excited about. What would you like to know?",
      speech: "Hi there! I'm Pooja's A.I. Security Assistant, and I'm so glad you stopped by. Ask me anything about her work, her security scanners, her skills, or the roles she's excited about. What would you like to know?"
    },
    {
      answer: "Hey! 😊 Welcome — I'm Pooja's personal AI assistant. She builds security tools that keep AI agents, models, and identities safe, and I'd love to tell you all about it. Go ahead, ask me anything!",
      speech: "Hey! Welcome. I'm Pooja's personal A.I. assistant. She builds security tools that keep A.I. agents, models, and identities safe, and I'd love to tell you all about it. Go ahead, ask me anything!"
    }
  ],

  fallback: {
    answer: "That's a great question — though it's a little outside what I know about Pooja! 😊 I'm happiest talking about her <strong>MCP Gateway</strong>, her <strong>model provenance scanner</strong>, her <strong>AWS IAM tool</strong>, her <strong>research</strong>, or the <strong>roles she's open to</strong>. Try one of those, or connect with her directly on <a href='https://linkedin.com/in/poojakiran' target='_blank'>LinkedIn</a>!",
    speech: "That's a great question, though it's a little outside what I know about Pooja! I'm happiest talking about her security scanners, her research, or the roles she's open to. Try one of those, or connect with her directly on LinkedIn!"
  },

  intents: [
    {
      id: "who",
      keywords: ["who is","who's","who are","yourself","introduce","biography","summary","tell me about pooja"],
      answer: "<strong>Pooja Kiran Bharadwaj</strong> is an <strong>AI Security Engineer</strong>, and honestly, her work is right at the frontier. 🚀 She secures the boundaries where AI agents, tools, identities, data, and model artifacts all meet. Her big idea is simple but powerful: <em>AI becomes a whole new security problem the moment it can act — not just answer.</em> She designs and ships open-source tooling across agentic AI security, MCP and tool access, IAM, model supply-chain security, adversarial ML, and model privacy.",
      speech: "Pooja Kiran Bharadwaj is an A.I. Security Engineer, and honestly, her work is right at the frontier. She secures the boundaries where A.I. agents, tools, identities, data, and model artifacts all meet. Her big idea is simple but powerful: A.I. becomes a whole new security problem the moment it can act, not just answer. She designs and ships open-source tooling across agentic A.I. security, tool access, identity, model supply-chain security, adversarial machine learning, and model privacy."
    },
    {
      id: "principles",
      keywords: ["principle","philosophy","believe","approach","mantra","motto","why"],
      answer: "I love this one! 💡 Three clear principles drive everything Pooja builds:<br>🧩 <strong>Capability is not permission</strong> — an agent <em>can</em> call a tool, but should it?<br>🔏 <strong>Permission is not provenance</strong> — we approved a model, but can we <em>prove</em> it's the trusted one?<br>🪪 <strong>Identity is not authorization</strong> — a valid identity can still hide an attack path. Each principle maps directly to a tool she's built.",
      speech: "I love this one! Three clear principles drive everything Pooja builds. First: capability is not permission. An agent can call a tool, but should it? Second: permission is not provenance. We approved a model, but can we prove it's the trusted one? And third: identity is not authorization. A valid identity can still hide an attack path. Each principle maps directly to a tool she's built."
    },
    {
      id: "mcp",
      keywords: ["mcp","gateway","tool call","agent tool","json-rpc","prompt injection","exfiltration","interception"],
      answer: "🛡️ The <strong>MCP Agent Security Gateway</strong> is one of my favorites! It's an inline gateway that sits between an MCP client and a downstream server, inspecting <code>tools/call</code> requests over JSON-RPC <em>before</em> they run — and making smart allow or block decisions. It catches prompt injection, PII leakage, shadow servers, and exfiltration patterns, plus it adds audit logging, rate limiting, and telemetry. The principle behind it: <em>capability is not permission.</em><br>→ <a href='https://github.com/poojakira/mcp-agent-security-gateway' target='_blank'>Take a look at the repo!</a>",
      speech: "The M.C.P. Agent Security Gateway is one of my favorites! It's an inline gateway that sits between an agent and a downstream server, inspecting tool-call requests before they run, and making smart allow or block decisions. It catches prompt injection, P.I.I. leakage, shadow servers, and exfiltration patterns, plus it adds audit logging, rate limiting, and telemetry. The principle behind it: capability is not permission."
    },
    {
      id: "provenance",
      keywords: ["provenance","hugging face","huggingface","hf","supply chain","pickle","typosquat","model artifact","torch.load","scanner model"],
      answer: "🔍 The <strong>HF Model Provenance Scanner</strong> is such a clever piece of work! It's a pre-load supply-chain scanner for Hugging Face model repos. It catches pickle exploits, typosquatting, and obfuscated payloads just by inspecting file headers — <em>without even downloading the model weights</em>. It even ships with a runtime <code>torch.load()</code> interception hook. The principle: <em>permission is not provenance.</em><br>→ <a href='https://github.com/poojakira/hf-model-provenance-scanner' target='_blank'>Check out the repo!</a>",
      speech: "The Hugging Face Model Provenance Scanner is such a clever piece of work! It's a pre-load supply-chain scanner for Hugging Face model repos. It catches pickle exploits, typosquatting, and obfuscated payloads just by inspecting file headers, without even downloading the model weights. It even ships with a runtime interception hook. The principle: permission is not provenance."
    },
    {
      id: "iam",
      keywords: ["iam","identity guard","aws","policy","privilege","passrole","least privilege","trust relationship","sarif","permission boundary"],
      answer: "🔐 The <strong>AWS Agent Identity Guard</strong> is a real workhorse! It's a static IAM linter for AI-agent roles with <strong>25 deterministic checks</strong> — spotting privilege escalation, <code>iam:PassRole</code> risks, wildcard access, weak trust relationships, and missing permission boundaries. And it plays beautifully with engineering workflows: it outputs text, JSON, and SARIF with CI-ready exit codes. The principle: <em>identity is not authorization.</em><br>→ <a href='https://github.com/poojakira/aws-agent-identity-guard' target='_blank'>See the repo!</a>",
      speech: "The A.W.S. Agent Identity Guard is a real workhorse! It's a static I.A.M. linter for A.I.-agent roles with twenty-five deterministic checks, spotting privilege escalation, pass-role risks, wildcard access, weak trust relationships, and missing permission boundaries. And it plays beautifully with engineering workflows: it outputs text, JSON, and SARIF with C.I.-ready exit codes. The principle: identity is not authorization."
    },
    {
      id: "projects",
      keywords: ["project","projects","built","build","portfolio","repos","repositories","flagship","scanners"],
      answer: "She's built a lot to be proud of! 🌟 Her three flagship scanners are:<br>🛡️ <strong>MCP Agent Security Gateway</strong> — agent tool-call inspection<br>🔍 <strong>HF Model Provenance Scanner</strong> — model supply-chain safety<br>🔐 <strong>AWS Agent Identity Guard</strong> — IAM linting<br><br>And there's more — research and red-team labs like adversarial-ml-lab, llm-redteam-framework, model-privacy-attacks, and dataset-poisoning-detector. Ask me about any one, I'd love to dive in!",
      speech: "She's built a lot to be proud of! Her three flagship scanners are: the M.C.P. Agent Security Gateway for agent tool-call inspection, the Hugging Face Model Provenance Scanner for model supply-chain safety, and the A.W.S. Agent Identity Guard for I.A.M. linting. And there's more, including research and red-team labs. Ask me about any one, I'd love to dive in!"
    },
    {
      id: "research",
      keywords: ["research","adversarial","red team","redteam","jailbreak","membership inference","privacy attack","poisoning","fgsm","pgd"],
      answer: "Her research is genuinely exciting! 🔬 Her red-team and research labs cover <strong>adversarial ML</strong> (FGSM, PGD, and C&W attacks, mapped to MITRE ATLAS AML.T0043), <strong>LLM jailbreak simulation and guardrail evaluation</strong>, <strong>membership-inference and model-inversion</strong> privacy attacks, and <strong>dataset-poisoning detection</strong>. What I admire most: she's rigorous about reproducible evaluation and refreshingly honest about limitations.",
      speech: "Her research is genuinely exciting! Her red-team and research labs cover adversarial machine learning, including F.G.S.M., P.G.D., and C and W attacks. She also works on L.L.M. jailbreak simulation and guardrail evaluation, membership-inference and model-inversion privacy attacks, and dataset-poisoning detection. What I admire most: she's rigorous about reproducible evaluation and refreshingly honest about limitations."
    },
    {
      id: "frameworks",
      keywords: ["framework","owasp","mitre","atlas","nist","att&ck","attack","standard","taxonomy"],
      answer: "She grounds her threat modeling in the best industry standards 📐 — the <strong>OWASP Top 10 for LLMs</strong>, <strong>MITRE ATLAS</strong>, the <strong>NIST AI RMF</strong>, and <strong>MITRE ATT&CK v19</strong>. That's what keeps her work credible and aligned with how the field actually thinks about risk.",
      speech: "She grounds her threat modeling in the best industry standards: the OWASP Top Ten for L.L.M.s, MITRE ATLAS, the NIST A.I. Risk Management Framework, and MITRE ATT and CK version nineteen. That's what keeps her work credible and aligned with how the field actually thinks about risk."
    },
    {
      id: "skills",
      keywords: ["skill","skills","tech","stack","tools","languages","toolbox","expertise","good at"],
      answer: "She's got a strong, focused toolkit! 💪 Her core strengths are <strong>AI/ML Security, AI Agent Security, Model Supply-Chain Security, LLM &amp; RAG Security Testing, and IAM &amp; Least Privilege</strong>. And her hands-on stack includes Python, PyTorch, AWS IAM, Docker, GitHub Actions, FastAPI, and Pytest. She's the kind of engineer who both designs the threat model <em>and</em> ships the code.",
      speech: "She's got a strong, focused toolkit! Her core strengths are A.I. and M.L. security, A.I. agent security, model supply-chain security, L.L.M. and RAG security testing, and identity and least privilege. Her hands-on stack includes Python, PyTorch, A.W.S. I.A.M., Docker, GitHub Actions, FastAPI, and Pytest. She's the kind of engineer who both designs the threat model and ships the code."
    },
    {
      id: "experience",
      keywords: ["experience","job","work history","career","employment","aerosec","teaching assistant","ta","honeywell"],
      answer: "Here's her journey so far 🧭:<br>• <strong>Independent AI Security Researcher &amp; Engineer</strong> (Aug 2024–present) — where she built the MCP Gateway, AWS Agent Identity Guard, and HF Provenance Scanner.<br>• <strong>Business Compliance Lead &amp; Market/Cost Analyst — AEROSEC</strong> at ASU's Technology Innovation Lab, in partnership with Honeywell Aerospace (Aug–Dec 2025).<br>• <strong>Graduate Teaching Assistant</strong> at ASU's Ira A. Fulton Schools of Engineering (Jan–Oct 2025). She brings both the engineering depth and the business perspective!",
      speech: "Here's her journey so far. Since August twenty twenty-four, she's been an independent A.I. Security Researcher and Engineer, where she built the M.C.P. Gateway, the A.W.S. Agent Identity Guard, and the Provenance Scanner. She also served as Business Compliance Lead and Market and Cost Analyst for AEROSEC at A.S.U.'s Technology Innovation Lab, in partnership with Honeywell Aerospace. And she was a Graduate Teaching Assistant at A.S.U.'s Fulton Schools of Engineering. She brings both the engineering depth and the business perspective!"
    },
    {
      id: "education",
      keywords: ["education","study","degree","university","school","asu","college","gpa","masters","btech","ramaiah"],
      answer: "She's got a strong academic foundation 🎓:<br>• <strong>MS, Information Technology</strong> — Arizona State University (2024–2026), with a 3.87 GPA.<br>• <strong>BTech, Computer Science &amp; Engineering</strong> — M. S. Ramaiah University of Applied Sciences (2019–2023), 8.44 CGPA. Consistently excellent, and clearly driven!",
      speech: "She's got a strong academic foundation. She's earning her Master's in Information Technology at Arizona State University, graduating in twenty twenty-six with a three point eight seven G.P.A. And she holds a Bachelor's in Computer Science and Engineering from M. S. Ramaiah University of Applied Sciences, with an eight point four four C.G.P.A. Consistently excellent, and clearly driven!"
    },
    {
      id: "publications",
      keywords: ["publication","paper","ieee","indicon","research paper","published","reinforcement learning"],
      answer: "Yes, she's a published researcher! 📄 Her paper <em>“A Personalized E-Learning System Using Reinforcement Learning Through Satellite”</em> was published at <strong>IEEE INDICON 2023</strong> and presented at NIT Warangal. She also earned the <strong>KSCST 46th Series Research Grant</strong> for undergraduate research in reinforcement learning and applied AI. Impressive, right?",
      speech: "Yes, she's a published researcher! Her paper, A Personalized E-Learning System Using Reinforcement Learning Through Satellite, was published at I.E.E.E. INDICON twenty twenty-three and presented at N.I.T. Warangal. She also earned the K.S.C.S.T. forty-sixth series research grant for undergraduate research in reinforcement learning and applied A.I. Impressive, right?"
    },
    {
      id: "certs",
      keywords: ["certification","certificate","cert","aws academy","badge","credential","license"],
      answer: "Absolutely! ✅ She holds the <strong>AWS Academy — Cloud Security Foundations</strong> credential (Nov 2025) and a <strong>Technology Innovation Lab — Honeywell Aerospace &amp; ASU</strong> credential (Nov 2025). She keeps leveling up her cloud and security foundations.",
      speech: "Absolutely! She holds the A.W.S. Academy Cloud Security Foundations credential from November twenty twenty-five, and a Technology Innovation Lab credential with Honeywell Aerospace and A.S.U., also from November twenty twenty-five. She keeps leveling up her cloud and security foundations."
    },
    {
      id: "hiring",
      keywords: ["hire","hiring","open to","roles","opportunity","opportunities","available","job seeking","looking for","recruit","full time","opt","visa","relocate","relocation"],
      answer: "Yes — and this is the exciting part! 🎯 Pooja is <strong>open to full-time roles right now</strong> in AI Security, AI/ML Security, Product Security for AI, Security Research Engineering, and AI Systems Security. She's especially energized by agentic AI, MCP and tool security, IAM and access control, model supply-chain security, adversarial testing, and secure AI infrastructure.<br><strong>She's available now, on F-1 OPT, and open to relocation.</strong> If your team is building in this space, she'd be a fantastic addition — <a href='https://linkedin.com/in/poojakiran' target='_blank'>reach out on LinkedIn!</a>",
      speech: "Yes, and this is the exciting part! Pooja is open to full-time roles right now, in A.I. Security, A.I. and M.L. Security, Product Security for A.I., Security Research Engineering, and A.I. Systems Security. She's especially energized by agentic A.I., tool security, identity and access control, model supply-chain security, adversarial testing, and secure A.I. infrastructure. She's available now, on F-1 O.P.T., and open to relocation. If your team is building in this space, she'd be a fantastic addition. Reach out on LinkedIn!"
    },
    {
      id: "contact",
      keywords: ["contact","email","reach","linkedin","github","connect","get in touch","message","location","where"],
      answer: "I'd love to connect you! 📫<br>• <a href='https://linkedin.com/in/poojakiran' target='_blank'>LinkedIn</a><br>• <a href='https://github.com/poojakira' target='_blank'>GitHub</a><br>• <a href='mailto:pkiran1@asu.edu'>pkiran1@asu.edu</a><br>📍 She's based in the Greater Phoenix Area, Arizona. Don't be shy — she loves talking security!",
      speech: "I'd love to connect you! You can find Pooja on LinkedIn and GitHub, or email her at p kiran one at a.s.u. dot e.d.u. She's based in the Greater Phoenix Area, Arizona. Don't be shy, she loves talking security!"
    },
    {
      id: "thanks",
      keywords: ["thank","thanks","appreciate","cool","awesome","nice","great"],
      answer: "Aww, you're so welcome! 😊 It was a pleasure. Ask me anything else, or connect with Pooja directly on <a href='https://linkedin.com/in/poojakiran' target='_blank'>LinkedIn</a> — she'd be thrilled to hear from you!",
      speech: "Aww, you're so welcome! It was a pleasure. Ask me anything else, or connect with Pooja directly on LinkedIn. She'd be thrilled to hear from you!"
    }
  ]
};
