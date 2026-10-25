# Arbeitsanweisungen für KI-Chats

## Einstieg

Lies zuerst README.md, docs/PROJECT.md und docs/DECISIONS.md. Prüfe anschließend den Git-Status und die für die Aufgabe relevanten Analysen und Quellen. Nutze den bestehenden Checkout; erstelle keinen zusätzlichen Worktree ohne ausdrücklichen Auftrag.

## Wissensqualität

- Schreibe auf Deutsch. Halte Fakten, Unternehmensselbstdarstellung, externe Kritik, Interpretation, Hypothesen und Entscheidungen ausdrücklich auseinander.
- Erfinde keine Zahlen, Quellen, Unternehmenspraktiken oder Erfolgsversprechen. Fehlende Daten bleiben offen. Keine unbelegten Vorwürfe gegen Unternehmen oder Personen.
- Jede wesentliche empirische oder rechtliche Aussage erhält Quellen-ID und Fundstelle. Erfasse URL, Herausgeber, Veröffentlichungsstand, Abrufdatum, Geltungsbereich und Einschränkungen im Quellenregister.
- Lies Quellen tatsächlich. Eine vorgeschlagene URL ist keine geprüfte Quelle. Prüfe Aktualität und unterscheide Rechtslage, angekündigte Änderungen und eigene Interpretation.
- Nutze Primärquellen bevorzugt; prüfe Eigeninteressen und gleiche strittige Aussagen mit unabhängigen Quellen ab.
- Vergleiche Kennzahlen nur bei gleichem Zeitraum, Markt, Nenner und Geschäftsmodell. Umsatz ist weder Gewinn noch verfügbarer Cashflow.
- Speichere keine Kundendaten, Zugangsdaten oder vertraulichen Verträge im Repository. Verwende anonymisierte oder synthetische Beispiele.

## Ablage und Übergabe

Unternehmensanalysen liegen unter research/companies/, Quellen unter research/SOURCES.md, Entscheidungen unter docs/DECISIONS.md. Nutze templates/COMPANY_ANALYSIS.md für neue Analysen.

Aktualisiere nach substanzieller Arbeit docs/PROJECT.md mit erledigten Punkten, offenen Fragen und nächstem Arbeitsschritt. Dokumentiere bei Entscheidungen Datum, Begründung, Evidenz und Bedingungen für eine Neubewertung. Bewahre abweichende Evidenz.

Prüfe interne Links und Git-Diff vor einem Commit. Bewahre fremde Änderungen. Publiziere nur innerhalb des erteilten Auftrags und berichte klar, ob Änderungen lokal, committed oder zu GitHub gepusht sind.

## Königswege: Fortsetzen der Quellenarbeit

Vor neuen Dateiabrufen research/companies/koenigswege/INVENTORY.md und exclusions.json lesen. Die ausgeschlossenen University-Ordner einschließlich ihrer Nachkommen nicht öffnen; eindeutig zugehörige Dateien und University-Passagen gemischter Unterlagen auslassen. document_inventory.csv enthält bewusst nur datensparsame Metadaten. `scoped_review` bedeutet ausschließlich den im Quellenregister beschriebenen Prüfumfang, niemals automatisch eine vollständige Inhaltsprüfung. Vorschlag, Beschlussbehauptung, dokumentierte Regel und geprüfter Betrieb bleiben getrennte Evidenzarten.

## Direkte Konkurrenten: Königswege und FG

Der Nutzer ordnet Königswege und Finanzgenies (FG) als direkte Konkurrenten ein. FG nicht mit Fonds Finanz verwechseln. Vor vergleichender Arbeit research/comparisons/koenigswege-vs-finanzgenies.md und research/claims.csv lesen. Ein Drive-Ablageort belegt keine Urheberschaft: FG-006 und KW-040 sind dieselbe Evidenzfamilie, FG-007 hat überwiegenden Königswege-Bezug. Screenshots, Vertragsvorlagen, Gesprächsbehauptungen und verifizierte aktuelle Betriebsregeln auseinanderhalten.

## KWIF, Website und Live-Intranets

KWIF-Drivequellen liegen unter research/companies/koenigswege-immobilien-finanzierung/. Öffentliche Websitequellen liegen unter research/companies/koenigswege/website/; deren page_inventory.csv und sources.json unterscheiden strukturellen Index von gezielter Textprüfung. Nur Metadaten und eigene Zusammenfassungen speichern, keine Rohseiten, personenbezogenen Objekt-/Bonitätsakten oder Originalverträge. Beide Live-Intranets verlangten beim letzten Zugriff Google-Anmeldung; INTRANET_ACCESS.md lesen und keine vollständige Intranetprüfung behaupten, solange kein tatsächlicher Inhaltszugriff vorliegt. Online University bleibt ausgeschlossen.
