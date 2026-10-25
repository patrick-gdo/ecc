# Eng begrenzte Rechenprüfung des P1-Skripts

Quelle: KW-OU-D010, Abschnitte „Finanzielle Unabhängigkeit“ und „FQ“. Stand: 25.10.2026. Dies sind eigene Nachrechnungen und konstruierte Zeitannahmen, keine aktuellen Marktdaten und keine Bewertung eines echten Investments.

| Aussage / Rechnung | Eigene Prüfung | Grenze |
| --- | --- | --- |
| 3.000 Euro heutige Kaufkraft bei 2 % Inflation nach 40 Jahren | `3000 × 1,02^40 = 6.624,12` Euro | Rechnerisch passend; 2 % sind eine angenommene konstante Inflation. |
| Realwert von 100.000 Euro unveränderter Nominalschuld nach zehn Jahren bei 2 % Inflation | `100000 / 1,02^10 = 82.034,83` Euro | Realentwertung ist keine monatlich zufließende Liquidität und tilgt keine Nominalschuld. |
| 46.000 Euro Endsaldo aus 10.000 Euro anfänglichem Einsatz nach zehn Jahren | `(46000/10000)^(1/10) − 1 = 16,4866 %` | Diese Wachstumsrate behandelt den Endsaldo wie einen einzigen Zahlungsrückfluss und berücksichtigt die Zeitpunkte weiterer Einzahlungen nicht. |

Das Skript nennt zunächst 10.500 Euro Kaufnebenkosten, später gerundet 10.000 Euro Einsatz, monatlich 50 Euro negativen Cashflow und nach zehn Jahren gerundet 165.000 Euro Immobilienwert, 133.000 Euro Restschuld sowie 20.000 Euro Sparplan. Vor den kumulierten 6.000 Euro Cashflow ergibt das 52.000 Euro Endvermögen; nach Abzug 46.000 Euro.

**Eigene Sensitivität:** Unter der ausdrücklich konstruierten Vereinfachung von 600 Euro Zusatzzahlung jeweils zum Jahresende für zehn Jahre und 52.000 Euro Verwertungserlös am Ende gilt:

`0 = −Anfangseinsatz − Summe[600/(1+r)^t, t=1…10] + 52000/(1+r)^10`

- Anfangseinsatz 10.000 Euro: interner jährlicher Zinsfuß **14,8440 %**.
- Anfangseinsatz 10.500 Euro: interner jährlicher Zinsfuß **14,3648 %**.

Ermittelt durch Intervallhalbierung mit 100 Iterationen auf `r ∈ [0,1]`. Die gewählte jährliche Zeitstruktur ist keine Rekonstruktion tatsächlicher monatlicher Zahlungen. Verkaufs-/Finanzierungs-/Steuerkosten, Mietausfall, Anschlusszins, Wertschwankungen und sonstige Zusatzkosten sind nicht vollständig modelliert.

**Bewertung:** Das Skript ist als illustrative Verkaufs-/Recruitingrechnung zu behandeln. Eine belastbare Renditeaussage benötigt alle datierten Zahlungsströme und Risiken. Für unseren Vertrieb sollten Realwert, Nominalschuld, Cashflow, Endvermögen und Rendite getrennt ausgewiesen werden. Die eigene Sensitivität bestätigt keine tatsächliche Rendite und ist keine Anlageempfehlung.
