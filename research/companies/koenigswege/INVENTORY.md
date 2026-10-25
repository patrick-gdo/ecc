# Dateiindex und Fortsetzungsregeln

**Auftragsänderung 25.10.2026 (DEC-005):** University ist nun eingeschlossen. Die folgenden älteren Zählstände beruhen auf dem damaligen Ausschluss und werden nicht rückwirkend erweitert. Neue [University-Teilprüfung](online-university/README.md) und [Prüfstatus](online-university/REVIEW_STATUS.md) separat lesen.

Die Datei [document_inventory.csv](document_inventory.csv) enthält 704 sichtbare Dateien außerhalb der festgehaltenen University-Ausschlüsse. Stand: Inventarisierung vom 25.10.2026. Keine neue Vollinventarisierung im zweiten Durchlauf; neu aufgerufene Dateien wurden anhand des vorhandenen Inventars gewählt.

Die Datei enthält bewusst keine personenbezogenen Dateinamen, Originalinhalte oder Kontaktlisten. `drive_file_id` identifiziert die Datei; der Detailaufruf lautet `https://drive.google.com/file/d/<drive_file_id>/view`. Verfügbarkeit und Freigabe können sich ändern. Titel und Fundstellen registrierter Quellen stehen in [sources.json](sources.json).

## Statuswerte

- `not_reviewed`: weder für diese Analyse heruntergeladen noch inhaltlich geprüft.
- `extracted_only`: technisch ausgelesen, noch keine dokumentierte Abschnittsprüfung. Ein Textauszug kann Layout, Bilder, Kommentare und weitere Inhalte auslassen.
- `downloaded_only`: heruntergeladen, noch keine dokumentierte Inhaltsprüfung.
- `scoped_review`: Prüfumfang im Quellenregister dokumentiert; ausdrücklich nicht automatisch vollständig geprüft. Auch eine begrenzte Begriffssuche ist als solche kenntlich.
- `no_text_extracted`: technische Leselücke; kein Schluss aus dem Dateititel auf den Inhalt.

## Zählung nach zweitem Durchlauf

- `extracted_only`: 25 Dateien.
- `no_text_extracted`: 1 Dateien.
- `not_reviewed`: 654 Dateien.
- `scoped_review`: 24 Dateien.

Die Quelle mit `no_text_extracted` ist ebenfalls im Quellenregister dokumentiert; deshalb ist die Anzahl der Registereinträge um eins höher als die Anzahl `scoped_review`. Insgesamt 50 Dateien heruntergeladen; davon 46 Office-/PDF-/Textdokumente technisch verarbeitet (eines ohne auslesbaren Text) und vier Grafiken visuell geprüft. Diese Zahlen werden nicht als Zahl vollständig gelesener Unterlagen verwendet.

## Für die nächste KI

1. README.md, AGENTS.md, REVIEW_STATUS.md und die aktuellen Befunde lesen.
2. Vor neuen Drive-Aufrufen [exclusions.json](exclusions.json) beachten. Der University-Ausschluss ist aufgehoben; historische Einträge sind keine aktuelle Sperrliste. Zugehörige Inhalte dürfen im neuen Auftrag geprüft werden, mit denselben Datenschutz- und Originalschutzgrenzen.
3. Nach Themenbedarf aus dem Index wählen und Inhalt tatsächlich abrufen. Die bloße Präsenz im Inventar ist kein Beleg für eine Aussage.
4. Quellen-ID, Hash, Datum und konkreten Prüfumfang ergänzen. Vertrauliche Originale und personenbezogene Daten außerhalb des Repositorys halten.
5. Status, Schlussfolgerungen und Projektübergabe gemeinsam aktualisieren. Änderungen versioniert auf GitHub speichern.

## Dritter Durchlauf – operative Vertiefung

14 weitere Dokumente heruntergeladen und mit explizitem Prüfumfang registriert; zwei bildbasierte PDFs zusätzlich gerendert und visuell gelesen. Kumuliert 64 heruntergeladene Dateien, 60 technisch verarbeitete Dokumente (eins ohne auslesbaren Text) und vier separat heruntergeladene Grafiken. Status im Index: `extracted_only` 25, `no_text_extracted` 1, `not_reviewed` 640, `scoped_review` 38. 39 Registereinträge einschließlich der zuvor dokumentierten Leselücke. Vorherige Zählungen oben sind historische Zwischenstände.

Die zusätzlich eingeordnete Vergleichsarbeitsmappe KW-040 war bereits heruntergeladen. Aktuell: 40 Registereinträge, 39 `scoped_review`, 24 `extracted_only`, eine `no_text_extracted`, 640 `not_reviewed`; weiterhin 64 heruntergeladene Dateien. Ihre zweite Ablage FG-006 zählt nicht als unabhängiger Beleg.

## Partnervertiefung: aktueller Stand

Eine weitere Vorlage als KW-041 textlich gelesen: 65 heruntergeladene Dateien, 41 Registereinträge; 40 `scoped_review`, 24 `extracted_only`, eine `no_text_extracted`, 639 `not_reviewed`. Historische Zählungen oben bleiben als Zwischenstände erhalten.

## Separate Ergänzung: Live-Intranet am 25.10.2026

Der authentifizierte KW-Durchlauf ist unter [intranet/](intranet/README.md) separat erfasst: 85 Seitenpositionen, davon 74 gezielte Inhaltsreviews; 21 ausgewählte Dokumentverweise, davon 19 mit benanntem inhaltlichem Prüfumfang und zwei Abruffehler; fünf externe Primärquellen. [Seitenindex](intranet/page_inventory.csv) und [Quellenregister](intranet/sources.json) enthalten eigene Zusammenfassungen und keine Originale.

Die früheren 704 Drive-Dateien wurden nicht erneut komplett inventarisiert. Live-Verknüpfungen können dieselbe Quelle oder neue Fassungen mit anderer Drive-ID betreffen. Deshalb keine Addition zu historischen Download-/Reviewzahlen und keine pauschale Umstufung des alten Dateiindex.
