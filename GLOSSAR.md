# Glossar

> Wird automatisch gepflegt — neue Begriffe werden ergänzt wenn sie im Unterricht fallen oder ein Azubi nach einer Erklärung fragt.

## 7 Module & Bibliotheken

**Bibliothek** — Eine Sammlung von fertigem Code, den andere Entwickler geschrieben haben und den du in deinem eigenen Programm nutzen kannst. In Python wird eine Bibliothek mit `import` eingebunden.

**import** — Python-Schlüsselwort das eine Bibliothek oder ein Modul in das aktuelle Programm lädt, damit dessen Funktionen genutzt werden können.

## 2 Hardware & GPIO — Grundlagen

**Raspberry Pi** — Ein kleiner Einplatinen-Computer, der sich besonders gut für Hardware-nahe Projekte eignet — z.B. Sensoren auslesen oder LEDs steuern.

**GPIO** — General Purpose Input/Output — die programmierbaren Pins am Raspberry Pi, über die externe Hardware (LEDs, Taster, Sensoren) angeschlossen und gesteuert werden kann.

**Pull-down-Widerstand** — Ein Widerstand der einen GPIO-Eingangspin auf einen definierten Zustand (GND = 0V = LOW) zieht, wenn kein Signal anliegt. Verhindert sogenannte "Floating Pins".

**Floating Pin** — Ein nicht angeschlossener GPIO-Eingangspin ohne definierten Pegel. Ohne Pull-up oder Pull-down kann er durch Störsignale zufällig HIGH oder LOW sein — das führt zu unzuverlässigem Programmverhalten.

## 6 Fehlerbehandlung

**try / except / finally** — Ein Python-Konstrukt zur Fehlerbehandlung. Code im `try`-Block wird ausgeführt, `except` fängt bestimmte Fehler ab, `finally` läuft immer — auch bei Fehler oder Abbruch. Wichtig z.B. für GPIO-Cleanup.

**KeyboardInterrupt** — Eine Exception die Python auslöst wenn der Nutzer das Programm mit Strg+C abbricht. Kann gezielt mit `except KeyboardInterrupt` abgefangen werden.

**bare except** — Ein `except`-Block ohne Angabe einer konkreten Exception (`except: pass`). Fängt alle Fehler stillschweigend ab — auch unerwartete — und erschwert die Fehlersuche. Gilt als schlechte Praxis.

## 1 Kontrollstrukturen

**while-Schleife** — Eine Schleife die so lange wiederholt ausgeführt wird, wie eine Bedingung wahr ist. `while True` läuft endlos weiter bis das Programm manuell gestoppt wird.
