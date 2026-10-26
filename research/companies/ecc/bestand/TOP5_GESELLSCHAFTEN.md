# ECC · Top 5 Gesellschaften nach Spartenbereich

Stand: 26.10.2026. Nutzerfrage: Welche Top-5-Gesellschaften wurden in Biometrie, Rente/bAV, Sach, KV Zusatz und KV Voll vermittelt?

**Auswertungsentscheidung:** Rangfolge nach Zahl der Vertragsdatensätze mit Art A/F/H. X (ohne Betreuung), K (Korrespondenz), beitragsfreie, beantragte, in Übertragung befindliche, abgelegte und stornierte Status sind ausgeschlossen. Kein zusätzlicher Stornodatumsfilter; deshalb keine Bestätigung laufender Zahlung. Die CSV belegt die ursprüngliche Vermittlungsherkunft nicht. Diese Tabelle beantwortet die Frage nach dem gespeicherten aktiven Bestand, nicht nach nachweislich selbst abgeschlossenem Neugeschäft. Quelle ECC-BST-001, Statuslegende ECC-BST-002.

Gesellschaftsbezeichnungen werden nicht konzernbereinigt (z. B. AXA und DBV getrennt). Die Bereichsbildung ist eine ausdrücklich dokumentierte analytische Zuordnung, kein zusätzliches Quellfeld.

| Bereich | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Biometrie | Canada Life Assurance Europe plc · 276 | Nürnberger Versicherungsgruppe · 199 | Swiss Life Lebensversicherung SE · 145 | Hannoversche Lebensversicherung AG · 137 | Baloise Holding AG (ehem. Basler) · 110 |
| Rente / bAV | Liechtenstein Life Assurance AG · 1049 | Baloise Holding AG (ehem. Basler) · 852 | Nürnberger Versicherungsgruppe · 523 | LV 1871 a.G. · 517 | HDI Versicherung AG · 343 |
| Sach | VHV Allgemeine Versicherung AG · 1313 | Adam Riese GmbH · 929 | Allianz Versicherungs-AG · 513 | DEVK Versicherungen · 498 | HUK-Coburg · 497 |
| KV Zusatz | AXA Konzern AG · 368 | Bayerische Beamtenkrankenkasse BBKK · 241 | Signal Iduna · 226 | Münchener Verein Versicherung · 210 | Barmenia Versicherungen · 187 |
| KV Voll | Debeka · 59 | ARAG · 58 | DBV Deutsche Beamtenversicherung · 57 | Barmenia Versicherungen · 51 | Signal Iduna · 39 |

## Zuordnung und Nenner

- **Biometrie**: BU, Risikoleben, Grundfähigkeiten, LV mit BUZ, DD, MultiRisk. 2526 Vertragszeilen.
- **Rente / bAV**: Rente, bAV, Riesterrente. 5270 Vertragszeilen.
- **Sach**: PKW, Privathaftpflicht, Hausrat, RS, Unfall, Wohngebäude, Krad, Glas, Anhänger, Hundehaftpflicht, Tierleben, Betriebshaftpflicht, Reise, LKW, HuG, Inhalt, Firmen-RS, VMH, gew. PKW, Elektronik, Traktor, Pferdehaftpflicht, gew. WGV, Wohnmobil, Jagdhaftpflicht, Berufshaftpflicht, Bauversicherung, Kaution, Tech, Boot, Cyber, Öltankhaftpflicht, Ertragsausfall, Transport. 13770 Vertragszeilen.
- **KV Zusatz**: KV-Zusatz. 2742 Vertragszeilen.
- **KV Voll**: PKV. 398 Vertragszeilen.

Nicht in diese fünf Gruppen eingeordnet: Ausbildung, Baufinanzierung, Bausparen, Fonds, GKV, Kapitalleben, Kombi, Kredit, Pflege, Reise-KV, Sonstiges, Sterbegeld, Unbekannt, bKV. Insbesondere werden Pflege, Sterbegeld, Reise-KV, bKV, Kapitalleben und die unklare Sparte Kombi nicht ohne explizite Entscheidung hinzugerechnet. Andere Zuordnungen können Rangfolgen verändern.

## Nachweis

[Alle Rangfolgen und Filter](top5_gesellschaften.json), [Rechenprogramm](rankings.py). Unabhängiger Abgleich: Python Counter und SQLite GROUP BY stimmen für sämtliche Gesellschaften in allen fünf Bereichen überein. Keine Einzelkunden- oder Policendaten gespeichert.
