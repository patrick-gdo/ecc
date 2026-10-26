# ECC · Vorbereitung auf gezielte Folgefragen

## Direkt beantwortbar aus dem analysierten Export

- Wie viele Vertragsdatensätze, Kundennummern, Sparten und Gesellschaftsbezeichnungen? Immer Status-/Zeitfilter nennen.
- Wie verteilen sich aktive, stornierte, abgelegte, beitragsfreie, beantragte und in Übertragung befindliche Einträge?
- Welche Sparten/Gesellschaften dominieren Gesamtbestand, aktive Gruppe oder A/F/H-Auswahl?
- Wie viele aktive Datensätze je Kundennummer; welche Altersstruktur und dokumentierte Spartenpräsenz?
- Wie viele Kunden haben einen gespeicherten letzten simplr-Login in 30/90/365 Tagen?
- Wo liegen Datenlücken und Status-/Datumswidersprüche?
- Wie konzentrieren sich Vertragszeilen auf VMT-Kennungen? Keine automatische Personen-/Hierarchiezuordnung.
- Welche rechnerischen Jahresbeiträge entstehen unter ausdrücklich benannter Periodenannahme?

## Nur mit zusätzlichem Abgleich

| Frage | Fehlende Grundlage |
| --- | --- |
| Wie viel laufende Bestandsprovision/Umsatz verdienen wir? | Courtagesätze, Berechtigung, Abrechnungen, Zahlungseingänge, Splits und Rückbelastungen |
| Was ist der Bestand oder ECC wert? | Wiederkehrender Nettoerlös, Kosten, Kundenbindung, Stornohaftung, Erwerberkriterien, rechtliche Übertragbarkeit |
| Wem gehören die Kunden und was darf mitgenommen werden? | Mandate, Verträge, Rechteketten und rechtliche Prüfung |
| Wie hoch ist unsere echte Jahresstornoquote? | Einheitliche Formel, Startbestand, Bewegungen, Neu-/Altgeschäft, Perioden und Abgrenzung |
| Welche Mitarbeiter/VPs sind aktiv oder sollen mitgehen? | Verbindliche VMT-Personen-/Hierarchiezuordnung und Aktivitätsdefinition |
| Wie viele Neukunden haben wir pro Monat gewonnen? | Kundenanlage-/Akquisedatum und vollständige Zu-/Abgänge |
| Welche Kunden sind unterversichert? | Bedarf, Haushalt, externe Verträge, Produktbedingungen und aktuelle Beratung |
| Welche Rentenprodukte sind ETF-Produkte / hochwertig / teuer? | Tarif- und Fondsdetails, Bedingungen, Kosten und Kundenanforderungen |
| Wie gut ist unsere Beratung gegenüber KW/FG? | Vergleichbare Qualitäts-/Ergebniskennzahlen mit gleichem Nenner und Zeitraum |

## Regeln für Folgeantworten

1. Zuerst den Stichtag 26.10.2026 und die Auswahl aus STATUS_LEGEND.md verwenden oder explizit einen anderen Filter definieren.
2. Aggregate in `aggregates.json` prüfen. A allein ist nicht der gesamte aktive Bestand; F bedeutet aktiv (DV).
3. Bei bislang nicht gespeicherten Kreuztabellen berechtigten Originalexport erneut heranziehen. Hash prüfen. Neue Fragen nicht aus Teilmengen hochrechnen.
4. Nur aggregierte Erkenntnisse in ECC ergänzen. Kundenspezifische Details nicht ins Git-Repository schreiben.
5. Fakt aus Export, rechnerische Annahme, Schlussfolgerung, Hypothese und unbekannte Größe auseinanderhalten.
6. Zukünftige Datensnapshots getrennt versionieren; diese Analyse ist kein automatisch aktueller Live-Bestand.
