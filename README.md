---
title: Reality Check
emoji: ❤️
colorFrom: red
colorTo: blue
sdk: gradio
app_file: app.py
pinned: false
sdk_version: 6.9.0
---

---
title: Reality Check
emoji: ❤️
colorFrom: red
colorTo: blue
sdk: gradio
app_file: app.py
pinned: false
sdk_version: 6.9.0
---

<div align="center">

# ❤️ Reality Check

**Erzähl mir, was passiert ist — und ich helfe dir, es klarer zu sehen.**

[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/OrangeDev/Reality-Check)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-6.9-FF7C00?logo=gradio&logoColor=white)](https://gradio.app)
[![OCR](https://img.shields.io/badge/OCR-Tesseract-6A4C93)](https://github.com/tesseract-ocr/tesseract)

<br>

*Ein KI-gestützter Analyse-Assistent für Chatverläufe, Beziehungssituationen und emotionale Dynamiken — entwickelt, um Muster sichtbar zu machen, statt Wunschdenken zu verstärken.*

<br>

<img src="https://img.shields.io/badge/-%E2%9C%A6%20CLARITY%20%E2%80%A2%20PATTERNS%20%E2%80%A2%20TRUTH%20%E2%9C%A6-1A1714?style=for-the-badge&labelColor=1A1714" alt="aesthetic">

</div>

---

## ✦ Was ist Reality Check?

Reality Check ist ein minimalistisches KI-Tool, das dabei hilft, **Beziehungssituationen, Chatverläufe und emotionale Unklarheit rationaler einzuordnen**. Statt nur auf Bauchgefühl zu reagieren, analysiert die App sprachliche Hinweise, Verhaltensmuster und Konsistenzsignale, um eine zweite, nüchterne Perspektive zu geben.

Der Fokus liegt nicht auf endgültigen Urteilen, sondern auf **Orientierung, Struktur und emotionaler Klarheit**.

> *Gefühle sind echt. Aber ihre Interpretation ist nicht immer eindeutig.*

Reality Check will nicht entscheiden, was du fühlen sollst — sondern dir helfen, klarer zu erkennen, **was tatsächlich im Verhalten der anderen Person sichtbar wird**.

---

## ✦ Features

**Reality Check Analyse**<br>
Strukturierte Auswertung statt reiner Intuition oder Wunschinterpretation
</br>
<br>
**Red Flag Detection**<br>
Erkennung typischer Warnmuster wie Distanz, Inkonsistenz, Unverbindlichkeit oder emotionale Unklarheit
</br>
<br>
**Scoring-System**<br>
Bewertung zentraler Faktoren wie Verbindlichkeit, Konsistenz und emotionale Klarheit
</br>
<br>
**Strukturierte Zusammenfassung**<br>
Klare Einordnung der Dynamik mit kompaktem Fazit und erkennbaren Mustern
</br>
<br>
**PDF Export**<br>
Export direkt aus dem Interface im UI-nahen Stil zur Reflexion oder zum Teilen
</br>
<br>
**OCR Support**<br>
Screenshots von Chats können per Tesseract in Text umgewandelt und analysiert werden
</br>
<br>
**Mobile-Ready**<br>
Responsives Interface für Smartphone, Tablet und Desktop
</br>

---

## ✦ Beispiel Output

```text
Red Flag Score: 7/10

Verbindlichkeit: 3/10
Konsistenz: 2/10
Emotionale Klarheit: 4/10

→ Muster: Distanz, Inkonsistenz, Unsicherheit
→ Tendenz: emotional unklar, kommunikativ nicht stabil
```

---

## ✦ Architektur

```text
Eingabe: Chatverlauf / Situation / Screenshot
    │
    ├──→ Optional: OCR (Tesseract)
    │         │
    │         └──→ Text aus Screenshot extrahieren
    │
    ├──→ Prompt Builder
    │         │
    │         └──→ Strukturierte Analyseanweisung
    │
    └──→ LLM via Hugging Face Inference API
              │
              └──→ Scores + Mustererkennung + Fazit
```

---

## ✦ Tech Stack

| Komponente | Technologie |
|---|---|
| **Frontend** | Gradio 6.9 mit Custom UI |
| **Backend** | Python |
| **LLM API** | Hugging Face Inference API |
| **Modelle** | Konfigurierbare Instruct-Modelle via HF Router |
| **OCR** | Tesseract OCR |
| **Export** | PDF im UI-orientierten Layout |
| **Hosting** | Hugging Face Spaces |

---

## ✦ Projektstruktur

```text
Reality-Check/
├── app.py                     # Hauptanwendung
├── requirements.txt           # Python-Abhängigkeiten
├── .env.example               # Beispiel für Umgebungsvariablen
├── README.md                  # Projektdokumentation
├── app/
│   └── prompts/
│       └── analysis_prompt.txt    # Prompt-Template für die Analyse
├── assets/
│   ├── css/                       # UI-Styling
│   └── icons/                     # Icons / UI-Assets
├── exports/
│   └── pdf/                       # Generierte PDF-Exports (optional/lokal)
└── temp/
    └── uploads/                   # Temporäre OCR-/Upload-Dateien
```

> Passe die Struktur an dein tatsächliches Repository an, falls einzelne Ordner oder Dateinamen bei dir anders heißen.

---

## ✦ Lokale Installation

```bash
# Repository klonen
git clone https://github.com/DEIN-USERNAME/Reality-Check.git
cd Reality-Check

# Virtuelle Umgebung erstellen
python3 -m venv venv
source venv/bin/activate

# Dependencies installieren
pip install -r requirements.txt
```

---

## ✦ Umgebungsvariablen

```bash
cp .env.example .env
```

Dann z. B. eintragen:

```env
HF_API_KEY=dein_token
HF_MODEL=meta-llama/Llama-3.1-8B-Instruct:cerebras
```

---

## ✦ OCR Installation

```bash
sudo apt install tesseract-ocr -y
sudo apt install tesseract-ocr-deu -y
```

Wenn du Screenshots analysieren möchtest, ist Tesseract erforderlich.

---

## ✦ Starten

```bash
python app.py
```

Die App läuft dann auf `http://127.0.0.1:7860`.

---

## ✦ Datenschutz

**Keine dauerhafte Speicherung**  
Eingaben werden nicht in einer eigenen Datenbank gespeichert, nicht für Nutzerprofile verwendet und nicht aktiv getrackt.

**Externe Verarbeitung**  
Für die Analyse wird Text an die Hugging Face Inference API gesendet. Dadurch verlässt deine Eingabe lokal dein Gerät und wird extern verarbeitet.

**Wichtiger Hinweis**  
Je nach Infrastruktur des externen Anbieters können Anfragen technisch bedingt kurzfristig protokolliert oder für Fehleranalyse verarbeitet werden.

**Empfehlung**  
Teile keine unnötig sensiblen Daten wie vollständige Namen, Adressen, Telefonnummern oder eindeutig identifizierende Informationen.

**Zukunftsvision**  
Langfristig ist eine vollständig lokale Verarbeitung denkbar, damit keine Inhalte das Gerät verlassen müssen.

---

## ✦ Grundsätze

Reality Check folgt klaren inhaltlichen Leitlinien:

- Keine Diagnosen und keine therapeutischen Aussagen
- Keine absolute Wahrheit, sondern rationale Perspektiven
- Keine emotionale Manipulation durch übertriebene Gewissheit
- Fokus auf beobachtbares Verhalten, nicht auf Fantasie oder Projektion
- Sensible Situationen sollten immer auch im echten Leben reflektiert oder besprochen werden

---

## ✦ Hinweis

Dieses Tool ersetzt nicht:

- keine Therapie
- keine psychologische Beratung
- keine rechtliche Einschätzung
- keine ehrliche Kommunikation zwischen Menschen

> Reality Check ist ein Spiegel — kein Urteil.

---

## ✦ Roadmap

- [ ] Vollständig lokale Inference
- [ ] Bessere Mustererkennung über längere Verläufe
- [ ] Shareable Reports
- [ ] Verlaufssitzungen / Session-Historie
- [ ] Erweiterte Timeline- und Dynamik-Analyse

---

## ✦ Live Demo

**→ [Reality Check auf Hugging Face ausprobieren](https://huggingface.co/spaces/OrangeDev/Reality-Check)**

---

<div align="center">

*❤️ Built with focus on clarity, emotion and truth*

<sub>Made for reflection, not illusion.</sub>

</div>

# ❤️ Reality Check

<div align="center">

## **Liebe macht blind. KI nicht.**

Ein minimalistisches, KI-gestütztes Tool zur **nüchternen Analyse von Chatverläufen, Beziehungen und emotionalen Dynamiken**.

<br>

**Live Demo:**  
https://huggingface.co/spaces/OrangeDev/Reality-Check

</div>

---

## Überblick

**Reality Check** hilft dabei, emotionale Situationen strukturierter zu betrachten.
Statt sich allein auf Hoffnung, Projektion oder Bauchgefühl zu verlassen, erzeugt das Tool eine zweite Perspektive: klar, sprachlich geordnet und auf wiederkehrende Muster fokussiert.

Es geht nicht darum, Gefühle zu entwerten. Es geht darum, sie besser einzuordnen.

---

## Warum dieses Projekt?

Zwischenmenschliche Kommunikation ist oft widersprüchlich.
Menschen lesen in Nachrichten mehr hinein, als tatsächlich gesagt wurde — oder übersehen genau die Muster, die eigentlich sichtbar sind.

**Reality Check** wurde dafür gebaut, um:

- emotionale Dynamiken nüchterner zu betrachten
- Inkonsistenzen schneller zu erkennen
- Unsicherheit sprachlich greifbar zu machen
- einen rationaleren Blick auf Chatverläufe und Beziehungsmuster zu ermöglichen

> Kein Orakel. Kein Urteil.  
> Sondern ein strukturierter Spiegel.

---

## Features

| Bereich | Beschreibung |
|---|---|
| 🔍 Reality Check | Analysiert Texte nicht romantisch, sondern strukturiert |
| 🚩 Red-Flag-Erkennung | Erkennt mögliche Muster wie Distanz, Widersprüche oder Unklarheit |
| 📊 Scoring-System | Bewertet Verbindlichkeit, Konsistenz und emotionale Klarheit |
| 🧠 KI-Auswertung | Erstellt ein Fazit mit nachvollziehbarer sprachlicher Einordnung |
| 📄 PDF-Export | Export direkt aus dem Interface im UI-nahen Layout |
| 📸 OCR-Support | Extrahiert Text aus Screenshots via Tesseract |
| 📱 Responsive UI | Nutzbar auf Desktop und Mobilgeräten |

---

## Beispielausgabe

```text
Red Flag Score: 7/10

Verbindlichkeit: 3/10
Konsistenz: 2/10
Emotionale Klarheit: 4/10

Muster:
- Distanz
- Inkonsistenz
- Unsicherheit

Fazit:
Die Kommunikation wirkt nicht stabil genug, um klare Verlässlichkeit zu signalisieren.
```

---

## Anwendungsfälle

Das Tool eignet sich zum Beispiel für:

- Chatverläufe mit gemischten Signalen
- emotionale Unsicherheit nach Kennenlernphasen
- nüchterne Selbstreflexion nach konflikthaften Gesprächen
- erste Einordnung von Kommunikationsmustern
- strukturierte Betrachtung statt impulsiver Interpretation

---

## Tech Stack

```text
Python
Gradio
Hugging Face Inference API
Tesseract OCR
Custom HTML/CSS
PDF Export
```

---

## Projektverzeichnis

Eine mögliche Projektstruktur sieht so aus:

```text
reality-check/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── data/
│   └── examples/
├── exports/
│   └── pdf/
├── app/
│   ├── prompts/
│   │   └── interpret_prompt.txt
│   ├── utils/
│   │   ├── analysis.py
│   │   ├── ocr.py
│   │   ├── pdf_export.py
│   │   └── scoring.py
│   ├── components/
│   │   └── ui_blocks.py
│   └── assets/
│       ├── styles.css
│       └── icons/
└── screenshots/
```

### Kurz erklärt

- **app.py** → Einstiegspunkt der Gradio-App
- **requirements.txt** → Python-Abhängigkeiten
- **.env.example** → Vorlage für Umgebungsvariablen
- **app/prompts/** → Prompt-Dateien für die KI-Auswertung
- **app/utils/** → Logik für Analyse, OCR, PDF und Scoring
- **app/components/** → wiederverwendbare UI-Bausteine
- **app/assets/** → Styles, Icons und statische Ressourcen
- **exports/** → erzeugte PDF-Dateien
- **screenshots/** → optionale Testbilder für OCR
- **data/** → Beispieldaten oder lokale Hilfsdaten

---

## Installation

### 1. Repository klonen

```bash
git clone https://github.com/DEIN-USERNAME/love-reality-check.git
cd love-reality-check
```

### 2. Virtuelle Umgebung erstellen

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 4. OCR installieren

Für Screenshot-Analyse mit Tesseract:

```bash
sudo apt update
sudo apt install tesseract-ocr -y
sudo apt install tesseract-ocr-deu -y
```

### 5. Umgebungsvariablen konfigurieren

```bash
cp .env.example .env
```

Dann in `.env` eintragen:

```env
HF_API_KEY=dein_token
HF_MODEL=meta-llama/Llama-3.1-8B-Instruct:cerebras
```

---

## Starten

```bash
python app.py
```

Danach im Browser öffnen:

```text
http://127.0.0.1:7860
```

---

## OCR-Unterstützung

Wenn du statt kopiertem Text Screenshots einfügst, kann das Tool den Inhalt per OCR extrahieren.

Das ist besonders nützlich für:

- Social-Media-Screenshots
- Messenger-Chats
- exportierte Konversationen als Bild
- Inhalte, die nicht direkt kopierbar sind

Je sauberer das Bild, desto besser die Erkennung.

---

## PDF-Export

Die Analyse kann direkt im Interface als PDF exportiert werden.

Vorteile:

- Layout bleibt möglichst nah am UI
- ideal für Dokumentation und Reflexion
- gut lesbar auf A4
- praktisch zum Speichern oder Teilen

---

## Datenschutz

### Was lokal passiert

Das Projekt speichert standardmäßig **keine eigene Datenbankhistorie**, sofern du keine zusätzliche Persistenz einbaust.

Geplant bzw. empfohlen ist ein möglichst datensparsamer Betrieb:

- keine lokale Nutzerverwaltung
- keine dauerhafte Chat-Historie
- kein eingebautes Tracking
- keine absichtliche Langzeitspeicherung von Inhalten

### Was extern passiert

Für die eigentliche Textanalyse wird die Eingabe an eine **Hugging Face Inference API** gesendet.
Dadurch gilt:

- die Eingabe verlässt dein lokales Gerät
- die Verarbeitung findet auf externer Infrastruktur statt
- temporäre technische Logs beim Anbieter können nicht vollständig ausgeschlossen werden

### Wichtiger Praxishinweis

Teile keine unnötig sensiblen Daten, zum Beispiel:

- vollständige Namen
- Adressen
- Telefonnummern
- konkrete Orte
- intime oder eindeutig identifizierende Informationen

Formuliere Inhalte lieber so, dass die Situation verständlich bleibt, ohne reale Identitäten offenzulegen.

### Perspektive für spätere Versionen

```text
Ziel: 100 % lokale Inference
→ keine externe API
→ deutlich höhere Privatsphäre
→ bessere Datensouveränität
```

---

## Grenzen des Tools

**Reality Check** ist ein Reflexionswerkzeug — keine therapeutische, juristische oder medizinische Instanz.

Es ersetzt nicht:

- Therapie
- professionelle Beratung
- Krisenhilfe
- echte Kommunikation zwischen Menschen

Die Auswertung ist eine KI-gestützte Einschätzung auf Basis sprachlicher Muster, nicht die endgültige Wahrheit über eine Beziehung oder Person.

---

## Roadmap

- [ ] Lokale Inference ohne API-Abhängigkeit
- [ ] Verlauf / Sessions
- [ ] Shareable Reports
- [ ] Zeitliche Emotionsanalyse
- [ ] Erweiterte Pattern Detection
- [ ] Mehrsprachige Analyse
- [ ] Feineres Scoring-Modell

---

## Vision

Ein Tool, das Menschen hilft,

- klarer zu sehen
- weniger zu projizieren
- emotionale Muster schneller zu erkennen
- fundierter zu reflektieren
- rationalere Entscheidungen zu treffen

---

## Für Entwickler

Wenn du das Projekt erweitern willst, sind diese Bereiche besonders interessant:

- lokales LLM statt externer API
- bessere Prompt-Strategien
- modulareres Scoring
- OCR-Qualität verbessern
- Exportformate erweitern
- UI/UX für längere Analysen optimieren

---

## Author

Built with focus on:

```text
Clarity
Emotion
Truth
```

---

## Support

Wenn dir das Projekt gefällt:

- gib dem Repo einen Stern
- teile es mit anderen
- gib Feedback oder Verbesserungsvorschläge

---

## Hinweis zur Verantwortung

Dieses Projekt ist für **Reflexion und Einordnung** gedacht — nicht für Überwachung, Manipulation oder Kontrolle anderer Menschen.

Die beste Nutzung entsteht dort, wo Klarheit, Fairness und Selbstreflexion im Vordergrund stehen.
