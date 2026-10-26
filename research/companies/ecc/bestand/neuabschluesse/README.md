# ECC · Top-Gesellschaften bei Vertragsbeginn seit 2024 und seit 2025

Stichtag **26.10.2026**, beide Datumsgrenzen einschließlich. Zwei überlappende Zeiträume, keine Addition. Nutzerfrage nach Neuabschlüssen operationalisiert über das Feld **Beginn**, nicht über Antragsdatum oder Erfassungsdatum. Ein gesonderter Nachweis der ursprünglichen Eigenvermittlung fehlt. Quellen ECC-BST-003/004, Statuslegende ECC-BST-002.

**Rangfolge nach Anzahl der Vertragszeilen**, nicht Beitrag oder Provision. Enthalten sind aktiv, beitragsfrei und storniert: A/F/H/N/R/S/Y. Nur beantragte B/E, abgelegte P/Z und Übertragungsstatus U/V bleiben ausgeschlossen; ebenfalls X ohne Betreuung und K Korrespondenz. Stornierte Zeilen sind bewusst enthalten, weil die Frage das historische Abschlussaufkommen und nicht nur heute aktive Verträge betrifft. Der Status allein beweist keinen tatsächlich policierten bzw. bezahlten Neuabschluss.

Die bisherige [Top-5-Bestandsauswertung](../TOP5_GESELLSCHAFTEN.md) verwendet nur A/F/H und hat keinen Beginnfilter. Ihre Zahlen sind deshalb nicht direkt vergleichbar. Gesellschaften bleiben getrennt nach Originalbezeichnung; Kurzbezeichnungen unten nur zur Lesbarkeit. AXA und DBV werden nicht zusammengelegt.

## Beginn 01.01.2024 bis 26.10.2026

| Sparte | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Biometrie | Hannoversche · **117** | Canada Life · **94** | Swiss Life · **88** | Baloise · **77** | Signal Iduna · **60** |
| Rente / bAV | Baloise · **971** | LV 1871 · **260** | Alte Leipziger · **210** | HDI · **148** | Nürnberger · **141** |
| Sach | VHV · **780** | Adam Riese · **489** | Helvetia · **476** | Itzehoer · **330** | Ammerländer · **309** |
| KV Zusatz | AXA · **418** | BBKK · **169** | Continentale · **71** | Allianz · **57** | Barmenia · **54** |
| KV Voll | ARAG · **36** | Barmenia · **31** | DBV · **7** | AXA · **3** | Allianz · **3** |

KV Voll: AXA und Allianz teilen sich Rang 4 mit je 3 Zeilen.

## Beginn 01.01.2025 bis 26.10.2026

| Sparte | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Biometrie | Hannoversche · **88** | Swiss Life · **65** | Baloise · **56** | Canada Life · **49** | Allianz · **39** / Continentale · **39** |
| Rente / bAV | Baloise · **663** | Alte Leipziger · **195** | LV 1871 · **174** | HDI · **88** | Nürnberger · **61** |
| Sach | VHV · **551** | Adam Riese · **316** | Ammerländer · **237** | Allianz · **232** | HFK1676 · **232** |
| KV Zusatz | AXA · **303** | BBKK · **88** | Allianz · **54** | Continentale · **47** | Barmenia · **32** |
| KV Voll | ARAG · **29** | Barmenia · **26** | DBV · **6** | AXA · **2** | Allianz · **2** |

Biometrie: Allianz und Continentale teilen sich Rang 5 mit je 39 Zeilen. Sach: Allianz und HFK1676 teilen sich Rang 4 mit je 232 Zeilen. KV Voll: AXA und Allianz teilen sich Rang 4 mit je 2 Zeilen.

## Rechenbasis und Prüfung

| Kennzahl | Ab 2024 | Ab 2025 |
| --- | ---: | ---: |
| Exportzeilen gesamt | 11640 | 8159 |
| Beginn nach Stichtag, ausgeschlossen | 419 | 419 |
| Zeilen im Datumsfenster | 11221 | 7740 |
| Davon nach Status ausgeschlossen | 737 | 536 |
| Ausgewählte Zeilen über alle Sparten | 10484 | 7204 |
| Davon in den fünf abgefragten Bereichen | 10071 | 6966 |
| Nur aktive A/F/H über alle Sparten (Alternative) | 7876 | 5958 |
| Exakte zusätzliche Doppelzeilen in Hauptauswertung | 0 | 0 |

Alle 19.799 Eingabezeilen aus beiden Dateien vollständig gelesen; dies sind wegen Überlappung keine 19.799 verschiedenen Verträge. Alle Beginnwerte sind syntaktisch gültig. Beide Exporte enthalten je 419 künftige Beginne nach dem Stichtag, einschließlich 180 im Jahr 2027. Keine automatische Dublettenbereinigung. In jedem Hauptfenster besteht eine zusätzliche Zeile mit gleichem Kandidatenschlüssel aus Kunde, Gesellschaft, VSN und Sparte; die Zeilen sind nicht vollständig identisch und bleiben erhalten. Deshalb ist die Zähleinheit Vertragsdatensatz, nicht garantiert eindeutige Police.

Der 2025-Export entspricht in Sparte, Art, Gesellschaft und Beginn exakt der entsprechenden Teilmenge des 2024-Exports. Bei vollständigem 18-Feld-Vergleich unterscheiden sich zwei Zeilen ausschließlich im Feld „Letzter Login (simplr)“. Diese Änderungen beeinflussen die Ranglisten nicht.

Alle vollständigen Gesellschaftsrangfolgen beider Zeitfenster und dreier Statussichten unabhängig mit Python Counter und SQLite GROUP BY abgeglichen. Summen über Gruppen und nicht zugeordnete Sparten stimmen. In den fünf Hauptgruppen fehlen keine Gesellschaftsangaben. Gleichstände werden explizit ausgegeben.

## Bereiche und Grenzen

Die Zuordnung entspricht der bisherigen Bestandsauswertung:

- **Biometrie:** BU, Risikoleben, Grundfähigkeiten, LV mit BUZ, DD, MultiRisk. Nenner ab 2024: 1050; ab 2025: 681.
- **Rente / bAV:** Rente, bAV, Riesterrente. Nenner ab 2024: 1847; ab 2025: 1251.
- **Sach:** PKW, Privathaftpflicht, Hausrat, RS, Unfall, Wohngebäude, Krad, Glas, Anhänger, Hundehaftpflicht, Tierleben, Betriebshaftpflicht, Reise, LKW, HuG, Inhalt, Firmen-RS, VMH, gew. PKW, Elektronik, Traktor, Pferdehaftpflicht, gew. WGV, Wohnmobil, Jagdhaftpflicht, Berufshaftpflicht, Bauversicherung, Kaution, Tech, Boot, Cyber, Öltankhaftpflicht, Ertragsausfall, Transport. Nenner ab 2024: 6071; ab 2025: 4301.
- **KV Zusatz:** KV-Zusatz. Nenner ab 2024: 1017; ab 2025: 664.
- **KV Voll:** PKV. Nenner ab 2024: 86; ab 2025: 69.

Nicht hinzugerechnet werden insbesondere Kapitalleben, Pflege, Sterbegeld, Reise-KV, bKV und Kombi. Keine Aussage über Vollständigkeit sämtlichen Unternehmensneugeschäfts; kein Schluss auf Umsatz, Courtage, Bestandswert oder rechtliche Inhaberschaft. „Abgelegt“ ist kein eindeutiger Abschlussnachweis. Die Alternative einschließlich P/Z sowie eine reine Aktivsicht liegen maschinenlesbar vor, damit eine andere fachliche Definition nachvollziehbar nachgerechnet werden kann.

## Wiederverwendung

- [Alle Rangfolgen, Filter und Prüfergebnisse](results.json)
- [Quellen, Fundstellen und Hashes](SOURCES.md)
- [Rechenprogramm](analyze_new_business.py)

```bash
python3 analyze_new_business.py --from-2024 /berechtigter/pfad/export_ab2024.csv --from-2025 /berechtigter/pfad/export_ab2025.csv --as-of 2026-10-26 --output /tmp/results.json
```

Python 3.9+ mit Standardbibliothek. Keine Rohdaten, Kunden- oder Policenkennungen im Repository. Für einen neuen Stichtag aktuelle Exporte nutzen; die vorhandene Momentaufnahme enthält keine spätere Statushistorie.
