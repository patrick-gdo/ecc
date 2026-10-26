# ECC · Vertragsarten und Zählregeln

Stand: 26.10.2026. Quelle **ECC-BST-002**, Nutzer-Screenshot „Bildschirmfoto 2026-10-26 um 14.20.05.png“, vollständige ausgelesene Textlegende „Vertragsart“. Zählwerte: **ECC-BST-001**, Spalte `Art`, sämtliche 50.694 Datenzeilen.

| Code | Bedeutung laut Screenshot | Datensätze | Kundennummern |
| --- | --- | --- | --- |
| B | beantragt | 199 | 174 |
| A | aktiv | 19.357 | 4.883 |
| N | beitragsfrei | 525 | 450 |
| H | aktiv Honorar | 0 | 0 |
| S | storniert | 12.982 | 3.648 |
| P | abgelegt | 1.342 | 964 |
| E | beantragt (DV) | 29 | 29 |
| F | aktiv (DV) | 7.483 | 2.755 |
| R | beitragsfrei (DV) | 374 | 276 |
| U | in Bestandsübertragung | 233 | 128 |
| X | aktiv ohne Betreuung | 2.451 | 1.221 |
| Y | storniert (DV) | 5.427 | 2.275 |
| Z | abgelegt (DV) | 219 | 159 |
| K | aktiv Korrespondenz | 29 | 25 |
| V | in Komplettübertragung | 44 | 35 |


**Korrektur gegenüber dem vorläufigen Untersuchungsansatz:** F ist „aktiv (DV)“ und wird nicht als Fremdvertrag interpretiert. Die Screenshot-Legende ersetzt die zuvor unvollständige Statuszuordnung. Kein offener Statuscode im Export; H ist in der Legende enthalten, im Export aber nicht vertreten.

Gruppen:

- Aktiv gekennzeichnet: A, F, H, X, K = 29.320 Datensätze.
- Davon A/F/H: 26.840; X: 2.451; K: 29.
- Storniert: S/Y = 18.409.
- Abgelegt: P/Z = 1.561.
- Beitragsfrei: N/R = 899.
- Beantragt: B/E = 228.
- In Übertragung: U/V = 277.

Die sechs Gruppen sind disjunkt und summieren sich auf 50.694. Kundenzahlen dürfen zwischen Gruppen nicht addiert werden; dieselbe Kundennummer kann mehrere Statusarten haben.

**Grenzen:** DV ist im Screenshot nicht ausgeschrieben. Keine eigenmächtige Auflösung der Abkürzung. Aktiv ohne Betreuung und Korrespondenz sind separat zu führen. Kein Status beweist allein Courtageberechtigung, Eigentum, aktuelle Zahlung oder Übertragbarkeit. Aktiv ist ein gespeichertes Kennzeichen, keine unabhängige Bestandsbestätigung durch den Versicherer.
