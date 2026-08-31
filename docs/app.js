/* =====================================================================
   AI SECURITY ASSISTANT — client-side bot (no backend, no API keys).
   Boot sequence → scanner greeting → intent-matched Q&A → speaks aloud.
   Tone: confident & optimistic. Voice: female (Web Speech API).
   ===================================================================== */

/* ---------- element refs ---------- */
const bootEl   = document.getElementById("boot");
const bootLog  = document.getElementById("bootLog");
const appEl    = document.getElementById("app");
const messages = document.getElementById("messages");
const chipsEl  = document.getElementById("chips");
const form     = document.getElementById("composer");
const input    = document.getElementById("input");
const statusText = document.getElementById("statusText");

/* =====================================================================
   VOICE (Web Speech API) — picks the best available female English voice.
   ===================================================================== */
const Voice = {
  enabled: true,
  voice: null,
  supported: ("speechSynthesis" in window),

  pickVoice(){
    if(!this.supported) return;
    const voices = window.speechSynthesis.getVoices();
    if(!voices.length) return;
    // Preference order: known female English voices, then any female-sounding, then any English.
    const preferred = [
      "google uk english female","google us english","microsoft zira","microsoft aria",
      "microsoft jenny","samantha","victoria","karen","moira","tessa","fiona","serena","allison","ava"
    ];
    const byName = n => voices.find(v => v.name.toLowerCase().includes(n));
    for(const p of preferred){ const m = byName(p); if(m){ this.voice = m; return; } }
    // fallback: any english voice
    this.voice = voices.find(v => /^en(-|_|$)/i.test(v.lang)) || voices[0];
  },

  speak(text){
    if(!this.supported || !this.enabled || !text) return;
    try{
      window.speechSynthesis.cancel();               // stop any prior utterance
      const u = new SpeechSynthesisUtterance(text);
      if(this.voice) u.voice = this.voice;
      u.lang  = (this.voice && this.voice.lang) || "en-US";
      u.rate  = 1.02;   // lively but clear
      u.pitch = 1.15;   // slightly higher = warmer/female
      u.volume = 1;
      window.speechSynthesis.speak(u);
    }catch(e){ /* ignore speech errors */ }
  },

  stop(){ if(this.supported) window.speechSynthesis.cancel(); }
};
if(Voice.supported){
  Voice.pickVoice();
  window.speechSynthesis.onvoiceschanged = () => Voice.pickVoice();
}

/* mute / unmute toggle button (injected into the chat header) */
function buildVoiceToggle(){
  const btn = document.createElement("button");
  btn.id = "voiceToggle";
  btn.type = "button";
  btn.className = "voice-toggle";
  btn.title = "Toggle voice";
  const render = () => { btn.textContent = Voice.enabled ? "🔊 Voice on" : "🔇 Voice off"; };
  render();
  btn.onclick = () => {
    Voice.enabled = !Voice.enabled;
    if(!Voice.enabled) Voice.stop();
    render();
  };
  const head = document.querySelector(".chat-head");
  if(head) head.appendChild(btn);
}

/* ---------- boot sequence ---------- */
const bootLines = [
  "> initializing ai-security-assistant v1.0 ...",
  "> loading knowledge base ......... <span class='ok'>[OK]</span>",
  "> mounting scanner modules ....... <span class='ok'>[OK]</span>",
  "> calibrating biometric scanner .. <span class='ok'>[OK]</span>",
  "> verifying identity: <span class='ok'>Pooja Kiran Bharadwaj</span>",
  "> threat models: OWASP-LLM · MITRE ATLAS · NIST AI RMF <span class='ok'>[OK]</span>",
  "> status: <span class='ok'>ONLINE</span> — awaiting operator query",
];

let li = 0;
function runBoot(){
  if(li < bootLines.length){
    bootLog.innerHTML += bootLines[li] + "\n";
    li++;
    setTimeout(runBoot, 360);
  } else {
    bootLog.innerHTML += "<span class='cursor'>█</span>";
    setTimeout(revealApp, 700);
  }
}

function revealApp(){
  bootEl.classList.add("done");
  appEl.setAttribute("aria-hidden","false");
  appEl.classList.add("show");
  buildVoiceToggle();
  setTimeout(greet, 500);
}

/* ---------- greeting ---------- */
function greet(){
  const hi = KB.greetings[Math.floor(Math.random()*KB.greetings.length)];
  botSay(hi, () => renderChips(defaultChips));
}

/* ---------- suggested question chips ---------- */
const defaultChips = [
  "Who is Pooja?",
  "What are her flagship projects?",
  "Tell me about the MCP Gateway",
  "What roles is she open to?",
  "What's her education?",
  "How do I contact her?"
];

function renderChips(list){
  chipsEl.innerHTML = "";
  list.forEach(text => {
    const c = document.createElement("button");
    c.type = "button";
    c.className = "chip";
    c.textContent = text;
    c.onclick = () => { handleUser(text); };
    chipsEl.appendChild(c);
  });
}

/* ---------- rendering messages ---------- */
function addMsg(html, who){
  const m = document.createElement("div");
  m.className = "msg " + who;
  m.innerHTML = html;
  messages.appendChild(m);
  messages.scrollTop = messages.scrollHeight;
  return m;
}

/* accepts a response object {answer, speech} (or a plain string) */
function botSay(resp, done){
  const html   = (resp && resp.answer)  ? resp.answer  : String(resp);
  const speech = (resp && resp.speech)  ? resp.speech  : stripHtml(html);

  const t = addMsg("<span class='typing'><span></span><span></span><span></span></span>","bot");
  statusText.textContent = "typing…";
  const delay = Math.min(1400, 500 + html.length * 5);
  setTimeout(() => {
    t.innerHTML = html;
    statusText.textContent = "online";
    messages.scrollTop = messages.scrollHeight;
    Voice.speak(speech);
    if(done) done();
  }, delay);
}

function stripHtml(html){
  const tmp = document.createElement("div");
  tmp.innerHTML = html;
  return (tmp.textContent || tmp.innerText || "").replace(/\s+/g," ").trim();
}

/* ---------- intent matching ---------- */
function normalize(s){ return s.toLowerCase().replace(/[^a-z0-9\s&.]/g," "); }

function findAnswer(query){
  const q = normalize(query);
  const words = q.split(/\s+/).filter(Boolean);

  // greeting shortcut
  if(/^(hi|hey|hello|yo|hola|sup|greetings)\b/.test(q))
    return KB.greetings[Math.floor(Math.random()*KB.greetings.length)];

  let best = null, bestScore = 0;
  for(const intent of KB.intents){
    let score = 0;
    for(const kw of intent.keywords){
      const k = normalize(kw);
      if(k.includes(" ")){
        if(q.includes(k)) score += 5;
      } else {
        if(words.includes(k)) score += 3;
        else if(k.length > 4 && words.some(w => w.length > 4 && (w.startsWith(k) || k.startsWith(w)))) score += 2;
      }
    }
    if(score > bestScore){ bestScore = score; best = intent; }
  }
  if(best && bestScore >= 2) return best;   // return full intent object
  return KB.fallback;
}

/* ---------- follow-up chips ---------- */
const followupChips = [
  "Tell me about the model provenance scanner",
  "What about the AWS IAM tool?",
  "What research has she done?",
  "What frameworks does she use?",
  "Is she open to work?",
  "What are her skills?"
];

/* ---------- handle a user turn ---------- */
function handleUser(text){
  const clean = text.trim();
  if(!clean) return;
  addMsg(clean, "user");
  input.value = "";
  chipsEl.innerHTML = "";
  const resp = findAnswer(clean);
  botSay(resp, () => {
    const shuffled = [...followupChips].sort(() => Math.random()-0.5).slice(0,4);
    renderChips(shuffled);
  });
}

/* ---------- events ---------- */
form.addEventListener("submit", e => {
  e.preventDefault();
  handleUser(input.value);
});

/* ---------- go ---------- */
runBoot();
