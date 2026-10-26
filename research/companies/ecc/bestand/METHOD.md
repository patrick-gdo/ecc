# ECC · Methodik und Datenwörterbuch

## Stichtag, Herkunft und Filter

Stichtag für alle zeitbezogenen Filter: **26.10.2026**. Quelle ECC-BST-001 vollständig eingelesen; Quelle ECC-BST-002 bestimmt Statusbedeutungen. Keine Beschränkung auf bestimmte VMTs, Gesellschaften oder Sparten. Datei-Hash in SOURCES.md und sources.json. Keine Aussage, dass der bereitgestellte Export alle Systeme, Rechtsträger oder alle Kunden ohne Vertragszeile umfasst.

## Zähleinheiten

1. **Zeile** ist die primäre Vertragsdatensatz-Einheit. Keine ungeprüfte Behauptung einer eindeutigen Police.
2. **Kunde** bedeutet verschiedene nichtleere Kundennummer innerhalb der angegebenen Auswahl. Nicht Personen oder Haushalte. Kunden-/Spartenmengen können überlappen.
3. **VMT** bedeutet Kennung. Keine Ableitung von aktiven VPs oder Organisationshierarchie.
4. **Aktiv** bedeutet Art in A/F/H/X/K gemäß Screenshot. X und K werden separat sichtbar gehalten. A/F/H ist eine zusätzliche, klar benannte Auswahl.
5. **Dubletten:** Primär alle Zeilen erhalten. Separat exakte 21-Feld-Zeilen ohne Mehrfachvorkommen gerechnet. Identische Vertragsnummer allein reicht nie zur Zusammenführung.

## Rechenannahmen

- Leer und Bindestrich gelten als fehlend. Keine Nullwerte aus fehlenden Beiträgen erzeugt.
- Deutsches Zahlenformat wird mit Decimal geparst; unabhängiger SQL-Abgleich in Ganzzahl-Cent.
- Jahresbeitragsszenario: Netto/Brutto je Zeile × 12/4/2/1 nach Zahlweise. Einmalig separat. **Periodenbasis und Währung sind nicht in der Quelle definiert.** Originalwerte nicht mit Erlösen, Bestandsprovision, AUM oder Bilanzgrößen verwechseln.
- Datumsfiltersichten sind Sensitivitäten, keine neue fachliche Vertragswahrheit. Fehlender Beginn wird bei „Beginn erreicht“ ausgeschlossen; fehlender Ablauf wird im zusätzlichen Ablaufcheck akzeptiert. Keine automatische Korrektur des Quellsystems.
- App-Fenster inklusive 26.10.2026: 30 Tage ab 27.09.2026, 90 Tage ab 29.07.2026, 365 Tage ab 27.10.2025. Kundennummer nur einmal zählen; bei widersprüchlichen Logins wäre der neueste zu verwenden. Im Datensatz keine solchen Konflikte.
- Altersdurchschnitt/Median sind kundenbezogen, nicht vertragsgewichtet. Fehlende Alterswerte ausgeschlossen; Nenner separat genannt.
- Konzern-, Tarif-, Berufs- und Haushaltsharmonisierung nicht vorgenommen.
- Beginnkohorten haben unterschiedliche Beobachtungsdauer. Keine naive Stornoquotenrangfolge, keine Kausalität und keine Umsatzprognose daraus.

## Felder

| Spalte | Bedeutung und Grenze |
| --- | --- |
| VMT | Vermittlerkennung; keine bestätigte Personen-, Team- oder Aktivitätsliste. |
| Kundennr. | Schlüssel für Kundenzählung; nicht verifiziert als eindeutige natürliche Person/Haushalt. |
| Vorname / Ansprechpartner | Personenbezogen; nur Vollständigkeit, keine Veröffentlichung. |
| Alter | Integer-Alter laut Export; je Kundennummer einmal. Datum der Altersberechnung fehlt. |
| Beruf | Freitext, nicht normiert; nur Vollständigkeit. Keine Berufsgruppen-Klassifikation. |
| Erster Login (simplr) | Datum je Kundennummer; keine Installations- oder Einwilligungsmessung. |
| Letzter Login (simplr) | Letztes eingetragenes Datum, keine vollständige Ereignishistorie. |
| VSN | Vertrags-/Versicherungsscheinnummer; nicht global eindeutig, keine Veröffentlichung. |
| Sparte | Originalkategorie; keine automatische Gleichsetzung mit Versicherungsbedarf. |
| Risiko | Freitext kann personenbezogen sein; nur Vollständigkeit, keine Rohtexte. |
| Art | Vertragsart-Code gemäß Nutzer-Screenshot ECC-BST-002. |
| Vorversicherung | Originalfreitext; kein Beleg eines erfolgreichen Anbieterwechsels. |
| Gesellschaft | Originalbezeichnung; keine Konzern- oder Namensnormalisierung. |
| Agentur | Originalzuordnung; keine bestätigte Courtageberechtigung; keine Einzelagenturausgabe. |
| Beginn | Gespeicherter Beginn; nicht gleich Neukunden-/Vertriebsdatum. |
| Ablauf | Gespeicherter Ablauf; Verlängerungen und Platzhalter beachten. |
| Antrag | Gespeichertes Antragsdatum; keine Erfolgsmessung. |
| Stornodatum | Gespeichertes Datum; kann fehlen, künftig oder widersprüchlich sein. |
| Zahlweise | Monatlich/vierteljährlich/halbjährlich/jährlich/einmalig. |
| Netto-Beitrag | Dezimalzahl; Periodenbasis/Währung unbestätigt; kein Nettoumsatz. |
| Brutto-Beitrag | Dezimalzahl; Periodenbasis/Währung unbestätigt; kein Vertriebserlös. |


## Datenschutz und Weiterverwendung

Nur eigene aggregierte Kennzahlen, Rechenlogik und Quellenmetadaten ins private Repository. Keine Original-CSV, Kundennummern, VSN, VMT-IDs, Namen, Berufs-/Risiko-/Agentur-Freitexte oder verknüpfbare Einzelzeilen. Vorhandene vertrauliche Originale bleiben in der vom Nutzer gewählten Quelle. Aggregate erlauben keine pauschale Berechtigung zu Kundenkontakt oder Migration.

## Reproduktion

Python 3.9+; Standardbibliothek genügt:

```bash
python3 analyze.py --input /berechtigter/pfad/bestand.csv --output /tmp/aggregates.json --as-of 2026-10-26
```

Bei neuer Datei zuerst Hash und Schema vergleichen; nicht so tun, als wäre ein veränderter Export identisch. `analyze.py` schreibt ausschließlich Aggregate. `aggregates.json` ist die rechnerische Grundlage; CSVs und Bericht sind daraus abgeleitete Ansichten.
