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
