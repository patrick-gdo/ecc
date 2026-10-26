# ECC · Datenqualität und Prüfstatus

Quelle ECC-BST-001, alle 50.694 Zeilen und 21 Spalten. Statuszuordnung nach ECC-BST-002. Berechnungsnachweis `aggregates.json`, Abschnitte `duplicates`, `quality`, `date_quality`, `active_checks`, `missingness`, `validation`.

## Kritische Befunde

| Befund | Umfang | Einordnung |
| --- | --- | --- |
| Aktiv markiert und Stornodatum bis Stichtag | 805 | Status-/Datumsabgleich erforderlich; nicht automatisch als laufend oder beendet festlegen |
| Aktiv markiert und künftiges Stornodatum | 14 | Kann geplante Beendigung sein; keine automatische Fehlerdiagnose |
| Aktive Zeile ohne Beginn | 2.954 | Zahlungs-/Laufzeitprüfung eingeschränkt |
| Aktive Zeile mit künftigem Beginn | 314 | Zukunftsbestand separat behandeln |
| Aktive Zeile mit vergangenem Ablauf | 653 | Verlängerung oder Datenpflege möglich; keine automatische Löschung |
| Aktive Zeile mit Nettobeitrag null | 1.399 | Fehlender Beitrag, beitragsfreie Phase oder andere Semantik möglich |
| Stornodatum vor 1900 | 2 | Minimum 1016-02-25; klarer fachlicher Prüfbedarf |
| Ablauf nach 2100 | 27 | Maximum 9999-01-01; möglicher Platzhalter |
| Stornodatum vor Vertragsbeginn | 1.020 | Kann Rücknahme vor Beginn sein; nicht pauschal Datenfehler |
| Gleiche Kunden-/Gesellschafts-/VSN-/Spartenkombination | 270 Gruppen / 580 betroffene Zeilen | Dublettenkandidaten; Teilrisiken/Versionen nicht ausgeschlossen |

Die Prüfmengen überlappen und dürfen nicht addiert werden. Insgesamt 10 Gruppen vollständig identischer Zeilen mit 29 zusätzlichen Zeilen. Ohne diese Zeilen verbleiben 50.665; die 29.320 aktiven Einträge sind von exakten Doppelzeilen nicht betroffen. Innerhalb aktiver Status: 42 mögliche Mehrfachgruppen nach Kunden-/Gesellschafts-/VSN-/Spartenschlüssel, 44 zusätzliche Zeilen. Keine automatische fachliche Zusammenführung ohne stabile Vertrags-ID.

## Fehlende Werte

| Feld | Leer oder „-“ | Anteil aller Zeilen |
| --- | --- | --- |
| VMT | 0 | 0,0 % |
| Kundennr. | 0 | 0,0 % |
| Vorname / Ansprechpartner | 174 | 0,3 % |
| Alter | 633 | 1,2 % |
| Beruf | 11.885 | 23,4 % |
| Erster Login (simplr) | 8.881 | 17,5 % |
| Letzter Login (simplr) | 8.881 | 17,5 % |
| VSN | 6 | 0,0 % |
| Sparte | 0 | 0,0 % |
| Risiko | 12.595 | 24,8 % |
| Art | 0 | 0,0 % |
| Vorversicherung | 45.584 | 89,9 % |
| Gesellschaft | 24 | 0,0 % |
| Agentur | 17.749 | 35,0 % |
| Beginn | 5.402 | 10,7 % |
| Ablauf | 10.396 | 20,5 % |
| Antrag | 29.024 | 57,3 % |
| Stornodatum | 29.957 | 59,1 % |
| Zahlweise | 0 | 0,0 % |
| Netto-Beitrag | 0 | 0,0 % |
| Brutto-Beitrag | 0 | 0,0 % |


Leere Storno-/Vorversicherungs-/Loginfelder sind nicht automatisch Fehler. Personenfelder werden nur auf Vollständigkeit geprüft; Namen, Berufe, Risikotexte, Kundennummern, VSN und VMT-IDs werden nicht veröffentlicht.

## Technische und rechnerische Abnahme

- 50.694 Datenzeilen mit exakt 21 Spalten; keine abgeschnittene Tabellenstichprobe.
- Alle vorhandenen Geldwerte und Datumswerte syntaktisch parsebar. Syntaktisch gültig bedeutet nicht fachlich richtig.
- Keine negativen Beiträge, kein Bruttobeitrag kleiner als Nettobeitrag, kein Ablauf vor Beginn und kein letzter Login vor erstem Login in der Datei.
- Zeilen-/Kundenzahl und jährliche Rechensummen unabhängig mit SQLite in Ganzzahl-Cent abgeglichen.
- Status-, Sparten- und Zahlweisensummen mit Gesamtsumme abgeglichen; Statuslegende deckt alle vorhandenen Codes ab.
- Kundenverteilungen und Altersklassen auf Nenner abgeglichen. Keine abweichenden Alters-/letzten Loginwerte innerhalb derselben Kundennummer festgestellt.

**Offen:** Vollständigkeit gegenüber Quellsystem, Aktualität je Datensatz, stabiler Vertragsschlüssel, echte Leistungs-/Zahlungszustände, semantische Beitragseinheit, VMT-Hierarchie und wirtschaftliche Berechtigung.
