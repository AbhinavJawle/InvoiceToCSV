# ⚡ InvoiceToCSV: KI-gestützte Dokumentenverarbeitung

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![AI](https://img.shields.io/badge/AI-Google_Gemini-4285F4?style=flat&logo=google&logoColor=white)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_APP_URL_HERE)

## 💼 Das Geschäftsproblem

Die manuelle Datenerfassung aus Rechnungen ist einer der größten Flaschenhälse in Buchhaltung und Supply Chain Management. Sie ist langsam, fehleranfällig und bindet wertvolle Arbeitszeit. Unternehmen verbringen tausende Stunden damit, Daten von PDFs in Excel-Tabellen zu übertragen.

## 🚀 Die Lösung

**InvoiceToCSV** ist eine automatisierte Pipeline, die unstrukturierte Rechnungsbilder (JPG/PNG) in Sekunden in strukturierte CSV-Daten umwandelt.
Das System nutzt **Multimodale KI (Google Gemini Flash)**, um Dokumente wie ein Mensch zu "lesen" und Positionen, Preise und Summen mit hoher Präzision zu extrahieren – unabhängig vom Layout der Rechnung.

## 🛠️ Tech Stack

- **Core Logic:** Python
- **UI/Frontend:** Streamlit
- **AI Engine:** Google Gemini Flash (Computer Vision / LLM)
- **Data Processing:** Pandas

## ✨ Hauptfunktionen

- **Universelle Extraktion:** Funktioniert mit jedem Rechnungslayout (keine Vorlagen/Templates nötig).
- **Multi-Währungs-Support:** Erkennt automatisch Währungen (€, $, ₹, £) und formatiert die Daten korrekt.
- **Privacy First:** API-Keys werden sicher über Umgebungsvariablen (`.env`) verwaltet und nicht im Code gespeichert.
- **Export Ready:** One-Click-Download als CSV für die direkte Integration in Excel oder ERP-Systeme.

## ⚙️ Installation & Start

1.  **Repository klonen**

    ```bash
    git clone [https://github.com/DEIN_USERNAME/InvoiceToCSV.git](https://github.com/DEIN_USERNAME/InvoiceToCSV.git)
    cd InvoiceToCSV
    ```

2.  **Abhängigkeiten installieren**

    ```bash
    pip install -r requirements.txt
    ```

3.  **API-Key konfigurieren**
    Erstelle eine Datei namens `.env` im Hauptverzeichnis und füge deinen Key ein:

    ```text
    GEMINI_API_KEY=dein_api_key_hier
    ```

4.  **App starten**
    ```bash
    streamlit run app.py
    ```

## 📈 Ausblick (Roadmap)

- [ ] Konnektor für SAP / Supabase Datenbanken.
- [ ] Batch-Processing (Verarbeitung von 50+ Rechnungen gleichzeitig).
- [ ] E-Mail-Integration zur automatischen Weiterleitung der CSV-Dateien.
