# ECC · Bestandsanalyse 26.10.2026

## Ergebnis und Geltungsbereich

**FAKT AUS EXPORT:** 50.694 Datensätze repräsentieren keinen reinen aktuellen Zahlungsbestand. Nach der Nutzerlegende sind 29.320 Einträge auf 6.147 Kundennummern aktiv gekennzeichnet. Darunter liegen 805 Einträge mit Stornodatum bis einschließlich 26.10.2026. Die Analyse deckt die gesamte gelieferte CSV ab; die Vollständigkeit sämtlicher Unternehmensbestände ist nicht nachgewiesen. [ECC-BST-001: gesamte Tabelle, `Art`, `Kundennr.`, `Stornodatum`; ECC-BST-002: Vertragsart-Legende]

ECC ist die vom Nutzer vorgegebene Wissensrubrik. Rechtsträger, wirtschaftliches Eigentum, Maklermandate und Kundenübertragbarkeit sind durch diese Datei nicht belegt. Geschäftsmodell, Vergütung, Kosten und regulatorische Einordnung bleiben außerhalb dieses Datenreviews.

## 1. Umfang und Status

| Kennzahl | Wert | Nenner / Grenze |
| --- | --- | --- |
| Alle Vertragsdatensätze | 50.694 | gesamter Export, einschließlich Historie |
| Exakt verschiedene Zeilen | 50.665 | nur identische 21-Feld-Zeilen zusammengefasst |
| Kundennummern gesamt | 6.918 | keine verifizierte Personen-/Haushaltszählung |
| Aktiv gekennzeichnet A/F/H/X/K | 29.320 | gespeicherter Status; X/K enthalten |
| Kunden mit aktivem Status | 6.147 | mindestens eine aktive Zeile |
| Aktive Einträge A/F/H | 26.840 | ohne X/K, keine Courtagebestätigung |
| Kunden mit A/F/H | 5.992 | mindestens eine Zeile dieser Auswahl |
| Kunden ohne aktive Zeile | 771 | können andere laufende Beziehungen haben |
| VMT-Kennungen gesamt / mit aktiven Zeilen | 241 / 234 | keine Zahl aktiver Vertriebspartner |
| Sparten / Gesellschaftsbezeichnungen gesamt | 60 / 378 | Originalbezeichnungen, nicht konzernbereinigt |


| Statusgruppe | Datensätze | Anteil an Export |
| --- | --- | --- |
| aktiv | 29.320 | 57,8 % |
| storniert | 18.409 | 36,3 % |
| abgelegt | 1.561 | 3,1 % |
| beitragsfrei | 899 | 1,8 % |
| beantragt | 228 | 0,4 % |
| in_uebertragung | 277 | 0,5 % |


Fundstellen: ECC-BST-001, gesamte Tabelle; `aggregates.json`: `all`, `exact_unique`, `status_groups`, `active_AFH`, `active_customer_overlap`, `distinct_nonmissing`; Statusdefinition ECC-BST-002. Die 18.409 stornierten Zeilen sind **keine Jahresstornoquote**. Die Kundenzahlen über Statusgruppen sind nicht disjunkt.

## 2. Spartenmix

| Sparte | Aktive Zeilen | Kunden mit aktiver Zeile | Anteil aktiver Zeilen |
| --- | --- | --- | --- |
| Rente | 4.521 | 3.060 | 15,4 % |
| PKW | 3.520 | 2.608 | 12,0 % |
| KV-Zusatz | 2.947 | 2.152 | 10,1 % |
| Privathaftpflicht | 2.813 | 2.682 | 9,6 % |
| RS | 1.782 | 1.675 | 6,1 % |
| Hausrat | 1.665 | 1.583 | 5,7 % |
| BU | 1.627 | 1.508 | 5,5 % |
| Unfall | 1.451 | 1.287 | 4,9 % |
| Wohngebäude | 1.022 | 823 | 3,5 % |
| bAV | 683 | 480 | 2,3 % |
| Risikoleben | 649 | 599 | 2,2 % |
| Kapitalleben | 488 | 471 | 1,7 % |


**BELEGTE SCHLUSSFOLGERUNG:** Rente ist mit 4.521 Zeilen die größte einzelne Sparte innerhalb der aktiven Statusgruppe. Im gesamten historischen Export ist dagegen PKW mit 8.536 Zeilen die größte Sparte. Ohne Statusfilter entsteht daher ein anderes Bild des Produktmixes. [ECC-BST-001: `Sparte` × `Art`; `aggregates.json`: `sparte`, `active_sparte`]

Alle 60 Sparten stehen in [sparten.csv](sparten.csv). Spartenkürzel werden unverändert geführt; keine Zusammenfassung zu nicht belegten Tarif- oder Risikoklassen. Kunden können mehrere Sparten und mehrere Verträge je Sparte haben.

## 3. Gesellschaften und Vermittlerkonzentration

| Gesellschaftsbezeichnung | Aktive Zeilen | Anteil aktiver Zeilen |
| --- | --- | --- |
| Liechtenstein Life Assurance AG | 1.399 | 4,8 % |
| VHV Allgemeine Versicherung AG | 1.333 | 4,5 % |
| Baloise Holding AG (ehem. Basler) | 1.186 | 4,0 % |
| Allianz Versicherungs-AG | 1.148 | 3,9 % |
| Adam Riese GmbH | 933 | 3,2 % |
| Concordia Versicherungsgruppe | 923 | 3,1 % |
| Nürnberger Versicherungsgruppe | 830 | 2,8 % |
| Generali Deutschland Versicherung AG | 721 | 2,5 % |
| Alte Leipziger | 700 | 2,4 % |
| AXA Konzern AG | 673 | 2,3 % |


Die zehn größten Gesellschaftsbezeichnungen enthalten 33,5812 % der aktiven Zeilen. Anbieterbezeichnungen sind nicht konzernbereinigt. Daraus folgt keine Aussage über Produktqualität oder Bilanzrisiko. [ECC-BST-001: `Gesellschaft`, `Art`; `aggregates.json`: `active_companies_top30`, `concentration.active.company_rows`]

**BELEGTE SCHLUSSFOLGERUNG:** Die zehn größten VMT-Kennungen bündeln 45,6617 % der aktiven Datensätze. Die Verteilung ist konzentriert. Es handelt sich um Kennungen, nicht verifiziert um zehn Personen oder zehn aktive Teams. Eine Team-/Hierarchieliste fehlt. [ECC-BST-001: `VMT`, `Art`; `concentration.active.vmt_rows`]

Innerhalb Rente entfallen 41,7 % der aktiven Zeilen auf die Bezeichnungen Liechtenstein Life und Baloise zusammen (1.033 + 852). Keine Aussage über ETF-Anteil, Fondsgüte, Kosten, Garantien oder Beratungsqualität; Tarifdetails fehlen. [ECC-BST-001: `Sparte=Rente`, aktive `Art`, `Gesellschaft`; `rente_active_companies_top10`]

## 4. Kundenstruktur und Betreuungstiefe

Aktive Gruppe: durchschnittlich **4,77 Zeilen je Kundennummer**, Median **4**. 1.367 Kunden haben genau eine aktive Zeile (22,2 %). Bei 268 Kundennummern sind aktive Zeilen mehreren VMT-Kennungen zugeordnet. [ECC-BST-001: `Kundennr.`, `Art`, `VMT`; `active_customers`]

| Alter | Kundennummern | Anteil gültiger Altersangaben |
| --- | --- | --- |
| unter18 | 114 | 1,9 % |
| 18-24 | 480 | 8,0 % |
| 25-34 | 2.182 | 36,5 % |
| 35-44 | 1.508 | 25,3 % |
| 45-54 | 581 | 9,7 % |
| 55-64 | 675 | 11,3 % |
| 65+ | 432 | 7,2 % |


Medianalter 35; 175 aktive Kundennummern ohne Altersangabe. Jede Kundennummer wurde einmal gezählt; Alterswerte derselben Kundennummer sind konsistent. Geschlecht, Haushalt, Region, Einkommen, Vermögen, Familienstand und tatsächlicher Beratungsbedarf sind nicht erfasst. Fehlende Altersangaben können Firmenkonten oder Datenlücken sein; das ist nicht entschieden. [ECC-BST-001: `Alter`, `Kundennr.`, aktive `Art`; `active_customers.age_*`]

### Dokumentierte Spartenpräsenz, keine Versorgungslückenmessung

| Sparte | Kunden mit aktiver Zeile | Anteil an 6.147 |
| --- | --- | --- |
| Privathaftpflicht | 2.682 | 43,6 % |
| Hausrat | 1.583 | 25,8 % |
| BU | 1.508 | 24,5 % |
| Rente | 3.060 | 49,8 % |
| PKW | 2.608 | 42,4 % |
| RS | 1.675 | 27,2 % |
| KV-Zusatz | 2.152 | 35,0 % |
| PKV | 395 | 6,4 % |
| Risikoleben | 599 | 9,7 % |
| Grundfähigkeiten | 315 | 5,1 % |
| bAV | 480 | 7,8 % |
| Riesterrente | 372 | 6,1 % |


5.426 aktive Kundennummern haben eine Altersangabe von 18 bis 64. Davon besitzen 3.881 keine aktive Zeile mit Sparte BU oder LV mit BUZ (71,5 %). Das ist ausschließlich eine Dokumentationsauswahl. Andere Policen, Kombiprodukte, Versorgungsformen, nicht sichtbare Verträge oder fehlende Versicherbarkeit können das Bild verändern. Keine automatische Produktempfehlung und keine medizinische/finanzielle Eignungsentscheidung. [ECC-BST-001: `Alter`, `Sparte`, `Art`, `Kundennr.`; `active_customers`]

**HYPOTHESE:** Ein strukturierter Bestandscheck könnte zusätzliche Beratungsbedarfe sichtbar machen. Erst bei Prüfung des Haushalts, vorhandener Versorgung, Kundenwünsche und Aktualität entsteht ein belegbarer Bedarf. Als Pilotkennzahl eignen sich aktualisierte Datensätze und geklärte Bedarfe, nicht bloß Verkaufsabschlüsse.

## 5. simplr-Nutzung

Von 6.147 aktiven Kundennummern haben 4.304 einen eingetragenen letzten Login (70,0 %), 1.843 keinen.

| Letzter Login innerhalb | Kunden | Anteil an allen aktiven Kundennummern |
| --- | --- | --- |
| 30 Kalendertagen, inkl. Stichtag | 706 | 11,5 % |
| 90 Kalendertagen, inkl. Stichtag | 1.593 | 25,9 % |
| 365 Kalendertagen, inkl. Stichtag | 2.937 | 47,8 % |

Fenster überlappen. Dies sind letzte Login-Daten aus einem Snapshot, keine Zahl der Logins, keine Messung einzelner App-Funktionen und kein Beleg für Kundenbindung oder Zufriedenheit. [ECC-BST-001: `Letzter Login (simplr)`, `Kundennr.`, aktive `Art`; `active_customers.last_login_*`]

## 6. Beiträge: Berechnung mit ausdrücklich offener Semantik

**ANNAHME:** Der eingetragene Beitrag gilt je Zahlperiode. Monatlich ×12, vierteljährlich ×4, halbjährlich ×2, jährlich ×1. Einmalig wird separat gehalten. Die Datei enthält kein Währungsfeld und keine Felddefinition zur Periodenbasis. Zahlen im Folgenden sind rechnerische Geldeinheiten, nicht als bestätigte EUR-Erlöse zu lesen.

Für sämtliche aktiven Kennzeichen ergeben sich **18.153.021,48 netto** und **19.140.683,55 brutto** pro Jahr unter dieser Annahme. 170 Einmaleinträge mit 805.884,99 netto werden nicht annualisiert. Die Einmalwerte sind gespeicherte Beträge, keine bestätigten Zahlungseingänge 2026. [ECC-BST-001: aktive `Art`, `Zahlweise`, Beitragsfelder; `status_groups.aktiv`]

| Auswahl | Datensätze | Jährlich hochgerechnet netto* | Jährlich hochgerechnet brutto* |
| --- | --- | --- | --- |
| Aktive A/F/H | 26.840 | 16.748.751,72 | 17.623.962,49 |
| Aktive ohne vergangenes Stornodatum | 28.515 | 17.664.417,99 | 18.614.110,49 |
| Aktive + Beginn vorhanden und erreicht | 25.289 | 15.927.347,09 | 16.770.207,16 |
| Zusätzlich Ablauf nicht vergangen/leer | 24.726 | 15.576.231,41 | 16.418.246,20 |


\* Ausschließlich Sensitivitätsrechnung. A/F/H ist eine Statusauswahl; die drei folgenden Zeilen verwenden **alle aktiven Kennzeichen einschließlich X/K** mit zunehmenden Datumsfiltern und sind daher nicht direkt mit der ersten Zeile als fortlaufender Filter zu lesen. Ein vergangener Ablauf kann etwa eine Verlängerung benötigen; Ausschluss ist keine Bestätigung tatsächlichen Vertragsendes.

**UNBEKANNT:** Tatsächlich vereinnahmte Courtage, Bestandsprovision, FU, Nettoerlös, Stornohaftung, Cashflow, Gewinn und Unternehmens-/Bestandswert. Beitrag ist kein Vertriebserlös. Der Gesamtbestand enthält zudem unterschiedliche Produktarten; diese sind nicht ungeprüft als reine Versicherungsprämien addierbar. Die berechneten Summen dürfen erst nach Bestätigung von Periodenbasis, Währung und Leistungsstatus für Finanzplanung genutzt werden.

## 7. Historie und Storno

20.737 Zeilen enthalten ein Stornodatum. Davon 20.629 von 1900 bis zum Stichtag, 106 nach dem Stichtag und 2 vor 1900. Das ist eine andere Auswahl als S/Y; Datum und Status sind nicht austauschbar. [ECC-BST-001: `Stornodatum`, `Art`; `storno_date_buckets`]

Beginn-, Antrag- und Stornodatumsverteilungen wurden für alle vorhandenen Jahre und 2026 zusätzlich monatlich berechnet. Oktober ist ein Teilmonat, und der Export enthält bereits künftige Beginn-/Stornodaten. Siehe [Monatsdaten](monate_2026.csv) und `dates_by_year` im JSON. Vertragsbeginn ist nicht gleich Akquisedatum; Bestandsübertragungen und Importe können ältere Beginne enthalten. Keine Aussage über Netto-Neukundengewinnung, echte monatliche Bestandsentwicklung oder jährliche Abwanderungsquote ohne Bewegungsdaten und historischen Nenner.

## 8. Priorisierte Folgearbeit

| Priorität | Befund / Entscheidungsvorschlag | Überprüfbares Ergebnis |
| --- | --- | --- |
| 1 | 805 aktive Zeilen mit vergangenem Stornodatum abgleichen | Je Eintrag Status/Datum geklärt; Ursache und Korrektur protokolliert |
| 1 | Beitragsbasis, Währung und Courtageberechtigung bestätigen | Schriftliche Felddefinition plus Stichprobenabgleich mit Originalpolice/Abrechnung |
| 2 | VMT- und Kundenmehrfachzuordnung klären | Verbindliche Zuordnung je Kennung und Kundenkonto; keine doppelte Teamzählung |
| 2 | 1.367 Einvertragskunden und Spartenpräsenz prüfen | Aktualisierte Versorgung je freiwilligem Beratungstermin; kein pauschales Abschlussziel |
| 3 | Periodische Bestandsentwicklung aufbauen | Monatliche Snapshots mit stabiler Vertrags-ID, Ein-/Austrittsdatum und Statushistorie |

Das sind Vorschläge auf Basis der Daten, keine bereits durchgeführten Kundenaktionen. Rechtliche Übertragbarkeit und wirtschaftliche Bewertung erfordern gesonderte Unterlagen. Keine Rangfolge gegenüber Königswege oder Finanzgenies, da vergleichbare empirische Nenner fehlen.
