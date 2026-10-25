# KW-Live-Intranet: Geschäftsmodell, Prozesse und Regelkonflikte

Stand und Abruf: **25.10.2026**. Ergänzung der [bisherigen Königswege-Analyse](../ANALYSIS.md). Quellen-IDs und genaue Prüfumfänge stehen in [SOURCES.md](SOURCES.md) und [sources.json](sources.json).

## 1. Ergebnis und Beweisgrenze

**Beobachteter Zugriff:** Das KW-Intranet war in der authentifizierten Browsersitzung tatsächlich lesbar. Auch das private Repository `patrick-gdo/ecc`, Branch `main`, war zugänglich. Der frühere KW-Zugriffsblocker ist damit für diesen Durchlauf aufgehoben. Das separate KWIF-Live-Intranet wurde nicht erneut geprüft. [KW-IN-P081; ../INTRANET_ACCESS.md]

Die Auswertung umfasst 74 gezielte Seitenreviews sowie 19 Dokumentreviews, davon eine nur visuell und ausschnittsweise lesbare Vorlage. Hinzu kommen vier Seiten mit bloßer Metadaten-/Einbettungserfassung, fünf ausgeschlossene Navigationsziele, eine bewusst ausgelassene Rangliste und ein fehlerhafter interner Link. Zwei weitere Dokumentabrufe scheiterten. Die 85 Seitenpositionen sind kein Nachweis sämtlicher existierender oder verborgener Intranetseiten. Die Auswahl der Dokumente konzentriert sich auf das Geschäftsmodell und wesentliche Prozess-/Haftungsbedingungen; verlinkte Ordner, Tariflisten, Videos und alle Fachunterlagen wurden nicht vollständig geprüft.

**Einordnung:** Das Intranet beschreibt ein umfangreiches Betriebssystem für Partnergewinnung, Beratung, Spezialisten, Verwaltung, Karriere und Abrechnung. Seine Stärke als Dokumentensammlung liegt in konkreten Zuständigkeiten und Formularen. Seine wesentliche Schwäche als Planungsgrundlage liegt in uneinheitlichen Regelständen, vereinfachenden Fachannahmen und nicht vollständig zusammenpassenden Seiten-/Vertragsangaben. Das ist ein dokumentarischer Befund, keine Aussage über die Häufigkeit tatsächlicher Fehlberatung oder Abrechnungsfehler.

Online University einschließlich eindeutig zugehöriger Inhalte blieb außerhalb der Sachauswertung. Schulungsziele wurden vorsorglich ausgelassen; gemischte Seiten nur ohne zugehörige Passagen ausgewertet. Keine Zugangsdaten, Kundenakten, personenbezogenen Ranglisten, Originalverträge oder Rohseiten wurden gespeichert.

## 2. Architektur und Leistungsversprechen

### Kundenerfassung, Betreuung und Reporting

**Unternehmensbeschreibung:** VPP dient der Kundenerfassung und Beratungsvorbereitung. Die aufgeklappten Erläuterungen beschreiben Immobilien-Scoring, Rentenlückenberechnung und Team Reporting. Letzteres enthält gemeldete Prognose-, Plan- und Istwerte; Wachstumszahlen sollen nur vollständig onboardete Partner zählen. Die Startseite nennt zusätzliche Controlling-Reports. VPM erläutert Vertriebs-, Struktur- und Abrechnungskennzahlen. [KW-IN-P002, Abschnitte „Team Reporting“ und Rechner; KW-IN-P007, Dashboard/Kennzahlen; KW-IN-P081, Reports-Hinweis]

**Interpretation:** Gemeldete Prognosen, automatisch gezählte Partner und abgerechneter Umsatz dürfen nicht in einer gemeinsamen Erfolgskennzahl verschwimmen. Ein Onboarding-Abschluss ist noch kein Nachweis aktiver Beratung. Die beschriebenen Kontrollen wurden nicht in einer operativen Kunden- oder Partnerdatenbank getestet.

| Werkzeug / Angebot | Beschriebene Rolle | Wirtschaftliche und operative Grenze |
| --- | --- | --- |
| Deeplico / Mailien | Automatisierte Kommunikation, Synchronisierung und Erinnerungen | Seite nennt 20 Euro monatlich für Deeplico bzw. 81 Euro für Mailien einschließlich Deeplico, zusätzlich volumenabhängige Gebühren. Preisstand nur als interne Angabe; eine Erinnerung beweist kein durchgeführtes Betreuungsgespräch. [P003] |
| Thronblick | Vernetzung von Beratung und Organisation | Seite mischt als verfügbar beworbene Funktionen und zukünftige Integrationen/Mobilfunktionen. Tarife und Nutzen nicht extern getestet. [P005] |
| NAFI | Ergänzung für komplexere Kfz-Fälle | Datenübernahme muss gegebenenfalls manuell kontrolliert werden; Schnittstellen schließen Nacharbeit nicht aus. [P006] |
| Xempus | Digitaler bAV-Prozess | Laut Seite ohne zusätzliche Plattformgebühr; daraus folgt keine Kostenfreiheit aller Produkte oder Beratungsleistungen. [P009] |
| Qonekto | Integration und Automatisierung | Preisangaben tragen einen älteren Stand; Wirtschaftlichkeit hängt von Fallzahl und eingesparter Arbeit ab. [P010] |

Kurz-IDs in Tabellen wie P003 bedeuten stets **KW-IN-P003**. Beschreibungen sind Eigenaussagen, keine Funktionsabnahmen.

**Gestaltungshypothese:** Für ein eigenes Modell sollte jede technische Übergabe eine verantwortliche Rolle und einen Nachweis erhalten: Kundenanlage → Einwilligung/Mandat → Beratung → Antrag → Policierung → Abrechnung → Betreuung. Fehlerquote, Nachbearbeitungszeit und Kosten pro vollständig bearbeitetem Fall wären aussagekräftiger als die Anzahl verfügbarer Tools. Noch keine Produktentscheidung.

### Beratungsrechner: Plausibilität vor vertrieblicher Wirkung

**Dokumentierter Ansatz:** Der Immobilien-Score kombiniert standardisierten Cashflow und Vermögensüberschuss. Die Seite bezeichnet ihn selbst als Tendenz, nicht als sichere Finanzierungszusage. [KW-IN-P002, „Analyse: Berechnung des Immobilien-Scores“]

Der Rentenlückenrechner setzt in der Standardbeschreibung den heutigen Rentenanspruch mit **48 % des Nettogehalts** an. Weitere Annahmen betreffen Einkommens-/Rentenentwicklung, 85 % gewünschtes Ruhestandseinkommen, Entnahmerate und Steuern. Die Erklärung nennt auch einen vertrieblichen Einsatz des Aufschubvergleichs. [KW-IN-P002, „Beratungstool: Berechnungsmethode des Rentenlückenrechners“]

**Externer Abgleich:** Das Rentenniveau ist laut Deutscher Rentenversicherung eine gesamtwirtschaftliche Relation einer standardisierten Rente nach 45 Durchschnittsverdienstjahren zum Durchschnittseinkommen, vor Steuern. Für eine persönliche Hochrechnung verweist die DRV auf Erwerbsbiografie und Renteninformation. [KW-IN-E04, Begriffsdefinition; KW-IN-E05, Einleitung/Onlineberechnung]

**Bewertung:** Aus der Kennzahl 48 % folgt kein individueller Anspruch von 48 % des aktuellen Nettogehalts. Die dokumentierte Standardannahme ist daher nur eine grobe Modellannahme und als persönliche Prognose nicht ausreichend. Ob Nutzer im tatsächlichen Tool eigene Renteninformationen einsetzen können und welche Voreinstellung aktuell aktiv ist, wurde nicht getestet. Für ein eigenes Modell wären nachvollziehbare individuelle Eingaben, Bandbreiten und eine klare Trennung von Bedarfsermittlung und Verkaufsargumentation zu prüfen.

## 3. Partnerlebenszyklus und persönliche Risiken

### Eintritt und Bürgschaft

**Dokumentierte Regeln:** Die Onboarding-Checkliste unterscheidet Startunterlagen und innerhalb von sechs Wochen nachzureichende Nachweise. Gewerbebeginn, Vertragsbeginn und Erlaubnisse müssen zusammenpassen. Die Oktober-Unterlage zur Bonität nennt einen Score von mindestens 642 oder eine Leerauskunft; bei geringerem Score wird eine Bürgschaft einer Führungskraft ab Senior Manager vorgesehen. Eine Verbesserung des Scores beendet die Bürgschaft nicht automatisch. [KW-IN-P012/P013; KW-IN-D02, Score/Bürgschaft/Entlassung; KW-IN-D03, S. 1]

Die verlinkte Bürgschaftsvorlage sieht eine weitreichende, selbstschuldnerische Sicherheit für gegenwärtige und künftige Ansprüche einschließlich Nebenforderungen vor. Die Entlassung nach § 9.2 hängt von weiteren Voraussetzungen und einer Entscheidung von KW ab. [KW-IN-D11, S. 1–5, insbesondere § 9.2]

**Abgrenzung zur bisherigen Analyse:** Die separat verlinkte Zusatzvereinbarung für Geschäftsführer und Gesellschafter enthält in dem visuell lesbaren Ausschnitt ebenfalls eine persönliche selbstschuldnerische Bürgschaft für Ansprüche gegen den gesellschaftsgebundenen Vertriebspartner. Das ist eine andere Vorlage und ein anderer Sicherungsanlass als die Anwerberbürgschaft. Der zuvor offene Dokumentenbeleg für diese Unterscheidung ist damit teilweise ergänzt; die Zusatzvereinbarung ist nicht vollständig geprüft. [KW-IN-P041; KW-IN-D10, S. 2 Ziff. 3 a–c; ergänzend bisherige Partneranalyse]

**Lehre:** Partnergewinnung und gesellschaftsrechtliche Haftungsbegrenzung getrennt erklären. Für die Liquiditätsplanung zählen nicht nur erwartete Ausschüttungen, sondern auch eigene Sicherheiten und übernommene Bürgschaften. Keine Bewertung individueller Vertragswirksamkeit.

### Karriere, Wechsel und Struktur

**Dokumentierter Prozess:** Beförderungen werden monatlich nach der Zweitabrechnung geprüft. Die Live-Seite zählt nur Umsatz der eigenen Abrechnung und beschreibt für rollierende Positionen zwölf Abrechnungen sowie einen Neustart des Wertungsumsatzes nach Beförderung. Sie nennt Kontrollen gegen verschobene Verträge und die Möglichkeit, erschlichene Beförderungen rückgängig zu machen. Für die Profiberateranforderung höherer Führungsstufen zählt laut FAQ die bestätigte Position, nicht ein zusätzliches Mindestvolumen des einzelnen Profis. [KW-IN-P035, „Wann und wie“, „Ehrliche Beförderung“, FAQ]

Karrierewechsel verändern auch die Struktur: Beim Wechsel zum Profiberater werden direkte Partner einschließlich Downline umgeordnet; bestimmte Positionen müssen für die Upline erneut bestätigt werden. Das Formular verlangt fünf **Arbeitstage**, die Seite fünf **Tage** Vorlauf. Bei der historischen Eigenumsatzwertung beschreibt die Seite sechs bzw. zwölf Monate innerhalb der letzten 60 Monate; die Formularbeschreibung muss dazu rollenbezogen abgeglichen werden. [KW-IN-P036; KW-IN-D06, S. 1–2]

| Richtung | Zuordnung laut Live-Seite |
| --- | --- |
| Teamaufbau → Consulting | M/SM → SC; D/SD → MC; P/SP → CP |
| Consulting → Teamaufbau | SC → SAN; MC → SM; CP → D |

Quelle: KW-IN-P036, beide Wechselrichtungen; KW-IN-D06, Zuordnungstabelle. Titelwechsel und neue wirtschaftliche Zuordnung sind keine Gleichstellung der bisherigen Aufgaben.

Umstrukturierungen verlangen Zustimmung der relevanten Ebenen, Vorlauf und Wirksamkeit zum Monatsersten; neue Zuordnung und Positionsbestätigung sind getrennte Vorgänge. Quereinsteiger müssen Umsatz und Qualifikation belegen. [KW-IN-P034/P040; KW-IN-D07/D08]

**Regelgrenze:** Die Vorlage 08.2026 enthält die rollierende Sechsmonatsbetrachtung, aber in den geprüften Klauseln keine gleichlautende ausdrückliche Nullstellung nach jeder Beförderung. Sie sagt zudem ab AN kein Überspringen; die Live-Seite erlaubt Sprünge im kumulierten Bereich T–AN und verlangt einzelne Schritte ab SAN. Die operative Interpretation kann dies teilweise vereinbaren, muss aber explizit versioniert werden. [KW-IN-D09, Anlage 3 § 2 Nr. 6–7, S. 32–33; KW-IN-P035, FAQ]

### Automatisches Offboarding und Austritt

Die Offboarding-Erläuterung nennt für T bis SAN eine Schwelle unter 500 Euro eigener Abschlussprovision, Warnungen nach sechs, sieben und acht Monaten sowie Kündigung im neunten Monat mit vier Wochen zum Monatsende. Führungskräfte ab SM können unter beschriebenen Bedingungen für 100 Euro innerhalb von 14 Tagen ein begrenztes Veto einsetzen; es schützt für drei Offboarding-Durchläufe, kein zweites Veto. [KW-IN-P042; KW-IN-D05, S. 1–3]

**Abgleichbedarf:** Hauptvertrag § 3 nennt nach Dauer der Zusammenarbeit ein, drei bzw. sechs Monate Kündigungsfrist. Die abweichende Vierwochenbeschreibung des Automatismus benötigt eine belastbare vertragliche Zuordnung oder Erklärung. Die Dokumente beweisen weder unwirksame tatsächliche Kündigungen noch die Anwendung einer bestimmten Fassung. [KW-IN-D09, Hauptvertrag § 3, S. 4–5]

Eigenkündigung und Führungskraftantrag sind getrennte Prozesse; KW entscheidet über den letzteren. Das Kündigungsformular fragt eine spätere externe Anbindung ab, gewährt damit aber noch keine automatische Kundenmitnahme. [KW-IN-P082; KW-IN-D12/D13, jeweils S. 1]

Für Kundenmitnahme sieht die aktuelle verlinkte VP-Vorlage unter anderem eine Erklärung binnen 14 Tagen nach Vertragsende, Kundenerklärungen binnen drei Monaten ab Zugang der Kündigung und eine Lösung für Betreuung/Stornohaftung mit Pool oder separater Vereinbarung vor. Ohne Erfüllung der Voraussetzungen gelten Herausgabe-/Sperr- und weitere Abwicklungsregeln. [KW-IN-D09, Anlage 1 § 8 Nr. 4–10, S. 17–19]

**Lehre:** Eintritt, Inaktivität, Kündigung und Bestandsübertragung als zusammenhängenden Prozess modellieren. Ein Umsatzminimum ist eine Aktivitätssteuerung, kein selbständiger Qualitätsnachweis. Ein Austrittsformular ersetzt weder Kundenwahl noch Haftungsübernahme.

## 4. Vergütung, Verteilung und Liquidität

### Abrechnung und Teilung

Die Abrechnungslogik beschreibt getrennten Eingang von Daten und Geld über mehrere Beteiligte. KW rechnet zweimal monatlich ab; die Unterlage bezeichnet Zeitangaben als grobe Richtlinie. Courtageanspruch, Buchung und Bankeingang sind daher unterschiedliche Zeitpunkte. [KW-IN-P076; KW-IN-D01, S. 1]

Teilungen zwischen zwei Beratern sind grundsätzlich in Zehnprozent-Schritten vorgesehen, betreffen Abschluss- und Bestandsprovision und wirken auf Umsatzwertung, Führungsvergütung und Stornohaftung. Bei Spezialisten gelten beschriebene Sonderverteilungen. Entscheidend ist die korrekte Vertragsnummer; eine Erfassung erst nach Abrechnung ist laut Anleitung nicht nachträglich korrigierbar. [KW-IN-P079, Grundlagen und Sparten; KW-IN-D04, Workflow]

Ratierliche Auszahlung bedeutet laut Seite zunächst vollständige Buchung in die Reserve und anschließende monatliche Freigabe über die Haftungsdauer, typischerweise 1/60. Auch Firmenumsatz zählt dann ratierlich. Sonderregeln für große Courtagen und bestimmte Geschäfte sind vom Standard zu trennen. [KW-IN-P083, Definition und Nachweise]

### Reserve und Risikobeitrag

**Dokumentierte Intranetregel:** Bei vorab vergüteter Abschlusscourtage mit Stornohaftung werden 10 % als Reserve beschrieben. Hinzu kommt ein als Vertrauensschadenshaftpflicht bezeichneter Risikobeitrag von 1 % des Umsatzes. Diese Bezeichnung ist nicht gleichbedeutend mit der beruflichen Vermögensschadenshaftpflicht des Partners. Die genaue Bemessungsbasis auf jeder Abrechnungsebene bleibt zu validieren. [KW-IN-P080, erste Abschnitte; KW-IN-P029]

| Cluster | Beschriebene Stornoquote | Besicherung der Resthaftung | Sockel |
| --- | --- | --- | --- |
| C1 | 0–5 % | 0 % | 20.000 Euro |
| C2 | 5–10 % | 5 % | 30.000 Euro |
| C3 | 10–20 % | 10 % | 40.000 Euro |
| C4 | über 20 % | 15 % | 50.000 Euro |

Quelle: KW-IN-P080, eingebettete Clustertabelle. Grenzwerte bei exakt 5 % und 10 % sind in dieser Schreibweise nicht eindeutig abgegrenzt.

Für aktive Partner beschreibt die Seite halbjährlich `Reserve − max(Besicherungssatz × Resthaftung, Sockel)`. Für inaktive Partner beschreibt sie `max(0, Reserve − Resthaftung)`. Bei der aktiven Formel fehlt die explizite Begrenzung auf null; dies ist eine Definitionsfrage, kein Beleg für eine tatsächlich negative Auszahlung. [KW-IN-P080, „Generelle Auszahlungen“/„Auszahlung bei inaktiven Partnern“]

**Vertragsabgleich:** Anlage 2 § 6 der VP-Vorlage beschreibt grundsätzlich Sicherung unverdienter Vorschüsse und weiterer ungesicherter Rückzahlungsansprüche, einen möglichen höheren Einbehalt sowie unter Voraussetzungen einen Zugriff von KW auf die Reserve. Die Live-Seite sagt pauschal, Stornos könnten nicht aus der Reserve bezahlt werden, und beschreibt für aktive Partner nur anteilige Resthaftungsbesicherung mit Sockel. Das kann unterschiedliche Anspruchs-/Ausnahmeebenen betreffen; die Rechtsgrundlage des aktiven Freigabemodells und dessen Verhältnis zum Vertrag fehlen im geprüften Material. [KW-IN-D09, S. 26–27; KW-IN-P080]

### Rechenprüfung der Stornoquote

**Quellenbefund:** Die Reserve-Seite verwendet in ihrem Beispiel positive Stornobeträge von insgesamt 10.000 Euro und Netto-Firmenumsatz von 34.000 Euro. Sie rechnet zusätzlich durch vier Abrechnungen. Die VPM-Seite enthält eine anders beschriftete Zeilenreihe, 34.000 Euro in der Ergebnisformel, einen Faktor −1 und das Ergebnis 6 %. [KW-IN-P080, „Beispielberechnung“; KW-IN-P007, „Berechnung der Stornoquote“]

**Eigene Nachrechnung, keine Unternehmenskennzahl:**

| Ausdruck | Rechenergebnis | Aussage |
| --- | --- | --- |
| 10.000 / (34.000 + 10.000) | 22,7273 % | Volumenverhältnis im Beispiel ohne weitere Division |
| Voriger Ausdruck / 4 | 5,6818 % | Entspricht dem Ergebnis der Reserve-Seite |
| −10.000 / (34.000 − 10.000) / 4 | −10,4167 % | Wörtliche VPM-Ergebnisformel ergibt nicht 6 % |

Die in VPM als Firmenumsatz bezeichneten vier Werte summieren sich zudem auf 44.000 Euro, nicht 34.000 Euro. Das Beispiel ist intern widersprüchlich. Die zusätzliche Division der Reserve-Seite ist rechnerisch nachvollziehbar, aber keine übliche reine Volumenquote. Für eine betriebliche Beurteilung fehlen Vorzeichenkonvention, implementierte Formel, Nenner, leere Perioden, Kohorten und Kalibrierung der Cluster. **Kein Softwarefehler und keine tatsächliche KW-Stornoquote werden behauptet.** Reproduzierbare Nachrechnung: [CALCULATIONS.md](CALCULATIONS.md).

### Boni und bedingte Förderung

KW+ belohnt interne Partnerempfehlungen laufend und endet beim Ausscheiden des Empfehlungsgebers. Das Formular präzisiert, dass der Bonus aus der direkten Differenzprovision des aufnehmenden Partners stammt. Er ist kein beförderungsrelevanter Firmenumsatz. [KW-IN-P037; KW-IN-D16, S. 1–2]

Der Standortleiterbonus von 4 % des zugeordneten Firmenumsatzes wird dagegen laut Seite zusätzlich von KW getragen. Anerkennung verlangt tatsächliche gewerbliche Räumlichkeiten, geeignete Nutzung, Nachweise und Bestätigung; bloße Geschäftsadressen oder flexible Gemeinschaftsplätze genügen nicht. Änderungen wirken zum Monatsersten, nicht rückwirkend. [KW-IN-P039, Anerkennung/Bonus; KW-IN-D14]

Davon getrennt ist die Förderung: bis zu zwölf Monate, maximal 1.000 Euro monatlich und höchstens 50 % tatsächlicher Standortkosten, unter weiteren Positions-, Partnerzahl-, Umsatz-, Stadt- und Freigabevoraussetzungen. Das Formular enthält wesentliche Rückzahlungsbedingungen bei Kündigung innerhalb von 36 Monaten nach Zahlung sowie bei Unterschreiten der beschriebenen Umsatzschwelle im Kontrollzeitraum. Diese Bedingungen fehlen in dieser Ausführlichkeit in der Webseitenkurzbeschreibung. [KW-IN-P039, „Standortförderung“; KW-IN-D15, S. 1–2]

**Interpretation:** Zuschüsse können spätere Rückzahlungsrisiken begründen. Für einen Standortfall müssen Mietbindung, Eigenkosten, Bonusverlust bei Partnerwechsel und mögliche Rückforderung gemeinsam gerechnet werden. „Förderung“ ist nicht automatisch endgültig verdienter Ertrag.

## 5. Beratung, Spezialisten und Kundenzuordnung

Fachseiten für Altersvorsorge, Biometrie, Kranken-, Sach- und Gewerbeversicherung stellen Leitfäden und weitere Unterlagen bereit. Wiederkehrende Disclaimer verlangen eigene Qualitäts- und Fallprüfung. Die sichtbare Sammlung ist kein unabhängiger Nachweis der besten Tarife oder einer einheitlichen Beratungsqualität. Die Checkliste für sauberes Geschäft verbindet Mandat/Vollmacht, Identifizierung, individuelle Dokumentation und korrekte Kunden-/Vertragsablage. [KW-IN-P045/P046/P049/P051–P053; KW-IN-D17, jeweilige Abschnitte]

BU-Leistungsfallunterstützung und weitere Fachkooperationen beschreiben Übergaben an Spezialisten. Bei Nettolohnoptimierung bestehen zusätzliche bAV- und Vergütungsverknüpfungen; Einsparungs- und Risikoversprechen sind nicht validiert. **Gestaltungshypothese:** Vergütung, Kompetenz und Kundeninteresse pro Fall prüfen, statt eine Empfehlung allein aus einem Kooperationsangebot abzuleiten. [KW-IN-P057–P061/P066]

Der Akquiseschutz beschreibt unter anderem sechsmonatige Schutzfristen bei vollständiger Anlage/Einwilligung und einen fortbestehenden Bestandsschutz bei aktiven Verträgen. Das sind interne Zuordnungsregeln; sie ersetzen weder die Kundenentscheidung noch die Austrittsbedingungen. Interne Umschlüsselung und externe Mitnahme sind verschiedene Prozesse. [KW-IN-P065, Kunden-/Partnerakquise; KW-IN-P070; KW-IN-D09, Anlage 1 § 8]

### Depotangebote

Die VV-Depot-Seite beschreibt einen Tippgeberweg, bei dem der Kunde die Auswahl trifft, mit gesonderter Vermögensverwaltung und laufender Vertriebsvergütung. Sie nennt unter anderem 0,93 % Vermögensverwaltungsvergütung einschließlich 0,5 % laufender Vertriebsvergütung nach der dortigen Steuerdarstellung; weitere Fonds- und Depotkosten kommen hinzu. Das ist eine interne Kostenbeschreibung, keine validierte Gesamtkostenquote. Eine fehlende direkte Synchronisierung macht die korrekte Zuordnung über den beschriebenen Link wichtig. [KW-IN-P054, Rolle/Kosten/Workflow]

Die §-34f-Seite weist mit Stand 16.07.2026 auf gestopptes FONDSNET-Neugeschäft und eine Umstellung zu Netfonds hin. Im selben Kontext stehen „zwei bis vier Wochen“ und ein vorläufiger Termin 01.01.2027; weiter unten bleiben Investifant-Anleitungen vorhanden. Der tatsächlich nutzbare Neugeschäftsweg am Abrufdatum ist deshalb aus der Seite nicht eindeutig bestimmbar. [KW-IN-P055, Umstellungshinweis und aufgeklappter Workflow]

Die Seite beschreibt außerdem 0,83 % jährliches Serviceentgelt mit quartalsweiser Abrechnung und zusätzliche Prüf-/Berufskosten. Die VL-Seite unterscheidet ausdrücklich Tippgabe von konkreter Fondsberatung. **Offen:** aktuelle Plattformfreigabe, Gesamtpreis je Fall, tatsächliche Erlaubnisse und praktische Durchsetzung der Rollengrenzen. [KW-IN-P055, Serviceentgelt/Kosten; KW-IN-P056, Tippgeberrolle]

## 6. Compliance: Hilfen vorhanden, aktuelle Rechtsfreigabe nicht belegt

### Konkrete Abweichungen

| Befund | Externer Abgleich / Konsequenz |
| --- | --- |
| Kleinunternehmerseite nennt 22.000/50.000 Euro. [P027] | Aktueller § 19 Abs. 1 UStG nennt 25.000/100.000 Euro unter seinen Voraussetzungen. Die Seite ist hinsichtlich dieser Zahlen überholt; die Einordnung verschiedener Vergütungen und der Gesamtumsatz müssen separat geprüft werden. [E01] |
| Datenschutztexte verwenden unter anderem eine Formulierung „mehr als 20“. [P019] | § 38 Abs. 1 BDSG sagt mindestens 20 ständig mit automatisierter Verarbeitung beschäftigte Personen und enthält zusätzliche Auslöser. Keine pauschale Freistellung kleiner Organisationen ableiten. [E02] |
| VP-Vorlage nennt in Anlage 5 Nr. 7 mehr als **95 %** Stimmrechte/Kapital für die dortige Ermittlung. Text und Seitenbild stimmen überein. [D09, S. 37] | § 3 Abs. 2 GwG nennt für die erfassten Gesellschaften mehr als **25 %** sowie alternative Kontrolltatbestände. Die Vorlagenangabe ist für diese Bestimmung fachlich fehlerhaft; tatsächliche Identifizierungsprozesse können davon abweichen. [E03] |

Dies sind gezielte Primärquellenabgleiche, kein vollständiges Rechtsaudit.

### Muster, Zuständigkeiten und tatsächliche Umsetzung

Die Standard-Risikoanalyse enthält konkrete Annahmen wie Einzelunternehmen, regionale Privatkunden und geringe Risiken. Außerdem stehen alternative Personalannahmen neben späteren Aussagen zu fehlenden Mitarbeitern; beim Geldwäschebeauftragten passen Nichtbestellung und spätere Meldeverweise nicht ohne weitere Erläuterung zusammen. Ein solches Muster muss vor Verwendung auf Rechtsform, Personal, Kunden und Produkte angepasst werden. Ein Blankomuster beweist keine erfolgte betriebliche Risikoanalyse. [KW-IN-D19, Kapitel 1–4 und 5]

Datenschutzfallseite und Kündigungsleitfaden unterscheiden Eingangsbestätigung, Abgabe der Betreuung, Einschränkung weiterer Verarbeitung und spätere Löschung. Die interne 72-Stunden-Angabe darf nicht pauschal mit jeder gesetzlichen Melde-/Antwortfrist gleichgesetzt werden. Die im Leitfaden aufgezählten pauschalen Aufbewahrungsfristen wurden nicht als allgemein gültig übernommen. Rechtsgrundlage, Dokumentart und Zweck bleiben einzeln zu prüfen. [KW-IN-P020/P022; KW-IN-D18, §§ 1–4]

Der verlinkte Datensperrbeleg war über den Dokumentzugang nicht lesbar; ein Geldwäsche-Arbeitshilfenlink führte auf eine 404-Seite. Das begrenzt die Nachvollziehbarkeit einzelner Prozessschritte, obwohl das Intranet insgesamt zugänglich ist. [KW-IN-D21; KW-IN-P084]

## 7. Was für den eigenen Geschäftsplan verwendbar ist

Die folgenden Punkte sind **eigene Gestaltungshypothesen**, keine bereits beschlossenen Modellmerkmale:

| Prinzip | Herleitung | Benötigte Prüfung |
| --- | --- | --- |
| Ein verbindliches Regelregister | Abweichungen zwischen Live-Seite, Formular und Vertrag | Version, Inkrafttreten, zuständige Stelle, Ausnahmen und Vertragsgrundlage pro Regel |
| Ein vollständiger Zahlungswasserfall | Teilung, Führung, Bonus, Gebühren, Reserve und spätere Rückforderung | Identische synthetische Fälle für Berater, Führung, Organisation und Kunde |
| Beratungsqualität getrennt von Umsatz messen | Karriere-/Offboardingsteuerung und fachliche Eigenverantwortung | Aktenqualität, Kundenverständnis, Beschwerden und Bestandsentwicklung |
| Rechnerannahmen offenlegen | Rentenlücken- und Immobilienscorebeschreibung | Individuelle Eingaben, Sensitivität und fachliche Freigabe vor Einsatz |
| Spezialistenübergaben klar vereinbaren | Teilung, Kooperationsdienste und Haftung | Wer berät, dokumentiert, betreut und trägt welche Kosten? |
| Exit und Sicherheiten schon vor Eintritt erklären | Bürgschaften, Kündigung und bedingte Kundenmitnahme | Verständlicher Musterfall einschließlich Fristen und Liquidität |
| Technik am vollständigen Fall messen | Mehrere Plattformen und manuelle Schnittstellen | Aufwand, Fehler und Gesamtkosten vor und nach Automatisierung |

**Noch nicht belegt:** Profitabilität der Organisation oder einzelner Rollen, tatsächliche durchschnittliche Ausschüttung, Kundenrenditen, Beraterbindung, gelebte Haftungsfreigabe und aktuelle Funktionsfähigkeit aller beworbenen Integrationen. Die neue Live-Evidenz ersetzt frühere pauschale Zugriffsblocker, aber nicht diese Ergebnis- und Betriebsnachweise. Priorisierte nächste Prüfungen stehen in [REVIEW_STATUS.md](REVIEW_STATUS.md).
