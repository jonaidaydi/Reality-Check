import os
import json
from pathlib import Path

import gradio as gr
import httpx
from dotenv import load_dotenv

import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
from PIL import Image

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY", "").strip()
HF_MODEL = os.getenv("HF_MODEL", "meta-llama/Llama-3.1-8B-Instruct:cerebras").strip()
HF_API_URL = "https://router.huggingface.co/v1/chat/completions"


# ---------- HELPERS ----------

def load_prompt(name: str) -> str:
    return (Path("prompts") / name).read_text(encoding="utf-8")


def safe_limit(text: str, max_chars: int = 8000) -> str:
    return (text or "")[:max_chars]


def get_text(file, text: str) -> str:
    if file is not None:
        file_path = getattr(file, "name", None)

        if file_path:
            lower = file_path.lower()

            if lower.endswith((".png", ".jpg", ".jpeg", ".webp")):
                try:
                    img = Image.open(file_path)
                    return pytesseract.image_to_string(img, lang="deu+eng")
                except Exception as e:
                    return f"OCR Fehler: {e}"

            return Path(file_path).read_text(encoding="utf-8", errors="ignore")

    return (text or "").strip()


def call_hf_chat(system_prompt: str, user_text: str) -> str:
    if not HF_API_KEY:
        return json.dumps({
            "tendenz": "Fehler",
            "red_flag_score": 0,
            "verbindlichkeit": 0,
            "konsistenz": 0,
            "emotionale_klarheit": 0,
            "red_flags": ["HF_API_KEY fehlt in .env"],
            "kurzanalyse": "Es konnte keine Modellanfrage gesendet werden.",
            "hinweis": "Trage deinen Hugging Face Token in die .env ein.",
            "fazit": "Sobald der API-Schlüssel gesetzt ist, kann die Analyse normal laufen."
        }, ensure_ascii=False)

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": HF_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ],
        "temperature": 0.35,
        "max_tokens": 900,
    }

    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(HF_API_URL, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        return json.dumps({
            "tendenz": "Fehler",
            "red_flag_score": 0,
            "verbindlichkeit": 0,
            "konsistenz": 0,
            "emotionale_klarheit": 0,
            "red_flags": [f"API Fehler: {str(e)}"],
            "kurzanalyse": "Die Anfrage an das Modell ist fehlgeschlagen.",
            "hinweis": "Prüfe Modellname, Internetverbindung und API-Key.",
            "fazit": "Technisch ist gerade keine verlässliche Einschätzung möglich."
        }, ensure_ascii=False)


def parse_json(raw: str) -> dict:
    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start == -1 or end <= 0:
            raise ValueError("Kein JSON gefunden")
        return json.loads(raw[start:end])
    except Exception:
        return {
            "tendenz": "Unklar",
            "red_flag_score": 0,
            "verbindlichkeit": 0,
            "konsistenz": 0,
            "emotionale_klarheit": 0,
            "red_flags": ["Antwort konnte nicht sauber strukturiert werden."],
            "kurzanalyse": raw[:700],
            "hinweis": "Bitte versuche es mit etwas mehr Kontext oder kürzerem Text erneut.",
            "fazit": "Auf Basis der aktuellen Eingabe ist noch keine wirklich belastbare Gesamteinschätzung möglich."
        }


def clamp_score(value) -> int:
    try:
        value = int(value)
    except Exception:
        value = 0
    return max(0, min(10, value))


def score_color(value: int) -> str:
    if value >= 7:
        return "#ff5c5c"
    if value >= 4:
        return "#ff9f43"
    return "#5ad18a"


def tendency_badge(tendency: str, score: int) -> str:
    color = score_color(score)
    return f"""
    <div style="
        display:inline-flex;
        align-items:center;
        gap:10px;
        padding:10px 14px;
        border-radius:999px;
        background:rgba(255,255,255,0.04);
        border:1px solid rgba(255,255,255,0.08);
        margin-bottom:16px;
        font-weight:700;
        font-size:15px;
    ">
        <span style="
            width:10px;
            height:10px;
            border-radius:50%;
            background:{color};
            box-shadow:0 0 10px {color};
            display:inline-block;
        "></span>
        <span>{tendency}</span>
    </div>
    """


def meter(label: str, value: int, invert: bool = False) -> str:
    value = clamp_score(value)
    display_value = value
    color = score_color(10 - value) if invert else score_color(value)
    width = value * 10

    return f"""
    <div style="margin-bottom:16px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;gap:12px;">
            <span style="font-weight:600;color:#f3f4f6;">{label}</span>
            <span style="font-size:14px;color:#c7cad1;white-space:nowrap;">{display_value}/10</span>
        </div>
        <div style="
            width:100%;
            height:12px;
            border-radius:999px;
            background:#1a1d24;
            overflow:hidden;
            border:1px solid rgba(255,255,255,0.06);
        ">
            <div style="
                width:{width}%;
                height:100%;
                border-radius:999px;
                background:linear-gradient(90deg, {color}, {color});
                box-shadow:0 0 14px {color}55;
            "></div>
        </div>
    </div>
    """


def flag_list(flags: list[str]) -> str:
    if not flags:
        flags = ["Keine klaren Red Flags erkannt."]
    items = "".join(
        f"""
        <li style="
            margin-bottom:10px;
            line-height:1.55;
            color:#eceef3;
        ">
            {flag}
        </li>
        """
        for flag in flags
    )
    return f"<ul style='padding-left:20px; margin:0;'>{items}</ul>"


def build_fazit(data: dict) -> str:
    tendenz = data.get("tendenz", "Unklar")
    score = clamp_score(data.get("red_flag_score", 0))
    verbindlichkeit = clamp_score(data.get("verbindlichkeit", 0))
    konsistenz = clamp_score(data.get("konsistenz", 0))
    klarheit = clamp_score(data.get("emotionale_klarheit", 0))

    if score >= 7:
        level = "deutlich auffällig"
    elif score >= 4:
        level = "gemischt bis kritisch"
    else:
        level = "eher unauffällig"

    return (
        f"Gesamt wirkt die Situation aktuell <strong>{level}</strong>. "
        f"Die Tendenz geht in Richtung <strong>{tendenz}</strong>. "
        f"Besonders wichtig sind hier Verbindlichkeit ({verbindlichkeit}/10), "
        f"Konsistenz ({konsistenz}/10) und emotionale Klarheit ({klarheit}/10). "
        f"Ein einzelner kurzer Ausschnitt reicht selten für ein endgültiges Urteil, "
        f"aber er kann Hinweise geben, ob sich ein Muster von Nähe, Distanz oder "
        f"Unverbindlichkeit abzeichnet. Entscheidend ist, ob Worte und Verhalten "
        f"über mehrere Situationen hinweg zusammenpassen."
    )


def render(data: dict) -> str:
    red_flag_score = clamp_score(data.get("red_flag_score", 0))
    verbindlichkeit = clamp_score(data.get("verbindlichkeit", 0))
    konsistenz = clamp_score(data.get("konsistenz", 0))
    emotionale_klarheit = clamp_score(data.get("emotionale_klarheit", 0))
    tendenz = data.get("tendenz", "Unklar")
    kurzanalyse = data.get("kurzanalyse", "")
    hinweis = data.get("hinweis", "")
    fazit = data.get("fazit") or build_fazit(data)

    return f"""
    <div id="report" style="
        max-width:960px;
        margin:12px auto 0 auto;
        background:linear-gradient(180deg, rgba(17,19,24,0.98), rgba(12,13,18,0.98));
        border:1px solid rgba(255,255,255,0.06);
        border-radius:22px;
        padding:26px;
        box-shadow:0 10px 30px rgba(0,0,0,0.25);
        color:#f5f7fb;
    ">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:20px;flex-wrap:wrap;">
            <div>
                <div style="font-size:28px;font-weight:800;letter-spacing:-0.02em;margin-bottom:8px;">
                    Analyse
                </div>
                {tendency_badge(tendenz, red_flag_score)}
            </div>

            <div style="
                min-width:180px;
                padding:16px 18px;
                border-radius:18px;
                background:rgba(255,255,255,0.03);
                border:1px solid rgba(255,255,255,0.06);
                text-align:left;
            ">
                <div style="font-size:13px;color:#b3b8c4;margin-bottom:6px;">Red Flag Score</div>
                <div style="font-size:34px;font-weight:900;line-height:1;color:{score_color(red_flag_score)};">
                    {red_flag_score}/10
                </div>
            </div>
        </div>

        <div style="
            margin-top:18px;
            display:grid;
            grid-template-columns:1fr;
            gap:10px;
        ">
            {meter("Verbindlichkeit", verbindlichkeit, invert=True)}
            {meter("Konsistenz", konsistenz, invert=True)}
            {meter("Emotionale Klarheit", emotionale_klarheit, invert=True)}
        </div>

        <div style="
            margin-top:22px;
            display:grid;
            grid-template-columns:1fr;
            gap:18px;
        ">
            <div class="report-card" style="
                padding:18px;
                border-radius:18px;
                background:rgba(255,255,255,0.025);
                border:1px solid rgba(255,255,255,0.05);
            ">
                <div style="font-size:17px;font-weight:800;margin-bottom:12px;">Red Flags</div>
                {flag_list(data.get("red_flags", []))}
            </div>

            <div class="report-card" style="
                padding:18px;
                border-radius:18px;
                background:rgba(255,255,255,0.025);
                border:1px solid rgba(255,255,255,0.05);
            ">
                <div style="font-size:17px;font-weight:800;margin-bottom:10px;">Kurzanalyse</div>
                <div style="line-height:1.65;color:#eceef3;">{kurzanalyse}</div>
            </div>

            <div class="report-card" style="
                padding:18px;
                border-radius:18px;
                background:rgba(255,92,92,0.06);
                border:1px solid rgba(255,92,92,0.18);
            ">
                <div style="font-size:17px;font-weight:800;margin-bottom:10px;">Hinweis</div>
                <div style="line-height:1.65;color:#f3f4f6;">{hinweis}</div>
            </div>

            <div class="report-card" style="
                padding:20px;
                border-radius:18px;
                background:linear-gradient(180deg, rgba(255,255,255,0.035), rgba(255,255,255,0.02));
                border:1px solid rgba(255,255,255,0.07);
            ">
                <div style="font-size:18px;font-weight:900;margin-bottom:10px;">Fazit</div>
                <div style="line-height:1.72;color:#eef1f6;font-size:15.5px;">
                    {fazit}
                </div>
            </div>
        </div>
    </div>
    """


# ---------- MAIN ACTION ----------

def run_red_flags(file, text):
    content = safe_limit(get_text(file, text))

    if not content.strip():
        return """
        <div style="
            max-width:960px;
            margin:12px auto 0 auto;
            padding:22px;
            border-radius:18px;
            background:#12141a;
            border:1px solid rgba(255,255,255,0.06);
            color:#f5f7fb;
        ">
            Bitte füge Text ein oder lade einen Chat/Screenshot hoch.
        </div>
        """

    prompt = load_prompt("red_flags.txt")
    raw = call_hf_chat(prompt, content)
    data = parse_json(raw)
    return render(data)


# ---------- CUSTOM CSS ----------

CUSTOM_CSS = """
:root{
  --bg:#06070b;
  --panel:#111319;
  --panel-2:#151922;
  --text:#f5f7fb;
  --muted:#adb3bf;
  --line:rgba(255,255,255,0.08);
  --accent:#ff5c5c;
  --accent-2:#ff7a7a;
  --pdf-1:#3a8dff;
  --pdf-2:#66b3ff;
}

body, .gradio-container{
  background: radial-gradient(circle at top, #0a0d14 0%, #05060a 55%, #030407 100%) !important;
  color: var(--text) !important;
  font-family: Inter, ui-sans-serif, system-ui, sans-serif !important;
}

.gradio-container{
  max-width: 1080px !important;
  margin: 0 auto !important;
  padding-top: 14px !important;
}

h1, h2, h3, h4, p, div, span, label{
  color: var(--text);
}

.compact-upload{
  min-height: 130px !important;
  max-height: 130px !important;
  border-radius: 18px !important;
  overflow: hidden !important;
}

.compact-upload .wrap{
  min-height: 130px !important;
}

.compact-upload [data-testid="file-upload-dropzone"]{
  min-height: 130px !important;
  border: 1px dashed rgba(255,255,255,0.14) !important;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.015)) !important;
  border-radius: 18px !important;
}

.compact-upload .or{
  opacity: 0.7;
}

textarea, .gr-textbox textarea{
  border-radius: 18px !important;
  background: rgba(255,255,255,0.02) !important;
  border: 1px solid rgba(255,255,255,0.08) !important;
  color: #f5f7fb !important;
  font-size: 15px !important;
  line-height: 1.6 !important;
}

button.primary, button.lg, .gr-button{
  border-radius: 16px !important;
  font-weight: 700 !important;
}

#analyze-btn{
  background: linear-gradient(90deg, #ff5c5c, #ff7878) !important;
  border: none !important;
  color: white !important;
  box-shadow: 0 8px 24px rgba(255, 92, 92, 0.25) !important;
}

#analyze-btn:hover{
  filter: brightness(1.05);
}

.pixel-flags{
  display:flex;
  gap:14px;
  align-items:flex-end;
  margin:10px 0 14px 0;
}

.pixel-flag{
  position:relative;
  width:22px;
  height:34px;
  animation: sway 2.4s ease-in-out infinite;
  transform-origin: bottom center;
}

.pixel-flag:nth-child(2){ animation-delay:.25s; }
.pixel-flag:nth-child(3){ animation-delay:.5s; }
.pixel-flag:nth-child(4){ animation-delay:.75s; }

.pixel-flag::before{
  content:"";
  position:absolute;
  left:9px;
  bottom:0;
  width:3px;
  height:34px;
  background:#d9dde6;
  border-radius:2px;
}

.pixel-flag::after{
  content:"";
  position:absolute;
  left:12px;
  top:3px;
  width:12px;
  height:10px;
  background:#ff5c5c;
  box-shadow:
    4px 0 0 #ff5c5c,
    8px 0 0 #ff5c5c,
    0 4px 0 #ff5c5c,
    4px 4px 0 #ff5c5c,
    8px 4px 0 #ff5c5c;
  clip-path: polygon(0 0, 100% 0, 74% 50%, 100% 100%, 0 100%);
}

@keyframes sway{
  0%{ transform: rotate(-4deg) translateY(0px); }
  50%{ transform: rotate(4deg) translateY(-1px); }
  100%{ transform: rotate(-4deg) translateY(0px); }
}

.claim-highlight{
  color:#ff4d4d;
  font-weight:600;
}

.hero-card{
  padding: 18px 0 8px 0;
}

.hero-title{
  font-size: 36px;
  font-weight: 900;
  letter-spacing: -0.03em;
  margin-bottom: 8px;
}

.hero-sub{
  color: #c6cad3;
  font-size: 16px;
  line-height: 1.65;
  max-width: 860px;
}

.section-title{
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: .14em;
  color: #9298a4;
  margin-bottom: 10px;
}

.pdf-wrap{
  display:flex;
  justify-content:center;
  margin:12px 0 8px 0;
}

.pdf-btn{
  width:100%;
  max-width:420px;
  padding:14px 18px;
  border-radius:16px;
  border:none;
  font-weight:800;
  font-size:15px;
  cursor:pointer;
  color:white;
  background:linear-gradient(90deg,var(--pdf-1),var(--pdf-2));
  box-shadow:0 10px 30px rgba(79,172,254,0.24);
  transition:all .2s ease;
}

.pdf-btn:hover{
  transform:translateY(-1px);
  filter:brightness(1.05);
}

.pdf-btn:active{
  transform:translateY(0);
}

.footer-note{
  position: relative;
  z-index: 10;
  text-align:center;
  color:#c6cad3;
  font-size:14px;
  line-height:1.7;
  max-width:760px;
  margin:28px auto 18px auto;
  opacity:0.9;
}

.footer-line{
  height:1px;
  background:rgba(255,255,255,0.08);
  margin:0 auto 18px auto;
  max-width:520px;
}

.privacy-wrap{
  max-width: 960px;
  margin: 22px auto 28px auto;
}

.privacy-details{
  border-radius: 22px;
  overflow: hidden;
}

.privacy-summary{
  list-style: none;
  cursor: pointer;
  user-select: none;
  display:flex;
  align-items:center;
  justify-content:center;
  gap:10px;
  text-align:center;
  padding:18px 22px;
  border-radius:20px;
  border:1px solid rgba(255,255,255,0.08);
  background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.015));
  color:#f5f7fb;
  font-size:16px;
  font-weight:800;
  transition:all .2s ease;
}

.privacy-summary:hover{
  border-color: rgba(255,255,255,0.14);
  background:linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.02));
}

.privacy-summary::-webkit-details-marker{
  display:none;
}

.privacy-box{
  margin-top:14px;
  padding:24px;
  border-radius:20px;
  border:1px solid rgba(255,255,255,0.07);
  background:linear-gradient(180deg, rgba(255,255,255,0.025), rgba(255,255,255,0.015));
  color:#f5f7fb;
}

.privacy-box h3{
  margin:0 0 10px 0;
  color:#d8b27a;
  font-size:18px;
  font-weight:800;
}

.privacy-box p{
  margin:0 0 26px 0;
  color:#eef1f6;
  line-height:1.75;
  font-size:15px;
}

.privacy-note{
  margin-bottom:0 !important;
  color:#8f96a3 !important;
}

@media (max-width: 600px){
  .privacy-summary{
    font-size:15px;
    padding:16px 18px;
    border-radius:18px;
  }

  .privacy-box{
    padding:18px;
    border-radius:18px;
  }

  .privacy-box h3{
    font-size:17px;
  }

  .privacy-box p{
    font-size:14px;
    line-height:1.7;
  }
}

@media print{
  @page{
    size:A4;
    margin:0;
  }

  html, body{
    background:#0b0e14 !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  body *{
    visibility:hidden !important;
  }

  #report, #report *{
    visibility:visible !important;
  }

  #report{
    position:absolute !important;
    left:0 !important;
    top:0 !important;
    width:100% !important;
    max-width:100% !important;
    margin:0 !important;
    padding:20px !important;
    border-radius:0 !important;
    box-shadow:none !important;
    background:linear-gradient(180deg, #111319, #0d1016) !important;
    border:1px solid rgba(255,255,255,0.08) !important;
  }

  #report, #report *, .report-card{
    break-inside: avoid !important;
    page-break-inside: avoid !important;
  }

  .compact-upload,
  .section-title,
  .pixel-flags,
  .hero-card,
  .pdf-wrap,
  .gr-button,
  textarea,
  input,
  .footer-note,
  .privacy-wrap,
  footer{
    display:none !important;
  }
}
"""


PDF_BUTTON_HTML = """
<div class="pdf-wrap">
  <button
    class="pdf-btn"
    onclick='
      const report = document.getElementById("report");
      if (!report) {
        alert("Bitte zuerst eine Analyse erstellen.");
        return;
      }

      const oldFrame = document.getElementById("print-frame");
      if (oldFrame) oldFrame.remove();

      const iframe = document.createElement("iframe");
      iframe.id = "print-frame";
      iframe.style.position = "fixed";
      iframe.style.right = "0";
      iframe.style.bottom = "0";
      iframe.style.width = "0";
      iframe.style.height = "0";
      iframe.style.border = "0";
      document.body.appendChild(iframe);

      const doc = iframe.contentWindow.document;
      const reportHtml = report.outerHTML;

      doc.open();
      doc.write(`
        <html>
          <head>
            <title>Reality Check Report</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <style>
              html, body {
                margin: 0;
                padding: 0;
                background: #0b0e14;
                color: #f5f7fb;
                font-family: Inter, Arial, sans-serif;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
              }

              body {
                margin: 0 !important;
                padding: 0 !important;
              }

              #report {
                max-width: 960px;
                margin: 0 auto !important;
                padding: 24px !important;
                background: #0b0e14 !important;
                color: #f5f7fb !important;
              }

              @page {
                size: A4;
                margin: 0;
              }

              #report,
              #report * {
                break-inside: avoid !important;
                page-break-inside: avoid !important;
                box-sizing: border-box;
              }

              #report > div {
                break-inside: avoid !important;
                page-break-inside: avoid !important;
              }

              #report h2,
              #report h3,
              #report h4,
              #report p,
              #report ul,
              #report li {
                break-inside: avoid !important;
                page-break-inside: avoid !important;
              }

              @media print {
                html, body {
                  background: #0b0e14 !important;
                  -webkit-print-color-adjust: exact !important;
                  print-color-adjust: exact !important;
                }

                body {
                  padding: 0 !important;
                }

                #report {
                  max-width: 100% !important;
                  margin: 0 !important;
                  padding: 20px !important;
                }
              }
            </style>
          </head>
          <body>
            ${reportHtml}
          </body>
        </html>
      `);
      doc.close();

      iframe.onload = function() {
        setTimeout(() => {
          iframe.contentWindow.focus();
          iframe.contentWindow.print();
        }, 300);
      };

      setTimeout(() => {
        try {
          iframe.contentWindow.focus();
          iframe.contentWindow.print();
        } catch (e) {}
      }, 800);
    '
  >
    📄 PDF herunterladen
  </button>
</div>
"""


PRIVACY_HTML = """
<div class="privacy-wrap">
  <div class="privacy-box">
    <button class="privacy-toggle" onclick="togglePrivacyNotice()">🔒 Datenschutzhinweis</button>
    <div id="privacy-content" class="privacy-content">
      <h4>Wie werden deine Daten verarbeitet?</h4>
      <p>
        Dein eingegebener Chat-Text oder Screenshot wird auf diesem Interface nicht dauerhaft gespeichert.
        Es gibt in dieser Version keine eigene Datenbank, kein Benutzerkonto und kein bewusst eingebautes Tracking deiner Eingaben.
      </p>

      <h4>Was passiert bei der Analyse?</h4>
      <p>
        Zur Erzeugung der Einschätzung wird dein Text an die <strong>Hugging Face Inference API</strong> gesendet,
        damit ein Sprachmodell die Situation analysieren kann. Das bedeutet, dass deine Eingabe den lokalen Server verlässt
        und von einem externen Dienst verarbeitet wird. Je nach Infrastruktur können dort Anfragen kurzzeitig protokolliert werden,
        etwa zur Stabilität, Fehlerbehebung oder Missbrauchserkennung.
      </p>

      <h4>Empfehlung</h4>
      <p>
        Teile keine sensiblen personenbezogenen Informationen wie vollständige Namen, Adressen, Telefonnummern,
        E-Mail-Adressen, Orte, Kennzeichen oder andere eindeutig identifizierende Details. Beschreibe Situationen lieber so,
        dass sie inhaltlich verständlich bleiben, ohne dich oder andere direkt identifizierbar zu machen.
      </p>

      <p class="privacy-muted">
        Reality Check befindet sich in aktiver Entwicklung. Perspektivisch kann eine lokalere oder datensparsamere Verarbeitung
        ergänzt werden, damit noch weniger Inhalte externe Dienste verlassen.
      </p>
    </div>
  </div>
</div>

<script>
function togglePrivacyNotice() {
  const box = document.getElementById("privacy-content");
  if (!box) return;
  box.classList.toggle("open");
}
</script>
"""


# ---------- UI ----------

with gr.Blocks(css=CUSTOM_CSS, title="Reality Check") as app:
    gr.HTML("""
    <div class="hero-card">
        <div class="pixel-flags">
            <div class="pixel-flag"></div>
            <div class="pixel-flag"></div>
            <div class="pixel-flag"></div>
            <div class="pixel-flag"></div>
        </div>
        <div class="hero-title">❤️ Reality Check</div>
        <div class="hero-sub">
            <span class="claim-highlight">Liebe macht blind. KI nicht.</span>
            Lade Chatverläufe oder Screenshots hoch,
            prüfe Red Flags klarer und erhalte eine nüchterne Einordnung.
        </div>
    </div>
    """)

    gr.HTML('<div class="section-title">Chat oder Screenshot</div>')
    file = gr.File(
        label="TXT oder Screenshot hochladen",
        elem_classes=["compact-upload"],
        file_types=[".txt", ".png", ".jpg", ".jpeg", ".webp"]
    )

    gr.HTML('<div class="section-title" style="margin-top:14px;">Text direkt einfügen</div>')
    text = gr.Textbox(
        lines=9,
        placeholder="Füge hier einen Chatverlauf oder eine kurze Situationsbeschreibung ein ..."
    )

    with gr.Column():
        btn = gr.Button("Analysieren", elem_id="analyze-btn")
        gr.HTML(PDF_BUTTON_HTML)
        out = gr.HTML()
        btn.click(run_red_flags, inputs=[file, text], outputs=out)

        gr.HTML("""
        <div class="footer-note">
            <div class="footer-line"></div>
            ⚠️ Diese Analyse ersetzt keine Therapie, keine professionelle Beratung und keine echte Begegnung.<br>
            Beobachte nicht nur Worte. Beobachte Verhalten.
        </div>
        """)

        gr.HTML("""
<div class="privacy-wrap">
  <details class="privacy-details">
    <summary class="privacy-summary">
      🔒 Datenschutzhinweis
    </summary>

    <div class="privacy-box">
      <h3>Wie werden deine Daten verarbeitet?</h3>
      <p>
        Dein eingegebener Text wird von dieser Oberfläche selbst nicht dauerhaft gespeichert.
        Es gibt in dieser Version keine Nutzerkonten und keine lokale Datenbank für deine Analyse.
      </p>

      <h3>Was passiert bei der Analyse?</h3>
      <p>
        Zur Auswertung wird dein Text an die <strong>Hugging Face Inference API</strong> gesendet,
        damit ein Sprachmodell die Einschätzung erzeugen kann. Das bedeutet, dass dein Text
        den Server verlässt und von einem externen Dienst verarbeitet wird.
      </p>

      <h3>Empfehlung</h3>
      <p>
        Teile keine sensiblen persönlichen Informationen, die dich oder andere direkt
        identifizierbar machen, z. B. vollständige Namen, Adressen, Telefonnummern,
        E-Mail-Adressen oder sehr konkrete Orte.
      </p>

      <p class="privacy-note">
        Langfristig ist eine stärker lokale und datensparsame Verarbeitung denkbar.
        Für diese Version gilt jedoch: Externe KI-Verarbeitung ist Teil der Analyse.
      </p>
    </div>
  </details>
</div>
""")

if __name__ == "__main__":
    app.launch()
