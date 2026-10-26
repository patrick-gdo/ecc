# ECC · Analyse des bereitgestellten Bestands

**Status: gesamte bereitgestellte CSV rechnerisch ausgewertet; fachliche Datenbereinigung offen.** Analysedatum 26.10.2026. Ablage unter ECC gemäß Nutzerauftrag; keine Feststellung rechtlicher Bestandszugehörigkeit.

- 50.694 Vertragsdatensätze, 6.918 Kundennummern, 241 VMT-Kennungen.
- 29.320 aktiv gekennzeichnete Datensätze auf 6.147 Kundennummern, einschließlich X/K.
- 26.840 in A/F/H; 2.451 aktiv ohne Betreuung; 29 aktiv Korrespondenz.
- 805 aktive Datensätze mit Stornodatum bis zum Stichtag.

| Einstieg | Inhalt |
| --- | --- |
| [Analyse](ANALYSIS.md) | Kennzahlen, Struktur, belegte Schlüsse und Hypothesen |
| [Statuslegende](STATUS_LEGEND.md) | Nutzerbestätigte Codebedeutungen und Zählregeln |
| [Datenqualität](DATA_QUALITY.md) | Dubletten, Datumswidersprüche, fehlende Felder |
| [Methodik und Felder](METHOD.md) | Nenner, Filter, Rechenannahmen, Datenschutz |
| [Quellen](SOURCES.md) | Herkunft, Prüfumfang, Grenzen und Datei-Hash |
| [Fragenkatalog](QUESTION_GUIDE.md) | Was beantwortbar ist und was Zusatzdaten braucht |
| [Maschinenlesbare Aggregate](aggregates.json) | Alle berechneten Sichten und Prüfergebnisse |
| [Rechenprogramm](analyze.py) | Reproduzierbare Auswertung ohne Einzelkundenausgabe |
| [Statusdaten](status.csv) | Alle 15 Legendenwerte einschließlich H = 0 |
| [Sparten](sparten.csv) | Alle Sparten, Gesamt-/Aktiv-/A-/A-F-H-Sichten |
| [Gesellschaften](gesellschaften_top30.csv) | Top 30 je Sicht, Originalbezeichnungen |
| [Monatsdaten 2026](monate_2026.csv) | Datierte Ereignisse im Export; keine Flussrechnung |

Die Originaldatei und personenbezogene Einzelzeilen bleiben außerhalb von GitHub. Für spätere Detailfragen Original über die Quellenreferenz lesen, Hash vergleichen und Filter offenlegen. Die Aggregate sind keine zweite Kundenverwaltung und werden durch spätere Drive-Änderungen nicht automatisch aktualisiert.

Erste Folgefrage: [Top 5 Gesellschaften je gewünschtem Spartenbereich](TOP5_GESELLSCHAFTEN.md), Rangfolge nach aktiven A/F/H-Vertragsdatensätzen mit expliziter Kategorienzuordnung.

Neue Folgefrage: [Top-Gesellschaften ab 2024 und ab 2025](neuabschluesse/README.md), jeweils nach Vertragsbeginn bis 26.10.2026. Zwei neue Exporte, Hauptsicht einschließlich beitragsfreier und stornierter Zeilen; reine Aktivsicht separat in den Aggregaten. Quellen ECC-BST-003/004.
