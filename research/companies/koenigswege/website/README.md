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

- `targeted_text_review`: 17 Seiten.
- `structural_index_only`: 214 Seiten.
- `opening_section_review`: 16 Seiten.
- `catalog_excerpt_review`: 65 Seiten.

`structural_index_only` bedeutet nur automatischen Abruf und Strukturindex. Bei Podcastseiten wurden sichtbare Begleittexte/Ankündigungen katalogisiert, keine Episoden angehört. Bei Partnerartikeln Eingangsabschnitte und Themen; keine vollständige Prüfung aller historischen Rechts-/Steuerangaben. Die im Bericht verwendeten Kernaussagen stammen aus gezielt gelesenen Seiten mit explizitem Prüfumfang.

## Grenzen der „gesamten Website“

Erfasst ist die über Sitemap und interne Links entdeckte statische HTML-Oberfläche derselben Domain. Keine versteckten oder nur durch JavaScript erzeugten Inhalte, keine privaten Dashboards, keine externen Plattformen, keine Anmeldungen, Kontakt-/Spendenaktionen oder Formularübermittlungen. Partnerprofile und Standortdaten werden als Seiten inventarisiert, nicht als persönliche Datenbank kopiert. Online University bleibt ausgeschlossen.

Die beiden angefragten Intranets verlangen Google-Anmeldung; Zugriff und nötiger nächster Schritt sind in [INTRANET_ACCESS.md](../INTRANET_ACCESS.md) dokumentiert. Websiteweite Erfassung ist weder ein vollständiger Intranetreview noch eine unabhängige Unternehmens-/Rechtsprüfung.
