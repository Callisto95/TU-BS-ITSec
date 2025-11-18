# Report

## 1. Security Goals

### a

#### Vertraulichkeit

Definition: Vertraulichkeit bedeutet, dass nur autorisierte Personen Zugriff auf Informationen oder Gegenstände haben.
$\rightarrow$ Mallory konnte möglicherweise persönliche Dokumente, digitale Geräte oder private Informationen einsehen.

#### Integrität

Definition: Integrität bedeutet, dass Daten oder Gegenstände nicht unbemerkt verändert oder manipuliert werden dürfen.
$\rightarrow$ Mallory könnte Dinge beschädigt, verändert oder manipuliert haben, z. B. Daten auf einem Computer.

#### Verfügbarkeit

Definition: Verfügbarkeit bedeutet, dass Ressourcen für autorisierte Personen zugänglich bleiben.
$\rightarrow$ Falls Mallory etwas gestohlen oder zerstört hat, sind diese Ressourcen für Alice nicht mehr verfügbar.

#### Authentizität

Definition: Authentizität stellt sicher, dass jemand tatsächlich derjenige ist, der er vorgibt zu sein.
$\rightarrow$ Mallory hat sich „Zugang verschafft“, ohne berechtigt zu sein – ein indirekter Verstoß.

### b

#### Physische Sicherheitsmechanismen

Definition: Maßnahmen, die den physischen Zugriff verhindern oder erschweren.
Beispiele:

stabileres Schloss / Sicherheitstür

Alarmanlage

Überwachungskameras

Bewegungsmelder

#### Organisatorische Sicherheitsmechanismen

Definition: Regeln und Abläufe, die Sicherheit erhöhen.
Beispiele:

Nachbarn bitten, die Wohnung im Auge zu behalten

Sicherheitsrichtlinien, z. B. nie den Schlüssel draußen verstecken

Mietvertrag mit Sicherheitsdienst im Gebäude

#### Technische / digitale Sicherheitsmechanismen

Definition: Technologien, die digitale oder physische Ressourcen schützen.
Beispiele:

Smart-Lock mit Zugangskontrolle

Kamera mit Cloud-Video

elektronisches Türschloss mit Zwei-Faktor-Authentisierung

#### Detektivische Mechanismen

Definition: Maßnahmen, die Vorfälle erkennen oder nachvollziehbar machen.
Beispiele:

Kameras mit Protokollierung

Türsensoren, die Öffnungen loggen

Smart-Home-Benachrichtigungen

## 2. Key Space

Menge aller Werte für $K_E$ and $K_D$.

### ROT13

Definition (ROT13): Eine Caesar-Verschlüsselung mit festem Verschiebungswert 13.

Da der Schlüssel nicht gewählt werden kann

Schlüsselraum = 1


### Vigènere with key length of n

Definition (Vigenère-Chiffre): Eine polyalphabetische Verschlüsselung, bei der jedes Schlüsselzeichen eine von 26 Caesar-Verschiebungen auswählt.

Bei Schlüssellänge 
𝑛 und 26 möglichen Varianten pro Position:

Schlusselraum = $26^n$


### AES with 256-bit key

Definition (AES): Ein symmetrischer Blockcipher mit Schlüssellängen 128, 192 oder 256 Bit.

Bei 256 Bit gilt:

Schlusselraum = $2^{256}$


### Monoalphabetic substitution with k letters

Definition (monoalphabetische Substitution): Jeder Klartextbuchstabe wird eindeutig einem Geheimtextbuchstaben zugeordnet – also eine Permutation des Alphabets.

Anzahl der möglichen Permutationen:

Schlusselraum = 𝑘!

## 3. XOR

Berechne

$$c0 \oplus c1 = (m0 \oplus k) \oplus (m1 \oplus k) = m0 \oplus m1 = mx$$

Rate immer längere Teile des Schlüssels durch $mx \oplus k_i = m1_i$, bis der Schlüssel k geraten wurde.

Einfach $c0 \oplus k = m0$ und $c1 \oplus k = m1$ berechnen.
