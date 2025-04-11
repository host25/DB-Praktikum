## Projektbeschreibung 
In diesem Projekt soll eine stark vereinfachte Version eines Lieferdienstes für Speisen und Getränke implementiert werden. Wir empfehlen Ihnen vorab, einen Blick auf etablierte Dienste wie Lieferando oder Wolt zu werfen, um einen Ersteindruck zu gewinnen.
Die zu implementierende Plattform Lieferspatz bietet Kunden die Möglichkeit, Essen bequem von Zuhause zu bestellen. Dabei steht den Kunden eine Vielzahl von Restaurants/Imbissen in der Umgebung zur Auswahl. Die Kunden wählen über die LieferspatzWebanwendung ihre Speisen und Getränke bei einem Restaurant ihrer Wahl aus. Die 
Bestellung wird dann per Lieferspatz an das entsprechende Lokal übermittelt, welches das Essen zubereitet. Im letzten Schritt holt ein Lieferspatz-Kurier das Essen bei dem Lokal ab und liefert es bei den Kunden aus. Die Bezahlung wird aus Kundensicht komplett über 
Lieferspatz ausgeführt, im Hintergrund wird das Geld entsprechend zwischen Lieferspatz und dem Lokal aufgeteilt.

## Aufgabenstellung & Projektbeschreibung 
Im folgenden Text finden Sie die genaue Beschreibung von Lieferspatz inklusive der geforderten Funktionalitäten. Zur Einfachheit beschreiben wir die Plattform zunächst aus der Sicht eines teilnehmenden Restaurants und dann aus der Sicht eines Kunden. Kuriere 
und Bezahlsystem müssen nicht abgebildet/implementiert werden. 

## Lieferspatz aus der Sicht eines Restaurants
Ein Restaurant/Imbiss kann bei Lieferspatz einen Geschäftsaccount anlegen. Dazu müssen ein Name, eine Adresse (Straße und Postleitzahl), eine Beschreibung, sowie ein Bild (optional) angegeben werden. Ferner wird beim Anlegen des Accounts ein Passwort 
ausgesucht, welches für zukünftige Logins benötigt wird. Optionen zum Zurücksetzen/Ändern des Passworts müssen nicht umgesetzt werden.Jedes Restaurant besitzt eine individuelle Speisekarte. Zur Einfachheit bezeichnen wir die 
Speisen/Getränke auf der Speisekarte als Items. Ein Restaurant kann jederzeit Items zur Karte hinzufügen, von der Karte entfernen oder verändern. Jedes Item hat einen Namen, eine Beschreibung, einen Preis und ein Bild (optional). Zur Einfachheit nehmen wir an, 
dass jedes Item beliebig oft zubereitet werden kann. Ferner legt jedes Restaurant Öffnungszeiten (von/bis) und Lieferradius fest. Der Lieferradius wird einfach als eine Liste an zulässigen Postleitzahlen angegeben.
Sobald eine Bestellung für ein Restaurant eingeht, wird in der Webanwendung darauf hingewiesen. Das Restaurant kann die Bestellung dann sichten und entweder ablehnen oder bestätigen. Ferner kann ein Restaurant jederzeit die Bestellhistorie einsehen (alle 
Bestellungen für dieses Restaurant). Die Historie enthält sowohl abgeschlossene, als auch laufende (also nicht abgeschlossene oder stornierte) Bestellungen. Dabei sollen alle laufenden Bestellungen zuerst gelistet werden, und danach alle abgeschlossenen und 
stornierten Bestellungen, jeweils zeitlich sortiert nach Eingangstag und -uhrzeit. Zu jeder Bestellung kann ein Restaurant alle Details einsehen.
Um den Bestellvorgang möglichst bequem zu gestalten, können Sie versuchen, die Speisekarten der Restaurants nach verschiedenen Kategorien aufzuteilen (Vorspeisen, Nachtisch, Getränke, Hauptgericht, etc.). Dies setzt natürlich entsprechende zusätzliche 
Angaben auf der Seite des Restaurants voraus.

## Lieferspatz aus Sicht der Kundschaft
Kunden können auf Lieferspatz einen Kundenaccount anlegen. Dazu müssen Vor- und Nachname, Adresse, Postleitzahl und Passwort angegeben werden. Bei dem Passwort gilt dasselbe Prinzip wie bei Restaurants. Nach erfolgreichem Login sehen Kunden eine Übersicht an Restaurants, die zu ihrer PLZ 
liefern können und aktuell geöffnet haben. Bei einem Klick auf ein Restaurant gelangen Kunden zu der Detailansicht mit der Beschreibung des Restaurants und der entsprechenden Speisekarte. Kunden stellen sich ihre Mahlzeit aus den verfügbaren Items von der Speisekarte 
zusammen. Bei jedem Item kann eine Mengenangabe getätigt werden. Zur Einfachheit nehmen wir an, dass die Speisen keinerlei Konfigurationsmöglichkeiten bieten. Sobald die gewünschten Items ausgesucht wurden, navigieren Kunden zur Übersichtsseite ihrer 
Bestellung („zum Warenkorb“ o.ä.). Hier werden nochmal alle Items inklusive Preisen (+Gesamtpreis) gelistet. In dieser Übersicht können einzelne Items direkt gelöscht werden, und es gibt eine Möglichkeit, einen optionalen Zusatztext (z.B. „Burger bitte ohne Zwiebeln”) für das Restaurant zu verfassen. Sind die Kunden mit der Auswahl zufrieden, 
können sie nun die Bestellung abschicken. Nach dem Abschicken der Bestellung können Kunden jederzeit den Status einer Bestellung (s.u.) einsehen. Ferner können Kunden jederzeit auf ihre Bestellhistorie zugreifen und die Details früherer Bestellungen einsehen. Auch hier sollen alle laufenden Bestellungen zuerst 
gelistet werden, und danach alle abgeschlossenen und stornierten Bestellungen, jeweils zeitlich sortiert nach Eingangstag und -uhrzeit. 
Beachten Sie, dass Kunden auch mehrere laufende (nicht abgeschlossene oder stornierte) Bestellungen haben können.

## Status einer Bestellung (beide Sichten)
Ab dem Zeitpunkt des Abschickens (Kundensicht) gilt eine Bestellung als „in Bearbeitung“. Sobald die Bestellung vom Restaurant bestätigt wurde, gilt diese als „in Zubereitung“. Lehnt ein Restaurant die Bestellung ab, 
gilt diese als „storniert“. Sobald die Bestellung zubereitet und versandt wurde, markiert das Restaurant die Bestellung als “abgeschlossen”.

## Studentseite 
Projektanfang ist unter https://github.com/li-vdh/its-tutor-praxisprojectWiSe2425 zu finden. Man kann auch ganz neu von Anfang an beginnen ohne dieses Teil zu nutzen.
