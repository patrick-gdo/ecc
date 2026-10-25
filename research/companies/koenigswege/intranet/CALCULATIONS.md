# Nachrechnung der dokumentierten Stornobeispiele

Stand: 25.10.2026. Quellen: KW-IN-P007 und KW-IN-P080, jeweils Abschnitt zur Berechnung der Stornoquote. Nur Nachrechnung veröffentlichter Beispiele, keine personenbezogenen Abrechnungen oder tatsächlichen Unternehmensquoten.

## Reserve-Seite

Vier beispielhafte Bruttoumsätze: 10.000 + 8.000 + 9.000 + 17.000 = 44.000 Euro.
Stornobeträge als positive Beträge: 0 + 2.000 + 5.000 + 3.000 = 10.000 Euro.
Daraus Netto-Firmenumsatz: 34.000 Euro.

- Volumenverhältnis: 10.000 / 44.000 = 22,7272727 %.
- Zusätzlich durch vier Abrechnungen geteilt: 5,6818182 %.
- Dies erklärt die 5,68 % der Reserve-Seite; die Division ist Bestandteil ihrer dokumentierten Kennzahl, nicht automatisch ein zulässiger Vergleich mit anderen Stornoquoten.

## VPM-Seite

Die vier als Firmenumsatz beschrifteten Werte summieren sich auf 44.000 Euro. Die Ergebnisformel setzt dagegen 34.000 Euro ein und multipliziert Storno mit −1.

Wörtliche Rechnung: (10.000 × −1 / (34.000 + 10.000 × −1)) / 4 = −10,4166667 %, nicht die angegebenen 6 %.

Es wäre unzulässig, die Formel stillschweigend zu reparieren und daraus die tatsächliche Implementierung abzuleiten.

## Reservefreigabe: begrenzte Rechenprobe

Das dokumentierte Beispiel aktiver Partner: 133.000 − max(55.600, 40.000) = 77.400 Euro. Der Besicherungsbetrag ist in der Quelle gerundet; die Rechnung übernimmt diese Rundung.

Zusätzlicher **synthetischer Grenzfall** zur Definitionsprüfung, keine KW-Abrechnung:
Reserve 15.000 Euro, prozentuale Besicherung 0 Euro, Sockel 20.000 Euro. Die wörtliche aktive Formel ergibt −5.000 Euro. Ob das System auf null begrenzt oder ein anderer Prozess greift, ist offen. Die inaktive Formel enthält diese Nullbegrenzung ausdrücklich.

## Reproduzierbare Rechnung

```python
from decimal import Decimal as D

gross = sum(map(D, ["10000", "8000", "9000", "17000"]))
cancellations = sum(map(D, ["0", "2000", "5000", "3000"]))
net = gross - cancellations
periods = D("4")
volume_ratio = cancellations / (net + cancellations)
reserve_page_ratio = volume_ratio / periods
vpm_literal_ratio = -cancellations / (net - cancellations) / periods
release_example = D("133000") - max(D("55600"), D("40000"))
synthetic_edge = D("15000") - max(D("0"), D("20000"))

assert gross == D("44000") and net == D("34000")
assert round(volume_ratio * 100, 4) == D("22.7273")
assert round(reserve_page_ratio * 100, 4) == D("5.6818")
assert round(vpm_literal_ratio * 100, 4) == D("-10.4167")
assert release_example == D("77400")
assert synthetic_edge == D("-5000")
```

Diese Rechenprobe prüft Arithmetik und Dokumentkonsistenz. Sie prüft weder Software noch Vertragsgeltung, Definition der Resthaftung, tatsächliche Auszahlung oder Angemessenheit der Cluster.
