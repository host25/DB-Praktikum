DROP TABLE IF EXISTS RestaurantAccount;
DROP TABLE IF EXISTS Oeffnungszeiten;
DROP TABLE IF EXISTS Vorspeisen;
DROP TABLE IF EXISTS Hauptgericht;
DROP TABLE IF EXISTS Nachtisch;
DROP TABLE IF EXISTS Getraenke;
DROP TABLE IF EXISTS Lieferradius;
DROP TABLE IF EXISTS KundenAccount;
DROP TABLE IF EXISTS Bestellung;
DROP TABLE IF EXISTS Items; 


CREATE TABLE RestaurantAccount(
 restaurant_ID INTEGER PRIMARY KEY AUTOINCREMENT,
 Name VARCHAR(50) NOT NULL ,
 Beschreibung VARCHAR(255) NOT NULL,
 Adresse VARCHAR(150) NOT NULL,
 Bild_path TEXT NOT NULL,    
 Passwort VARCHAR(50) NOT NULL
 );

CREATE TABLE Oeffnungszeiten (
OID INTEGER PRIMARY KEY AUTOINCREMENT,
restaurant_ID INT NOT NULL,
Tag VARCHAR(20) NOT NULL,
oeffnet_ab TEXT,
schliesst_um TEXT,
FOREIGN KEY(restaurant_ID) REFERENCES RestaurantAccount(restaurant_ID)
);

CREATE TABLE Lieferradius(
 LID INTEGER PRIMARY KEY AUTOINCREMENT,
 postleitzahl TEXT NOT NULL,
 restaurant_ID INT,
 FOREIGN KEY (restaurant_ID) REFERENCES RestaurantAccount(restaurant_ID) 
 );


CREATE TABLE KundenAccount(
 kundenNr INTEGER PRIMARY KEY AUTOINCREMENT,
 kvorname VARCHAR(100) NOT NULL,
 kname VARCHAR(100) NOT NULL,
 kadresse VARCHAR(200) NOT NULL,
 kpostleitzahl INT NOT NULL,
 kpasswort VARCHAR(20) NOT NULL
 );

CREATE TABLE Bestellung(
 bestellNr INTEGER PRIMARY KEY AUTOINCREMENT,
 created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
 status VARCHAR(50),
 gesamtpreis FLOAT NOT NULL,
 anmerkung TEXT,
 restName VARCHAR(50) NOT NULL,
 kundenNr INTEGER NOT NULL, 
 kundenAdr VARCHAR(200) NOT NULL,
 restaurant_ID INTEGER NOT NULL,
 FOREIGN KEY(restaurant_ID) REFERENCES RestaurantAccount(restaurant_ID),
 FOREIGN KEY(kundenNr) REFERENCES KundenAccount(kundenNr)
 ); 

CREATE TABLE Items (
    ItemsID INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    anzahl INTEGER NOT NULL,
    preis INTEGER NOT NULL,
    bestellNr INTEGER NOT NULL,
    itemName VARCHAR(100) NOT NULL,
    kundenNr INTEGER NOT NULL,
    FOREIGN KEY(kundenNr) REFERENCES KundenAccount(kundenNr)
);

CREATE TABLE Vorspeisen(
VID INTEGER PRIMARY KEY AUTOINCREMENT,
VName VARCHAR(50) NOT NULL,
VBild VARCHAR(255) NOT NULL,
VBeschreibung VARCHAR(255) NOT NULL,
VPreis INT NOT NULL,
restaurant_ID INTEGER NOT NULL,
FOREIGN KEY(restaurant_ID) REFERENCES RestaurantAccount(restaurant_ID)
);

CREATE TABLE Hauptgericht (
HID INTEGER PRIMARY KEY AUTOINCREMENT,
HName VARCHAR(50) NOT NULL,
HBild VARCHAR(255) NOT NULL,
HBeschreibung VARCHAR(255) NOT NULL,
HPreis FLOAT NOT NULL,
restaurant_ID INTEGER NOT NULL,
FOREIGN KEY(restaurant_ID) REFERENCES RestaurantAccount(restaurant_ID)
);
CREATE TABLE Nachtisch(
NID INTEGER PRIMARY KEY AUTOINCREMENT,
Nname VARCHAR(50) NOT NULL,
NBild VARCHAR(255) NOT NULL,
NBeschreibung VARCHAR(255) NOT NULL,
NPreis FLOAT NOT NULL,
restaurant_ID INTEGER NOT NULL,
FOREIGN KEY(restaurant_ID) REFERENCES RestaurantAccount(restaurant_ID)
);
CREATE TABLE Getraenke(
GID INTEGER PRIMARY KEY AUTOINCREMENT,
GName VARCHAR(50) NOT NULL,
GBild VARCHAR(255) NOT NULL,
GBeschreibung VARCHAR(255) NOT NULL,
GPreis FLOAT NOT NULL,
restaurant_ID INTEGER NOT NULL,
FOREIGN KEY(restaurant_ID) REFERENCES RestaurantAccount(restaurant_ID)
);

