# Öffentliche Königswege-Website

Stand: 25.10.2026. Websiteweite technische Erfassung über Sitemap und interne HTML-Links; relevante Kunden-/Partner-/Immobilien- und Rechtsdarstellungen gezielt geprüft. Keine vollständige manuelle Prüfung sämtlicher Fachbehauptungen, Videos oder Audioinhalte.

- [Analyse und Lehren](ANALYSIS.md)
- [Quellen und konkrete Prüfumfänge](SOURCES.md) / [sources.json](sources.json)
- [Seitenindex](page_inventory.csv), [alle URL-Aufrufe](request_inventory.csv), [Abdeckung](coverage.json)

## Tatsächlich erreichte Abdeckung

- 309 Sitemap-Einträge, alle als URL aufgerufen (Erfolg bzw. Fehler dokumentiert).
- 449 URL-Aufrufe im Bestand, davon 447 erfolgreiche HTML-Antworten.
- 312 kanonische Seiten nach Gruppierung von 135 Varianten.
- Keine verbleibenden URLs in der Suchwarteschlange.
- Ein Standortpfad liefert 404; eine technische Builder-Komponente lieferte nach anfänglichem Timeout und erneutem Abruf 503. Die URL-Liste nennt beide.

## Wie viel davon inhaltlich geprüft ist

- `targeted_text_review`: 16 Seiten.
- `structural_index_only`: 203 Seiten.
- `article_body_review`: 16 Seiten.
- `profile_text_review`: 8 Seiten.
- `page_text_review`: 4 Seiten.
- `catalog_excerpt_review`: 65 Seiten.

Vertiefung: [Partnerbereich vollständig schriftlich ausgewertet](PARTNER_ANALYSIS.md), [Prüfliste](partner_review.csv). Alle 16 Partnerartikel außerhalb der University-Ausschlüsse, acht direkt verlinkte Profile und vier Einstiegs-/Übersichtsseiten textlich gelesen; drei Abbildungen visuell geprüft. Audio, Video und externe Lerninhalte nicht gelesen. Strukturindex bedeutet keine Inhaltsprüfung.

## Grenzen der „gesamten Website“

Erfasst ist die über Sitemap und interne Links entdeckte statische HTML-Oberfläche derselben Domain. Keine versteckten oder nur durch JavaScript erzeugten Inhalte, keine privaten Dashboards, keine externen Plattformen, keine Anmeldungen, Kontakt-/Spendenaktionen oder Formularübermittlungen. Partnerprofile und Standortdaten werden als Seiten inventarisiert, nicht als persönliche Datenbank kopiert. Online University bleibt ausgeschlossen.

Die beiden angefragten Intranets verlangen Google-Anmeldung; Zugriff und nötiger nächster Schritt sind in [INTRANET_ACCESS.md](../INTRANET_ACCESS.md) dokumentiert. Websiteweite Erfassung ist weder ein vollständiger Intranetreview noch eine unabhängige Unternehmens-/Rechtsprüfung.
