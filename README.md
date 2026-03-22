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

## ✦ Anwendungsfälle

Das Tool eignet sich zum Beispiel für:

- Chatverläufe mit gemischten Signalen
- emotionale Unsicherheit nach Kennenlernphasen
- nüchterne Selbstreflexion nach konflikthaften Gesprächen
- erste Einordnung von Kommunikationsmustern
- strukturierte Betrachtung statt impulsiver Interpretation



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

### 1. Repository klonen

```bash
git clone https://github.com/DEIN-USERNAME/reality-check.git
cd reality-check
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

Danach läuft die App im Browser unter:

```text
http://127.0.0.1:7860
```
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
