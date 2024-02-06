import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute('DROP  TABLE IF EXISTS posts')

cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",
    ('Pizza & Co','Herzlich willkommen bei Pizza & Co.In einem lebhaften Ambiente, umgeben von italienischem Flair, erwarten Sie handgefertigte Pizzen mit einer modernen Note. Genießen Sie bei uns die perfekte Mischung aus authentischem Geschmack und innovativen Belägen.','narkusstraße 42,45479 duisburg','/Restimage/imbiss.jpeg','3333'))
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",
    ('African Grill','Im African Grill verschmilzt die Essenz Afrikas mit modernem Flair. Treten Sie  in eine warme, farbenfrohe Atmosphäre ein.','Meatstraße 67,40421 MeatStadt','/Restimage/AfricanGrill.jpg','Africa14')
    )
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",
    ('Mahlzeit','Willkommen bei Mahlzeit.Genießen Sie hier kulinarische Meisterwerke, die mit Liebe zubereitet werden, und lassen Sie sich von der Vielfalt internationaler Aromen zu einem wahren Mahlzeit-Genuss verführen.','GutenWeg 4,62789 DergaStadt','/Restimage/Mahlzeit.jpg','1234h'))
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",    
    ('Fries&Friends', 'Willkommen bei Fries&Friends – wo Knusprigkeit auf Geselligkeit trifft.Genießen Sie handgeschnittene Pommes in kreativen Variationen und entdecken Sie, wie Freunde und Fritten zu einer unvergesslichen kulinarischen Erfahrung verschmelzen.','AltWeg 41,39478 Dormst','/Restimage/Fries&friends.jpg','abc47')
    )    
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",
    ('Bonafilde','Ein gemütliches Restaurant mit traditionellen Rezepten und einer herzlichen Atmosphäre. Frische Zutaten und liebevolle Zubereitung verleihen den Gerichten einen unverwechselbaren Geschmack.','Adenauer-Allee 21,50502 Dingen','/Restimage/bonafilde.jpg','4876h'))
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",    
    ('Ember & Ivy','Modernes, gehobenes Restaurant, rustikaler Charme, kreative Fusionen.','MeinWeg 6,25147 wiens','/Restimage/Ember & Ivy.jpg','8910')
    )    
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",
    ('Gourmet Haven','Paradies für Feinschmecker, raffinierte internationale Köstlichkeiten.','Bad Way 78,28963 Altem','/Restimage/Gourmet Haven.jpg','4567'))
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",   
    ('Moonshine','Trendiges, urbanes Restaurant, moderne, global inspirierte Gerichte.','Kamerunische straße 2,17847 Berlin','/Restimage/Moonshine.jpg','0123')
    )    
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",
    ('Queens Garden','Elegantes Restaurant, königliche Atmosphäre, traditionelle und moderne Speisen.','GutenWeg 34,62789 DergaStadt','/Restimage/QueensGarden.jpg','h147'))
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",    
    ('The Grill','Rustikales Restaurant, erstklassige gegrillte Spezialitäten.','Kingpassage 1,40421 Meatstadt','/Restimage/The Grill.jpg','63k41')
    )    
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",
    ('The Kitchen','Familienfreundliches Restaurant, lebendige Atmosphäre, frische Zutaten.','Boss-Allee 87,40432 Dortmund','/Restimage/TheKitchen.jpg','4789'))
cur.execute("INSERT INTO RestaurantAccount (Name, Beschreibung, Adresse,  Bild_path, Passwort) VALUES (?,?,?,?,?)",    
    ('Curious Plate','Neugieriges Restaurant, kreative, unkonventionelle Gerichte.','Den Weg 227,62789 DergaStadt','/Restimage/CuriousPlate.jpg','00014'),    
    )


""" ÖFFNUNGSZEITEN """

cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (1,'Montag','11:00:00', '22:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (1,'Dienstag','00:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (1,'Mittwoch','00:00:00', '22:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (1,'Donerstag','11:00:00', '22:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (1,'Freitag','00:00:00', '22:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (1,'Samstag','10:00:00', '24:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (2,'Montag','10:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (2,'Dienstag','00:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (2,'Mittwoch','10:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (2,'Donnerstag','10:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (2,'Freitag','00:00:00', '24:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (2,'Samstag','10:00:00', '24:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (3,'Montag','09:00:00', '18:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (3,'Dienstag','00:00:00', '18:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (3,'Mittwoch','09:00:00', '18:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (3,'Donnerstag','09:00:00', '18:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (3,'Freitag','09:00:00', '18:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (3,'Samstag','09:00:00', '18:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (4,'Montag','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (4,'Dienstag','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (4,'Mittwoch','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (4,'Donnerstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (4,'Freitag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (4,'Samstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (4,'Sonntag','09:00:00', '18:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (5,'Montag','00:00:00', '24:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (5,'Dienstag','00:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (5,'Mittwoch','12:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (5,'Donnerstag','12:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (5,'Freitag','17:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (5,'Samstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (5,'Sonntag','09:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (6,'Montag','11:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (6,'Dienstag','00:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (6,'Mittwoch','11:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (6,'Donnerstag','11:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (6,'Freitag','11:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (6,'Samstag','11:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (6,'Sonntag','07:00:00', '15:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (7,'Montag','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (7,'Dienstag','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (7,'Mittwoch','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (7,'Donnerstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (7,'Freitag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (7,'Samstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (7,'Sonntag','09:00:00', '18:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (8,'Montag','10:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (8,'Dienstag','00:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (8,'Mittwoch','10:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (8,'Donnerstag','10:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (8,'Freitag','10:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (8,'Samstag','10:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (9,'Montag','06:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (9,'Dienstag','06:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (9,'Mittwoch','06:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (9,'Donnerstag','06:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (9,'Freitag','06:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (9,'Samstag','06:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (9,'Sonntag','06:00:00', '14:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (10,'Montag','09:00:00', '24:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (10,'Dienstag','09:00:00', '24:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (10,'Mittwoch','09:00:00', '24:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (10,'Donnerstag','09:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (10,'Freitag','09:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (10,'Samstag','09:00:00', '24:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (10,'Sonntag','11:00:00', '16:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (11,'Montag','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (11,'Dienstag','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (11,'Mittwoch','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (11,'Donnerstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (11,'Freitag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (11,'Samstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (11,'Sonntag','09:00:00', '18:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (12,'Montag','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (12,'Dienstag','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (12,'Mittwoch','09:00:00', '23:00:00'),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (12,'Donnerstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (12,'Freitag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (12,'Samstag','09:00:00', '23:00:00' ),
)
cur.execute("INSERT INTO Oeffnungszeiten (restaurant_ID,Tag,oeffnet_ab,schliesst_um) VALUES(?,?,?,?)",
    (12,'Sonntag','09:00:00', '18:00:00' ),
)


""" LIEFERRADIUS """

cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (1,40421))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (2,40421))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (3,40421))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (4,40421))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (5,40432))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (6,40432))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (7,40432))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (8,40432))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (1,62789))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (3,62789))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (5,62789))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (8,62789))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (9,39478))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (10,39478))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (11,39478))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (12,39478))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (4,50503))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (8,50503))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (9,50503))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (11,50503))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (2,62789))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (6,62789))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (7,62789))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (11,62789))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",     
    (1,25147))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (10,25147))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (7,25147))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (9,25147))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (8,28963))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (7,28963))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (6,28963))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (4,28963))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (2,45479))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (3,45479))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (11,45479))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (6,45479))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)", 
    (1,54178))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (4,54178))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (5,54178))
cur.execute("INSERT INTO Lieferradius(restaurant_ID,postleitzahl) VALUES(?,?)",
    (9,54178))



cur.execute("INSERT INTO KundenAccount(kvorname,kname,kadresse,kpostleitzahl,kpasswort) VALUES (?, ?, ?, ?, ?)",
    ('Chriss','Nord','Gute Straße 28,40432 GuteStadt','40432','Chris80990'))
cur.execute("INSERT INTO KundenAccount(kvorname,kname,kadresse,kpostleitzahl,kpasswort) VALUES (?, ?, ?, ?, ?)",
    ('Yvan','Censeur','Censeurweg 28,40421 CensVille','40421','cens25'))
cur.execute("INSERT INTO KundenAccount(kvorname,kname,kadresse,kpostleitzahl,kpasswort) VALUES (?, ?, ?, ?, ?)",
    ('Arthur','Kamdem','Money Weg 14,54178 MoneyStadt','54178','kior'))
cur.execute("INSERT INTO KundenAccount(kvorname,kname,kadresse,kpostleitzahl,kpasswort) VALUES (?, ?, ?, ?, ?)",
    ('dan','April','MainWay 1,45479 MainStadt','45479','daam4'))



""" vorspeisen """

cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Moehrensuppe','Vorspeisen/Moehrensuppe.jpg','Leichte Suppe aus frischen Möhren, delikat gewürzt.',5 ,1),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Buttermilchbrot','Vorspeisen/Buttermilchbrot.jpg','Locker-flaumiges Brot mit dem erfrischenden Geschmack von Buttermilch.',5 ,1),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Krautsalat','Vorspeisen/Krautsalat.jpg','Frischer Krautsalat mit knackigen Gemüsestreifen, leicht mariniert.',5 ,1),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Champignonsuppe','Vorspeisen/Champignonsuppe.jpg','Cremige Suppe mit zarten Champignons, perfekt abgeschmeckt.',5 ,2),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Avocado creme','Vorspeisen/Avocado creme.jpg','Samtige Creme aus reifen Avocados, verfeinert mit Kräutern.',5 ,2),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Nizzasalat','Vorspeisen/Nizzasalat.jpg','Klassischer Salat aus Nizza mit Tomaten, Thunfisch und Oliven.',5 ,2),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Bananensuppe','Vorspeisen/Bananensuppe.jpg','Fruchtige Suppe mit Bananen, leicht süß und erfrischend.',5 ,3),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Wassermelonen-suppe','Vorspeisen/Wassermelonen-suppe.jpg','Sommerliche Suppe mit saftiger Wassermelone, erfrischend kühl.',5 ,3),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Karotten-Salat','Vorspeisen/Karotten-Salat.jpg','Frischer Salat aus knackigen Karotten, leicht angemacht.',5 ,3),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Moehrensuppe','Vorspeisen/Moehrensuppe.jpg','Leichte Suppe aus frischen Möhren, delikat gewürzt.',5 ,4),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Wassermelonen-suppe','Vorspeisen/Wassermelonen-suppe.jpg','Sommerliche Suppe mit saftiger Wassermelone, erfrischend kühl.',5 ,4),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Nizzasalat','Vorspeisen/Nizzasalat.jpg','Klassischer Salat aus Nizza mit Tomaten, Thunfisch und Oliven.',5 ,4),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Moehrensuppe','Vorspeisen/Moehrensuppe.jpg','Hier beschreiben',5 ,5),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Buttermilchbrot','Vorspeisen/Buttermilchbrot.jpg','Hier beschreiben',5 ,5),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Nizzasalat','Vorspeisen/Nizzasalat.jpg','Klassischer Salat aus Nizza mit Tomaten, Thunfisch und Oliven.',5 ,5),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Wassermelonen-suppe','Vorspeisen/Wassermelonen-suppe.jpg','Sommerliche Suppe mit saftiger Wassermelone, erfrischend kühl.',5 ,6),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Karotten-Salat','Vorspeisen/Karotten-Salat.jpg','Frischer Salat aus knackigen Karotten, leicht angemacht.',5 ,6),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Moehrensuppe','Vorspeisen/Moehrensuppe.jpg','Leichte Suppe aus frischen Möhren, delikat gewürzt.',5 ,6),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Bananensuppe','Vorspeisen/Bananensuppe.jpg','Fruchtige Suppe mit Bananen, leicht süß und erfrischend.',5 ,7),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Wassermelonen-suppe','Vorspeisen/Wassermelonen-suppe.jpg','Sommerliche Suppe mit saftiger Wassermelone, erfrischend kühl.',5 ,7),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Karotten-Salat','Vorspeisen/Karotten-Salat.jpg','Frischer Salat aus knackigen Karotten, leicht angemacht.',5 ,7),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Buttermilchbrot','Vorspeisen/Buttermilchbrot.jpg','Locker-flaumiges Brot mit dem erfrischenden Geschmack von Buttermilch.',5 ,8),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Krautsalat','Vorspeisen/Krautsalat.jpg','Frischer Krautsalat mit knackigen Gemüsestreifen, leicht mariniert.',5 ,8),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Champignonsuppe','Vorspeisen/Champignonsuppe.jpg','Cremige Suppe mit zarten Champignons, perfekt abgeschmeckt.',5 ,8),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Wassermelonen-suppe','Vorspeisen/Wassermelonen-suppe.jpg','Sommerliche Suppe mit saftiger Wassermelone, erfrischend kühl.',5 ,9),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Karotten-Salat','Vorspeisen/Karotten-Salat.jpg','Frischer Salat aus knackigen Karotten, leicht angemacht.',5 ,9),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Buttermilchbrot','Vorspeisen/Buttermilchbrot.jpg','Locker-flaumiges Brot mit dem erfrischenden Geschmack von Buttermilch.',5 ,9),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Krautsalat','Vorspeisen/Krautsalat.jpg','Frischer Krautsalat mit knackigen Gemüsestreifen, leicht mariniert.',5 ,9),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Wassermelonen-suppe','Vorspeisen/Wassermelonen-suppe.jpg','Sommerliche Suppe mit saftiger Wassermelone, erfrischend kühl.',5 ,10),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Karotten-Salat','Vorspeisen/Karotten-Salat.jpg','Frischer Salat aus knackigen Karotten, leicht angemacht.',5 ,10),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Moehrensuppe','Vorspeisen/Moehrensuppe.jpg','Leichte Suppe aus frischen Möhren, delikat gewürzt.',5 ,10),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Bananensuppe','Vorspeisen/Bananensuppe.jpg','Fruchtige Suppe mit Bananen, leicht süß und erfrischend.',5 ,10),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Wassermelonen-suppe','Vorspeisen/Wassermelonen-suppe.jpg','Sommerliche Suppe mit saftiger Wassermelone, erfrischend kühl.',5 ,10),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Moehrensuppe','Vorspeisen/Moehrensuppe.jpg','Leichte Suppe aus frischen Möhren, delikat gewürzt.',5 ,11),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Buttermilchbrot','Vorspeisen/Buttermilchbrot.jpg','Locker-flaumiges Brot mit dem erfrischenden Geschmack von Buttermilch.',5 ,11),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Krautsalat','Vorspeisen/Krautsalat.jpg','Frischer Krautsalat mit knackigen Gemüsestreifen, leicht mariniert.',5 ,11),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Karotten-Salat','Vorspeisen/Karotten-Salat.jpg','Frischer Salat aus knackigen Karotten, leicht angemacht.',5 ,12),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Buttermilchbrot','Vorspeisen/Buttermilchbrot.jpg','Locker-flaumiges Brot mit dem erfrischenden Geschmack von Buttermilch.',5 ,12),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Krautsalat','Vorspeisen/Krautsalat.jpg','Frischer Krautsalat mit knackigen Gemüsestreifen, leicht mariniert.',5 ,12),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Wassermelonen-suppe','Vorspeisen/Wassermelonen-suppe.jpg','Sommerliche Suppe mit saftiger Wassermelone, erfrischend kühl.',5 ,12),
)
cur.execute(" INSERT INTO Vorspeisen(VName,VBild,VBeschreibung,VPreis,restaurant_ID) VALUES  (?, ?, ?, ?, ?)",
    ('Karotten-Salat','Vorspeisen/Karotten-Salat.jpg','Frischer Salat aus knackigen Karotten, leicht angemacht.',5 ,12),
)

""" Hauptgerichte """

cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Eru mit Gari','Hauptgerichte/Eru mit Gari.jpg','Traditionelles Gericht mit Eru-Blättern und Gari (Maniokmehl).',12 ,2),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Koki mit Bananen','Hauptgerichte/Koki mit Bananen.jpg','Köstliches Gericht aus Koki-Bohnen serviert mit Bananen.',25 ,2),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('poulet DG','Hauptgerichte/poulet DG.jpg','Afrikanisches Hähnchengericht mit Gemüse, Kochbananen und würziger Sauce.',28 ,2),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Okok sucré et salé','Hauptgerichte/Okok sucré et salé.jpg','Geschmacksintensives Gericht mit süßen und salzigen Aromen.',10 ,2),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pommes mit Curry Wurst','Hauptgerichte/Pommes mit Curry Wurst.jpg','Klassische Pommes mit herzhafter Currywurst',6.50 ,1),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Chili Cheese Fries','Hauptgerichte/Chili Cheese Fries.jpg','Pommes mit würzigem Chili, Käse und sahniger Sauce.',9 ,1),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Gebratener Reis mit Pouletwuerfel','Hauptgerichte/Gebratener Reis mit Pouletwuerfel.jpg','Perfekt gebratener Reis mit zarten Hähnchenstücken.',12 ,1),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Kalb Schnitzel','Hauptgerichte/Kalb Schnitzel.jpg','Zartes Kalbsschnitzel, goldbraun gebraten.',16 ,1),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Bauerntopf','Hauptgerichte/Bauerntopf.jpg','Herzhafter Eintopf mit Fleisch und frischem Gemüse.',9 ,3),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Paprika-Sähne-Hähnchen','Hauptgerichte/Paprika-Sähne-Hähnchen.jpg','Saftiges Hähnchen in cremiger Paprikasauce.',10 ,3),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Rinderroulade klassich','Hauptgerichte/Rinderroulade klassich.jpg','Klassisch zubereitete Rinderroulade mit herzhafter Füllung.',17 ,3),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Omas beste Frikadellen','Hauptgerichte/Omas beste Frikadellen.jpg','Traditionelle Frikadellen nach Omas bewährtem Rezept.',7 ,3),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pasta Bolognese','Hauptgerichte/Pasta Bolognese.jpg','Al dente gekochte Pasta mit herzhafter Bolognesesauce.',8 ,3),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pizza Thunfisch','Hauptgerichte/thunfisch.jpeg','Pizza belegt mit saftigem Thunfisch und frischen Zutaten.',8 ,4),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pizza Hawaii','Hauptgerichte/Hawaii.jpeg','Klassische Pizza mit Ananas und Schinken.',7.20 ,4),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pizza Salami','Hauptgerichte/pizza salami.jpeg','Pizza mit würziger Salami und schmelzendem Käse.',7 ,4),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Mista Salat','Hauptgerichte/Salat.jpeg','Bunter gemischter Salat mit frischem Gemüse und Dressing.',9 ,4),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Koki mit Bananen','Hauptgerichte/Koki mit Bananen.jpg','Köstliches Gericht aus Koki-Bohnen serviert mit Bananen.',25 ,5),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('poulet DG','Hauptgerichte/poulet DG.jpg','Afrikanisches Hähnchengericht mit Gemüse, Kochbananen und würziger Sauce.',28 ,5),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Okok sucré et salé','Hauptgerichte/Okok sucré et salé.jpg','Geschmacksintensives Gericht mit süßen und salzigen Aromen.',10 ,5),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pommes mit Curry Wurst','Hauptgerichte/Pommes mit Curry Wurst.jpg','Klassische Pommes mit herzhafter Currywurst',6.50 ,5),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Chili Cheese Fries','Hauptgerichte/Chili Cheese Fries.jpg','Pommes mit würzigem Chili, Käse und sahniger Sauce.',9 ,5),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Rinderroulade klassich','Hauptgerichte/Rinderroulade klassich.jpg','Klassisch zubereitete Rinderroulade mit herzhafter Füllung.',17 ,6),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Omas beste Frikadellen','Hauptgerichte/Omas beste Frikadellen.jpg','Traditionelle Frikadellen nach Omas bewährtem Rezept.',7 ,6),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pasta Bolognese','Hauptgerichte/Pasta Bolognese.jpg','Al dente gekochte Pasta mit herzhafter Bolognesesauce.',8 ,6),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pizza Thunfisch','Hauptgerichte/thunfisch.jpeg','Pizza belegt mit saftigem Thunfisch und frischen Zutaten.',8 ,6),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pizza Hawaii','Hauptgerichte/Hawaii.jpeg','Klassische Pizza mit Ananas und Schinken.',7.20 ,7),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Chili Cheese Fries','Hauptgerichte/Chili Cheese Fries.jpg','Pommes mit würzigem Chili, Käse und sahniger Sauce.',9 ,7),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Gebratener Reis mit Pouletwuerfel','Hauptgerichte/Gebratener Reis mit Pouletwuerfel.jpg','Perfekt gebratener Reis mit zarten Hähnchenstücken.',12 ,7),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Kalb Schnitzel','Hauptgerichte/Kalb Schnitzel.jpg','Zartes Kalbsschnitzel, goldbraun gebraten.',16 ,8),
)

cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Eru mit Gari','Hauptgerichte/Eru mit Gari.jpg','Traditionelles Gericht mit Eru-Blättern und Gari (Maniokmehl).',12 ,8),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Koki mit Bananen','Hauptgerichte/Koki mit Bananen.jpg','Köstliches Gericht aus Koki-Bohnen serviert mit Bananen.',25 ,8),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('poulet DG','Hauptgerichte/poulet DG.jpg','Afrikanisches Hähnchengericht mit Gemüse, Kochbananen und würziger Sauce.',28 ,8),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Okok sucré et salé','Hauptgerichte/Okok sucré et salé.jpg','Geschmacksintensives Gericht mit süßen und salzigen Aromen.',10 ,8),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pommes mit Curry Wurst','Hauptgerichte/Pommes mit Curry Wurst.jpg','Klassische Pommes mit herzhafter Currywurst',6.50 ,9),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Chili Cheese Fries','Hauptgerichte/Chili Cheese Fries.jpg','Pommes mit würzigem Chili, Käse und sahniger Sauce.',9 ,9),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Gebratener Reis mit Pouletwuerfel','Hauptgerichte/Gebratener Reis mit Pouletwuerfel.jpg','Perfekt gebratener Reis mit zarten Hähnchenstücken.',12 ,9),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Kalb Schnitzel','Hauptgerichte/Kalb Schnitzel.jpg','Zartes Kalbsschnitzel, goldbraun gebraten.',16 ,9),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Bauerntopf','Hauptgerichte/Bauerntopf.jpg','Herzhafter Eintopf mit Fleisch und frischem Gemüse.',9 ,10),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Paprika-Sähne-Hähnchen','Hauptgerichte/Paprika-Sähne-Hähnchen.jpg','Saftiges Hähnchen in cremiger Paprikasauce.',10 ,10),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Rinderroulade klassich','Hauptgerichte/Rinderroulade klassich.jpg','Klassisch zubereitete Rinderroulade mit herzhafter Füllung.',17 ,10),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Omas beste Frikadellen','Hauptgerichte/Omas beste Frikadellen.jpg','Traditionelle Frikadellen nach Omas bewährtem Rezept.',7 ,10),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pasta Bolognese','Hauptgerichte/Pasta Bolognese.jpg','Al dente gekochte Pasta mit herzhafter Bolognesesauce.',8 ,10),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pizza Thunfisch','Hauptgerichte/thunfisch.jpeg','Pizza belegt mit saftigem Thunfisch und frischen Zutaten.',8 ,11),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pizza Hawaii','Hauptgerichte/Hawaii.jpeg','Klassische Pizza mit Ananas und Schinken.',7.20 ,11),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pizza Salami','Hauptgerichte/pizza salami.jpeg','Pizza mit würziger Salami und schmelzendem Käse.',7 ,11),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Mista Salat','Hauptgerichte/Salat.jpeg','Bunter gemischter Salat mit frischem Gemüse und Dressing.',9 ,11),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Koki mit Bananen','Hauptgerichte/Koki mit Bananen.jpg','Köstliches Gericht aus Koki-Bohnen serviert mit Bananen.',25 ,11),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('poulet DG','Hauptgerichte/poulet DG.jpg','Afrikanisches Hähnchengericht mit Gemüse, Kochbananen und würziger Sauce.',28 ,12),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Okok sucré et salé','Hauptgerichte/Okok sucré et salé.jpg','Geschmacksintensives Gericht mit süßen und salzigen Aromen.',10 ,12),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pommes mit Curry Wurst','Hauptgerichte/Pommes mit Curry Wurst.jpg','Klassische Pommes mit herzhafter Currywurst',6.50 ,12),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Chili Cheese Fries','Hauptgerichte/Chili Cheese Fries.jpg','Pommes mit würzigem Chili, Käse und sahniger Sauce.',9 ,12),
)
cur.execute("INSERT INTO Hauptgericht(HName,HBild,HBeschreibung,HPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Rinderroulade klassich','Hauptgerichte/Rinderroulade klassich.jpg','Klassisch zubereitete Rinderroulade mit herzhafter Füllung.',17 ,12),
)


""" Nachtisch """

cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Himbeer-Puddingcreme Schnitten','Nachtisch/Himbeer-Puddingcreme Schnitten.jpg','mit fruchtiger Himbeer-Puddingcreme zwischen zarten Schichten.',10 ,1)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Biskuitrolle','Nachtisch/Biskuitrolle.jpg','Luftige Biskuitrolle, gefüllt mit einer delikaten Creme.',5 ,1)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Blitz Käsekuchen mit Vanillepudding','Nachtisch/Blitz Käsekuchen mit Vanillepudding.jpg','Schnell zubereiteter Käsekuchen mit cremigem Vanillepudding..',6 ,1)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Käsekuchen Muffins','Nachtisch/Käsekuchen Muffins.jpg','Mini-Käsekuchen in Muffin-Form, perfekt für kleine Genussmomente.',7 ,1)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Mandarinenkuchen mit Schmand','Nachtisch/Mandarinenkuchen mit Schmand.jpg','Saftiger Mandarinenkuchen, verfeinert mit Schmand.',6 ,2)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Saftiger Zitronenkuchen mit Frischkäse','Nachtisch/Saftiger Zitronenkuchen mit Frischkäse.jpg','Herrlich saftiger Zitronenkuchen mit einer Frischkäse-Glasur.',10 ,2)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Schoko-Kokos-Kuchen vom Blech','Nachtisch/Schoko-Kokos-Kuchen vom Blech.jpg','Sündhaft leckerer Schoko-Kokos-Kuchen, auf dem Blech gebacken.',9 ,2)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Erdbeer Fanta Kuchen','Nachtisch/Erdbeer Fanta Kuchen.jpg','Erfrischender Kuchen mit dem süßen Geschmack von Erdbeeren und Fanta.',9 ,2)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Mousse au chocolat','Nachtisch/Mousse au chocolat.jpg','Zarte Schokoladenmousse, ein himmlisch luftiges Dessert.',7 ,3)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Spaghetti-Eis Dessert','Nachtisch/Spaghetti-Eis Dessert.jpg','Kreatives Dessert, das wie Spaghetti aussieht, aber süß und fruchtig ist',10 ,3)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Dessert mit Weintrauben','Nachtisch/Dessert mit Weintrauben.jpg','Leichtes Dessert mit frischen Weintrauben, perfekt für den süßen Abschluss.',5 ,3)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Apple Crumble','Nachtisch/Apple Crumble.jpg','Knuspriger Apfel-Crumble mit zimtiger Note.',7 ,4)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Crème brûlée','Nachtisch/Crème brûlée.jpg','Klassische Crème brûlée mit karamellisierter Zuckerkruste.',7 ,4)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Melonen-Hai','Nachtisch/Melonen-Hai.jpg','Lustiges Dessert in Hai-Form, basierend auf erfrischender Melone.',8 ,4)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Schokosoufflee medium','Nachtisch/Schokosoufflee medium.jpg','Mittelgroßes Schokoladensoufflé, warm und verführerisch.',9 ,5)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Dicke Obst-Pfannkuchen','Nachtisch/Dicke Obst-Pfannkuchen.jpg','Fluffige Pfannkuchen, dick und reichhaltig, garniert mit frischem Obst.',17 ,5)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Käsekuchen Muffins','Nachtisch/Käsekuchen Muffins.jpg','Mini-Käsekuchen in Muffin-Form, perfekt für kleine Genussmomente.',17 ,5)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Mandarinenkuchen mit Schmand','Nachtisch/Mandarinenkuchen mit Schmand.jpg','Saftiger Mandarinenkuchen, verfeinert mit Schmand.',13 ,5)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Saftiger Zitronenkuchen mit Frischkäse','Nachtisch/Saftiger Zitronenkuchen mit Frischkäse.jpg','Herrlich saftiger Zitronenkuchen mit einer Frischkäse-Glasur.',7 ,6)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Schoko-Kokos-Kuchen vom Blech','Nachtisch/Schoko-Kokos-Kuchen vom Blech.jpg','Sündhaft leckerer Schoko-Kokos-Kuchen, auf dem Blech gebacken.',8 ,6)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Erdbeer Fanta Kuchen','Nachtisch/Erdbeer Fanta Kuchen.jpg','Erfrischender Kuchen mit dem süßen Geschmack von Erdbeeren und Fanta.',9 ,6)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Saftiger Zitronenkuchen mit Frischkäse','Nachtisch/Saftiger Zitronenkuchen mit Frischkäse.jpg','Herrlich saftiger Zitronenkuchen mit einer Frischkäse-Glasur.',9 ,6)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Schoko-Kokos-Kuchen vom Blech','Nachtisch/Schoko-Kokos-Kuchen vom Blech.jpg','Sündhaft leckerer Schoko-Kokos-Kuchen, auf dem Blech gebacken.',13 ,7)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Erdbeer Fanta Kuchen','Nachtisch/Erdbeer Fanta Kuchen.jpg','Erfrischender Kuchen mit dem süßen Geschmack von Erdbeeren und Fanta.',9 ,7)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Mousse au chocolat','Nachtisch/Mousse au chocolat.jpg','Zarte Schokoladenmousse, ein himmlisch luftiges Dessert.',5 ,7)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Spaghetti-Eis Dessert','Nachtisch/Spaghetti-Eis Dessert.jpg','Kreatives Dessert, das wie Spaghetti aussieht, aber süß und fruchtig ist',6 ,8)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Dessert mit Weintrauben','Nachtisch/Dessert mit Weintrauben.jpg','Leichtes Dessert mit frischen Weintrauben, perfekt für den süßen Abschluss.',5 ,8)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Apple Crumble','Nachtisch/Apple Crumble.jpg','Knuspriger Apfel-Crumble mit zimtiger Note.',8 ,8)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Crème brûlée','Nachtisch/Crème brûlée.jpg','Klassische Crème brûlée mit karamellisierter Zuckerkruste.',9 ,8)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Himbeer-Puddingcreme Schnitten','Nachtisch/Himbeer-Puddingcreme Schnitten.jpg','mit fruchtiger Himbeer-Puddingcreme zwischen zarten Schichten.',11 ,9)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Biskuitrolle','Nachtisch/Biskuitrolle.jpg','Luftige Biskuitrolle, gefüllt mit einer delikaten Creme.',10 ,9)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Blitz Käsekuchen mit Vanillepudding','Nachtisch/Blitz Käsekuchen mit Vanillepudding.jpg','Schnell zubereiteter Käsekuchen mit cremigem Vanillepudding..',14 ,9)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Käsekuchen Muffins','Nachtisch/Käsekuchen Muffins.jpg','Mini-Käsekuchen in Muffin-Form, perfekt für kleine Genussmomente.',7 ,10)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Schoko-Kokos-Kuchen vom Blech','Nachtisch/Schoko-Kokos-Kuchen vom Blech.jpg','Sündhaft leckerer Schoko-Kokos-Kuchen, auf dem Blech gebacken.',9 ,10)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Erdbeer Fanta Kuchen','Nachtisch/Erdbeer Fanta Kuchen.jpg','Erfrischender Kuchen mit dem süßen Geschmack von Erdbeeren und Fanta.',12 ,10)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Saftiger Zitronenkuchen mit Frischkäse','Nachtisch/Saftiger Zitronenkuchen mit Frischkäse.jpg','Herrlich saftiger Zitronenkuchen mit einer Frischkäse-Glasur.',9 ,10)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Schoko-Kokos-Kuchen vom Blech','Nachtisch/Schoko-Kokos-Kuchen vom Blech.jpg','Sündhaft leckerer Schoko-Kokos-Kuchen, auf dem Blech gebacken.',9 ,11)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Erdbeer Fanta Kuchen','Nachtisch/Erdbeer Fanta Kuchen.jpg','Erfrischender Kuchen mit dem süßen Geschmack von Erdbeeren und Fanta.',8 ,11)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Mousse au chocolat','Nachtisch/Mousse au chocolat.jpg','Zarte Schokoladenmousse, ein himmlisch luftiges Dessert.',9 ,11)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Himbeer-Puddingcreme Schnitten','Nachtisch/Himbeer-Puddingcreme Schnitten.jpg','mit fruchtiger Himbeer-Puddingcreme zwischen zarten Schichten.',5 ,12)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Biskuitrolle','Nachtisch/Biskuitrolle.jpg','Luftige Biskuitrolle, gefüllt mit einer delikaten Creme.',8 ,12)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Blitz Käsekuchen mit Vanillepudding','Nachtisch/Blitz Käsekuchen mit Vanillepudding.jpg','Schnell zubereiteter Käsekuchen mit cremigem Vanillepudding..',9 ,12)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Käsekuchen Muffins','Nachtisch/Käsekuchen Muffins.jpg','Mini-Käsekuchen in Muffin-Form, perfekt für kleine Genussmomente.',11 ,12)
)
cur.execute("INSERT INTO Nachtisch(Nname,NBild,NBeschreibung,NPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Schoko-Kokos-Kuchen vom Blech','Nachtisch/Schoko-Kokos-Kuchen vom Blech.jpg','Sündhaft leckerer Schoko-Kokos-Kuchen, auf dem Blech gebacken.',8 ,12)
)


""" GETRÄNKE """

cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Helles','Getränke/helles.jpg','Mit Alkohol',5 ,1)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Fruchtsaft','Getränke/Fruchtsaft.jpg','Alkoholfrei',4 ,1)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Eistee','Getränke/fuzetee.jpg','Alkoholfrei',3 ,1)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,1)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Ingwerbier','Getränke/ingwerbier.jpg','Alkoholfrei',4 ,1)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Limonade','Getränke/limonade.jpg','Alkoholfrei',5 ,2)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pilsner','Getränke/pilsner.jpg','Mit Alkohol',5 ,2)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wodka','Getränke/wodka.jpg','Mit Alkohol',8 ,2)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,2)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sekt','Getränke/Sekt.jpg','Mit Alkohol',12 ,2)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sprite','Getränke/Sprite.jpeg','Alkoholfrei',3 ,2)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Cola','Getränke/Cola.jpeg','Alkoholfrei',4 ,2)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Bier','Getränke/Bier.jpeg','Mit Alkohol',5 ,3)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,3)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Fanta','Getränke/fanta.jpg','Alkoholfrei',4 ,3)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sprite','Getränke/Sprite.jpeg','Alkoholfrei',3 ,3)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Cola','Getränke/Cola.jpeg','Alkoholfrei',4 ,3)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,4)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sprite','Getränke/Sprite.jpeg','Alkoholfrei',3 ,4)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Cola','Getränke/Cola.jpeg','Alkoholfrei',4 ,4)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Fruchtsaft','Getränke/Fruchtsaft.jpg','Alkoholfrei',4 ,5)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Eistee','Getränke/fuzetee.jpg','Alkoholfrei',3 ,5)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,5)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Ingwerbier','Getränke/ingwerbier.jpg','Alkoholfrei',4 ,5)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Limonade','Getränke/limonade.jpg','Alkoholfrei',5 ,6)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pilsner','Getränke/pilsner.jpg','Mit Alkohol',5 ,6)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Bier','Getränke/Bier.jpeg','Mit Alkohol',5 ,6)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,6)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Fanta','Getränke/fanta.jpg','Alkoholfrei',4 ,6)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,7)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sprite','Getränke/Sprite.jpeg','Alkoholfrei',3 ,7)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wodka','Getränke/wodka.jpg','Mit Alkohol',8 ,7)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sprite','Getränke/Sprite.jpeg','Alkoholfrei',3 ,7)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Cola','Getränke/Cola.jpeg','Alkoholfrei',4 ,7)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,8)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Cola','Getränke/Cola.jpeg','Alkoholfrei',4 ,8)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sekt','Getränke/Sekt.jpg','Mit Alkohol',12 ,8)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Bier','Getränke/Bier.jpeg','Mit Alkohol',5 ,8)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Fanta','Getränke/fanta.jpg','Alkoholfrei',4 ,8)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,9)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sprite','Getränke/Sprite.jpeg','Alkoholfrei',3 ,9)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Cola','Getränke/Cola.jpeg','Alkoholfrei',4 ,9)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Fruchtsaft','Getränke/Fruchtsaft.jpg','Alkoholfrei',4 ,9)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Eistee','Getränke/fuzetee.jpg','Alkoholfrei',3 ,10)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Ingwerbier','Getränke/ingwerbier.jpg','Alkoholfrei',4 ,10)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Limonade','Getränke/limonade.jpg','Alkoholfrei',5 ,10)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pilsner','Getränke/pilsner.jpg','Mit Alkohol',5 ,10)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,10)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Limonade','Getränke/limonade.jpg','Alkoholfrei',5 ,11)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pilsner','Getränke/pilsner.jpg','Mit Alkohol',5 ,11)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Bier','Getränke/Bier.jpeg','Mit Alkohol',5 ,11)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,11)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Fanta','Getränke/fanta.jpg','Alkoholfrei',4 ,11)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Wasser','Getränke/wasser.jpg',' Alkoholfrei',2.5 ,12)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Sprite','Getränke/Sprite.jpeg','Alkoholfrei',3 ,12)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Limonade','Getränke/limonade.jpg','Alkoholfrei',5 ,12)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Pilsner','Getränke/pilsner.jpg','Mit Alkohol',5 ,12)
)
cur.execute("INSERT INTO Getraenke (GName,GBild,GBeschreibung,GPreis,restaurant_ID) VALUES(?,?,?,?,?)",
    ('Cola','Getränke/Cola.jpeg','Alkoholfrei',4 ,12)
)



connection.commit()
connection.close()