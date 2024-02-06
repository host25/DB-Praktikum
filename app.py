import sqlite3,os     #os , um Dateien zu importieren
from datetime import datetime 
from flask import Flask, render_template, request, url_for, flash, redirect, abort,session,g
from flask_login import LoginManager,UserMixin,login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename  # Für sicheres Hochladen von Dateien
from flask_socketio import SocketIO

app = Flask(__name__,static_folder='static')
app.config['SECRET_KEY'] = 'kior237'
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.init_app(app) 


def get_db_connection():          #Datenbankverbindung herstellen
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


#SocketIO-Integration für die bidirektionale Echtzeitkommunikation zwischen dem Server und dem Client
@socketio.on('connect', namespace='/restaurants')
def handle_connect():
    print('Client connected:', request.sid)

@socketio.on('disconnect', namespace='/restaurants')
def handle_disconnect():
    print('Client disconnected:', request.sid)


#Routen definieren, was passieren soll, wenn ein Benutzer auf eine bestimmte URL zugreift.
@app.route('/')
def index():
    return render_template('index.html')  #Template-Rendering:um Webseiten zu generieren und an den Benutzer zu senden

@app.route('/Error')
def Error():
    return render_template('Error.html')


#creation new user et restaurant
@app.route('/UserRegister/', methods=('GET', 'POST'))
def NewUser(): 
    if request.method == 'POST':                       #HTTP-POST-Anfrage
        kvorname = request.form['kvorname']               # die Formulardaten werden aus der Anfrage extrahiert
        kname = request.form['kname']
        Straße = request.form['Straße']
        kpostleitzahl = request.form['kpostleitzahl']
        Stadt = request.form['Stadt']
        kAdresse = Straße +", " + kpostleitzahl + " " + Stadt
        kpasswort = request.form['kpasswort']
        Mypost = ['40421','40432','62789','39478','50503','54178','25147','28963','45479']

        if kpostleitzahl not in Mypost:
            flash('Momentant können wir nicht an diesem Postleitzahl liefern. Sie könnten mit (40421-40432-62789-39478-50503-54178-25147-28963-45479) versuchen 😃')
            return render_template('UserRegister.html')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO KundenAccount(kvorname, kname, kadresse, kpostleitzahl, kpasswort) VALUES (?, ?, ?, ?, ?)',
                         (kvorname,kname,kAdresse,kpostleitzahl,kpasswort))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
    return render_template('UserRegister.html')

@app.route('/RestRegister/', methods=('GET', 'POST'))
def NewRest():
    if request.method == 'POST':
        Name = request.form['Name']
        Beschreibung = request.form['Beschreibung']
        Adresse = request.form['Adresse']
        bild = request.files['bild']
        Passwort = request.form['Passwort']
        if bild:
                secure_bild=secure_filename(bild.filename)
                bild_path = os.path.join('static/Restimage', secure_bild)
                bild.save(bild_path)
                bild_path = os.path.normpath(bild_path)
        with get_db_connection() as conn:
            conn.execute('INSERT INTO RestaurantAccount(Name, Beschreibung, Adresse, Bild_path, Passwort) VALUES (?, ?, ?, ?, ?)',
                             (Name, Beschreibung, Adresse, bild_path, Passwort))
            conn.commit()
            restaurant_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
        try:
            selected_days = request.form.getlist('selected_days')
            if selected_days:
                for day in selected_days:
                    Tag=day
                    oeffnet_ab = request.form.get(f"{day}_oeffnet_ab")
                    schliesst_um = request.form.get(f"{day}_schliesst_um")
                    if any(value is None for value in (Tag, oeffnet_ab, schliesst_um)):
                        continue 
                    conn.execute('INSERT INTO Oeffnungszeiten (restaurant_ID, Tag, oeffnet_ab, schliesst_um) VALUES (?, ?, ?, ?)',
                                (restaurant_id, Tag, oeffnet_ab, schliesst_um))
            conn.commit()

            selected_postleitzahlen = [request.form.get(f"selected_postleitzahl_{postleitzahl}") for postleitzahl in ["40421", "40432", "62789", "39478","50503", "54178", "25147", "28963", "45479"] if request.form.get(f"selected_postleitzahl_{postleitzahl}")]
            if selected_postleitzahlen:
                for postleitzahl in selected_postleitzahlen:
                    conn.execute('INSERT INTO Lieferradius(restaurant_ID, Postleitzahl) VALUES (?, ?)',
                                (restaurant_id,postleitzahl))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Erreur SQLite: {e}")
        finally: conn.close()
        return redirect(url_for('login2'))
    return render_template('RestRegister.html')

#login User
class User(UserMixin):              # wird verwendet, um die Daten eines Benutzers zu speichern, der sich anmeldet oder registriert
    def __init__(self, user_id, kvorname, kname):
        self.id = user_id
        self.kvorname = kvorname
        self.kname = kname
    
@login_manager.user_loader
def load_user(user_id):                 # wird von Flask-Login verwendet, um einen Benutzer anhand seiner user_id zu laden
    conn = get_db_connection()
    user_data = conn.execute('SELECT * FROM KundenAccount WHERE kundenNr = ?', (user_id,)).fetchone()
    conn.close()

    if user_data:
        user = User(user_id=user_data['kundenNr'], kvorname=user_data['kvorname'], kname=user_data['kname'])
        return user
    return None

def valid_login(kname, kpasswort):
    conn = get_db_connection()
    user_data = conn.execute('SELECT * FROM KundenAccount WHERE kname = ? AND kpasswort = ?', (kname, kpasswort)).fetchone()
    conn.close()

    if user_data:
        user = User(user_id=user_data['kundenNr'], kvorname=user_data['kvorname'], kname=user_data['kname'])
        login_user(user)
        return user

    return None

@app.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user = valid_login(request.form['kname'], request.form['kpasswort'])
        if user:
            login_user(user)
            flash('Login erfolgreich!!')
            return redirect(url_for('input_postleitzahl'))

        flash('Login fehlgeschlagen. Überprüfen Sie Vorname, Name und Passwort.', 'danger')

    return render_template('login.html')

#login restaurant
class Restaurant(UserMixin):
    def __init__(self, restaurant_id, Name, Passwort):
        self.id = restaurant_id
        self.Name = Name
        self.Passwort = Passwort

@login_manager.user_loader
def load_user(restaurant_id):
    conn = get_db_connection()
    restaurant_data = conn.execute('SELECT * FROM RestaurantAccount WHERE restaurant_ID = ?', (restaurant_id,)).fetchone()
    conn.close()

    if restaurant_data:
        restaurant = Restaurant(restaurant_id=restaurant_data['restaurant_ID'], Name=restaurant_data['Name'], Passwort=restaurant_data['Passwort'])
        return restaurant
    return None

def valid_login2(Name, Passwort):
    conn = get_db_connection()
    restaurant_data = conn.execute('SELECT * FROM RestaurantAccount WHERE Name = ? AND Passwort = ?', (Name, Passwort)).fetchone()
    conn.close()

    if restaurant_data:
        restaurant = Restaurant(restaurant_id=restaurant_data['restaurant_ID'], Name=restaurant_data['Name'], Passwort=restaurant_data['Passwort'])
        return restaurant

    return None

@app.route('/login2/', methods=('GET', 'POST'))
def login2():
    if request.method == 'POST':
        restaurant = valid_login2(request.form['Name'], request.form['Passwort'])
        if restaurant:
            login_user(restaurant)
            flash('Login erfolgreich!','success')
            return redirect(url_for('restaurant_dashboard'))
        flash('Login fehlgeschlagen. Überprüfen Sie den Namen und  das Passwort.', 'danger')
    return render_template('login2.html')


@app.route('/logout/')  
@login_required
def logout():
    session.pop('cart', None)  # Efface le contenu du Warenkorb apres un logout
    logout_user()
    flash('Sie wurden abgemeldet.', 'success')     #success est juste un attribut et est optional
    return redirect(url_for('index'))

def get_current_weekday():
    # aktuellen Wochentag als Integer bekommen (Montag ist 0 und Sonntag ist 6)
    current_weekday_int = datetime.now().weekday()

    # Integer auf den entsprechenden Wochentag mappen
    weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
    current_weekday_str = weekdays[current_weekday_int]

    return current_weekday_str

def get_open_restaurants_by_postcode(postleitzahl):
    current_time = datetime.now().strftime('%H:%M:%S')
    
    conn = get_db_connection()
    restaurants = conn.execute('''
        SELECT * 
        FROM Lieferradius 
        JOIN RestaurantAccount ON Lieferradius.restaurant_ID = RestaurantAccount.restaurant_ID 
        JOIN Oeffnungszeiten ON Lieferradius.restaurant_ID = Oeffnungszeiten.restaurant_ID
        WHERE Lieferradius.postleitzahl = ? 
        AND ? BETWEEN Oeffnungszeiten.oeffnet_ab AND Oeffnungszeiten.schliesst_um
        AND Oeffnungszeiten.Tag = ?  -- Fügen Sie hier den aktuellen Wochentag hinzu
    ''', (postleitzahl, current_time, get_current_weekday())).fetchall()

    conn.close()
    return restaurants


@login_required
@app.route('/restaurants/')
def show_restaurants():
    postleitzahl = session.get('user_postleitzahl')
    MyPost=['40421','40432','62789','39478','50503','54178','25147','28963','45479']
    if not postleitzahl:
        flash('Bitte geben Sie zuerst Ihre Postleitzahl ein.', 'warning')
        return redirect(url_for('input_postleitzahl'))
    elif postleitzahl not in MyPost:
        flash('Momentan liefern wir leider nicht zu diesem Postleitzahl', 'warning')
        return redirect(url_for('input_postleitzahl'))

    restaurants = get_open_restaurants_by_postcode(postleitzahl)
    if  not restaurants :
        flash('Es sind zur Zeit kein Restaurant  geöffnet, das zu dir liefern kann! Vielleicht erneut später versuchen?')
        return redirect(url_for('input_postleitzahl'))
    else :
        return render_template('restaurants.html', restaurants=restaurants)

@app.route('/input_postleitzahl', methods=('GET', 'POST'))
@login_required
def input_postleitzahl():
    if request.method == 'POST':
        postleitzahl = request.form['postleitzahl']
        session['user_postleitzahl'] = postleitzahl  # Store the Postleitzahl in the session
        return redirect(url_for('show_restaurants'))

    return render_template('input_postleitzahl.html')

#affichage de la page d'accueil du restaurant
@app.route('/restaurant_dashboard')
@login_required
def restaurant_dashboard():
    # notwendigen Daten für das Dashboard holen
    conn = get_db_connection()
    restaurant = conn.execute('SELECT * FROM RestaurantAccount WHERE restaurant_ID = ?', (current_user.id,)).fetchone()
    vorspeisen = conn.execute('SELECT * FROM Vorspeisen WHERE restaurant_ID = ?', (current_user.id,)).fetchall()
    hauptgerichte = conn.execute('SELECT * FROM Hauptgericht WHERE restaurant_ID = ?', (current_user.id,)).fetchall()
    nachtisch = conn.execute('SELECT * FROM Nachtisch WHERE restaurant_ID = ?', (current_user.id,)).fetchall()
    getraenke = conn.execute('SELECT * FROM Getraenke WHERE restaurant_ID = ?', (current_user.id,)).fetchall()
    conn.close()

    return render_template('restaurant_dashboard.html', restaurant=restaurant, vorspeisen=vorspeisen, hauptgerichte=hauptgerichte,nachtisch=nachtisch, getraenke=getraenke)

@app.route('/edit_dish/<category>/<int:dish_id>', methods=['GET', 'POST'])
@login_required
def edit_dish(category, dish_id):
    try:
        conn = get_db_connection()

        if request.method == 'POST':
            # Daten aus dem Formular erhalten
            new_name = request.form.get('new_name')
            new_beschreibung = request.form.get('new_beschreibung')
            new_preis = request.form.get('new_preis')

            update_dish(conn, category, dish_id, new_name, new_beschreibung, new_preis)

            conn.commit()
            flash('Gericht aktualisiert.', 'success')
            return redirect(url_for('restaurant_dashboard'))

        # Überprüfe, ob die übergebene Kategorie gültig ist
        possible_tables = ['Vorspeisen', 'Hauptgericht', 'Nachtisch', 'Getraenke']
        if category not in possible_tables:
            flash('Ungültige Kategorie.', 'danger')
            return redirect(url_for('restaurant_dashboard'))

        # Verwende den spezifischen Schlüssel für jede Kategorie (VID, HID, NID, GID)
        key_column = f'{category[0]}ID'  # z.B., 'VID' für Vorspeisen
        dish = dict(conn.execute(f'SELECT * FROM {category} WHERE {key_column}=?', (dish_id,)).fetchone())
        if dish:
            return render_template('edit_dish.html', dish=dish, category=category)

        flash('Gericht nicht gefunden.', 'danger')
        return redirect(url_for('restaurant_dashboard'))
    finally:
        if conn:
            conn.close()

def update_dish(conn, category, dish_id, new_name, new_beschreibung, new_preis):
    key_column = f'{category[0]}ID'
    update_query = f'UPDATE {category} SET {category[0]}Name=?, {category[0]}Beschreibung=?, {category[0]}Preis=? WHERE {key_column}=?'
    conn.execute(update_query, (new_name, new_beschreibung, new_preis, dish_id))


@app.route('/delete_dish/<category>/<int:dish_id>', methods=['POST'])
@login_required
def delete_dish(category, dish_id):
    try:
        conn = get_db_connection()

        # Überprüfe, ob die übergebene Kategorie gültig ist
        possible_tables = ['Vorspeisen', 'Hauptgericht', 'Nachtisch', 'Getraenke']
        if category not in possible_tables:
            flash('Ungültige Kategorie.', 'danger')
            return redirect(url_for('restaurant_dashboard'))

        # Verwende den spezifischen Schlüssel für jede Kategorie (VID, HID, NID, GID)
        key_column = f'{category[0]}ID'  # z.B., 'VID' für Vorspeisen

        conn.execute(f'DELETE FROM {category} WHERE {key_column}=?', (dish_id,))     # Gericht aus der Datenbank löschen


        conn.commit()
        flash('Gericht entfernt.', 'success')
        return redirect(url_for('restaurant_dashboard'))

    except Exception as e:
        flash('Fehler beim Löschen des Gerichts.', 'danger')
        return redirect(url_for('restaurant_dashboard'))

    finally:
        if conn:
            conn.close()

@app.route('/add_dish/<category>/<int:restaurant_id>', methods=['GET', 'POST'])
def add_dish(category, restaurant_id):
    if request.method == 'POST':
        # Daten aus dem Formular erhalten
        name = request.form['name']
        beschreibung = request.form['beschreibung']
        preis = request.form['preis']
        bild = request.files['bild']

        # Sicherstellen, dass das Bild sicher hochgeladen wird
        if bild:
            secure_bild = secure_filename(bild.filename)
            bild.save(os.path.join('static/', secure_bild))  # Das Bild im 'static/uploads'-Ordner speichern

        # Datenbankverbindung herstellen und Datensatz einfügen
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Überprüfe, ob die übergebene Kategorie gültig ist
            possible_tables = ['Vorspeisen', 'Hauptgericht', 'Nachtisch', 'Getraenke']
            if category not in possible_tables:
                flash('Ungültige Kategorie.', 'danger')
                return redirect(url_for('restaurant_dashboard'))

            # Spaltennamen dynamisch basierend auf der Kategorie zusammenstellen
            columns = {
                'Vorspeisen': ('VName', 'VBeschreibung', 'VPreis', 'VBild', 'restaurant_ID'),
                'Hauptgericht': ('HName', 'HBeschreibung', 'HPreis', 'HBild', 'restaurant_ID'),
                'Nachtisch': ('NName', 'NBeschreibung', 'NPreis', 'NBild', 'restaurant_ID'),
                'Getraenke': ('GName', 'GBeschreibung', 'GPreis', 'GBild', 'restaurant_ID')
            }

            column_names = columns[category]

            # SQL-Query zum Einfügen des Datensatzes
            query = f"INSERT INTO {category} ({', '.join(column_names)}) VALUES ({', '.join(['?'] * len(column_names))})"    #len(column_names) verwendet, um dynamisch die Anzahl der Platzhalter in der SQL-Abfrage zu bestimmen, basierend auf der Anzahl der Spalten in der Tabelle, in die Daten eingefügt werden sollen
            
            # Parameter für die SQL-Abfrage zusammenstellen
            params = (name, beschreibung, preis, secure_bild, restaurant_id)

            cursor.execute(query, params)
            conn.commit()

            flash('Gericht erfolgreich hinzugefügt.', 'success')
            return redirect(url_for('restaurant_dashboard'))

        except Exception as e:
            flash(f'Fehler beim Hinzufügen des Gerichts: {str(e)}', 'danger')
            return redirect(url_for('restaurant_dashboard'))

        finally:
            conn.close()

    # Hier Restaurantinformationen abrufen und als Kontext für das Template bereitstellen
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM RestaurantAccount WHERE restaurant_ID = ?"
    cursor.execute(query, (restaurant_id,))
    restaurant = cursor.fetchone()
    conn.close()
    restaurant_dict = dict(zip([desc[0] for desc in cursor.description], restaurant))    
    return render_template('add_dish.html', category=category, restaurant=restaurant_dict)


@app.route('/restaurant_detail/<int:restaurant_id>/')
@login_required
def restaurant_details(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant is None:
        abort(404)

    vorspeisen = get_dishes_by_category(restaurant_id, 'Vorspeisen')
    Hauptgericht = get_dishes_by_category(restaurant_id, 'Hauptgericht')
    Nachtisch = get_dishes_by_category(restaurant_id, 'Nachtisch')
    getraenke = get_dishes_by_category(restaurant_id, 'Getraenke')

    return render_template('restaurant_details.html', restaurant=restaurant, vorspeisen=vorspeisen, Hauptgericht=Hauptgericht, Nachtisch=Nachtisch, getraenke=getraenke)

def get_dishes_by_category(restaurant_id, category):
    conn = get_db_connection()
    # Überprüfen Sie den Tabellennamen und die Spaltennamen in Ihrer Datenbank
    dishes = conn.execute('SELECT * FROM {} WHERE restaurant_ID = ?'.format(category), (restaurant_id,)).fetchall()
    conn.close()
    return dishes

def get_restaurant_by_id(restaurant_id):
    conn = get_db_connection()
    restaurant = conn.execute('SELECT * FROM RestaurantAccount WHERE restaurant_ID = ?', (restaurant_id,)).fetchone()
    conn.close()
    return restaurant


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        # Access the session object within the context of the request
        if 'cart' not in session:
            session['cart'] = []

    # die aus dem Formular erhaltenen Artikel dem Warenkorb hinzufügen  
    item_name = request.form['item_name']
    item_price = float(request.form['item_price'])
    quantity = int(request.form['quantity'])
    total_price = item_price * quantity

    # Element zum Warenkorb hinzufügen
    session['cart'].append({
        'item_name': item_name,
        'quantity': quantity,
        'item_price': item_price,
        'total_price': total_price
    })

    flash(f'{quantity} x {item_name} wurde zum Warenkorb hinzugefügt.', 'success')
    return redirect(request.referrer) # pour rester sur la meme page

@app.route('/show_cart/<int:restaurant_id>/')
def show_cart(restaurant_id):
    cart = session.get('cart', [])
    total_price = sum(item['total_price'] for item in cart)
    conn = get_db_connection()
    restaurant = conn.execute('SELECT * FROM RestaurantAccount WHERE restaurant_ID = ?', (restaurant_id,)).fetchone()
    if restaurant is None:
        abort(404)
    return render_template('cart.html', cart=cart, total_price=total_price,restaurant=restaurant)


@app.route('/remove_from_cart/<int:restaurant_id>/<string:item_name>/', methods=['POST'])
def remove_from_cart(restaurant_id, item_name):
    # Récupérer le panier de la session
    cart = session.get('cart', [])

    # Parcourir le panier pour trouver l'article à supprimer
    for item in cart:
        if item['item_name'] == item_name:
            cart.remove(item)
            break

    # Mettre à jour le panier dans la session
    session['cart'] = cart

    # Rediriger l'utilisateur vers la page du panier
    return redirect(url_for('show_cart', restaurant_id=restaurant_id))


def calculate_total_price(cart):
    total_price1 = sum(item['total_price']  for item in cart)
    return total_price1 

@app.route('/submit_order', methods=['POST'])
@login_required
def submit_order():
   
    if request.method == 'POST':
        restaurant_name = request.form.get('restaurant_name')
        kundenNr = current_user.id
        Anmerkung = request.form['anmerkung']       
        current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        current_cart = session['cart']  # Annahme: session['cart'] enthält die aktuellen Warenkorbdaten
        total_price = calculate_total_price(current_cart)

        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            restaurant_id=conn.execute('SELECT restaurant_ID FROM RestaurantAccount WHERE Name=?',(restaurant_name,)).fetchone()[0]
            Adresse= conn.execute('SELECT kadresse FROM KundenAccount WHERE kundenNr=?',(current_user.id,)).fetchone()[0]
            
            cursor.execute("INSERT INTO Bestellung (created,gesamtpreis, restaurant_ID,restName, kundenNr,kundenAdr,anmerkung,status) VALUES (?, ?, ?, ?, ?,?, ?,?)", (current_time,total_price, restaurant_id,restaurant_name, kundenNr,Adresse, Anmerkung,"In Bearbeitung"))
            bestellNr = cursor.lastrowid  # Die zuletzt eingefügte Bestellnummer abrufen

            # Insertion dans la Table Items pour chaque Article commandé
            for item in session['cart']:
                iName=item['item_name']
                cursor.execute("INSERT INTO Items (anzahl, preis,created, bestellNr,kundenNr,itemName) VALUES (?, ?, ?, ?, ?, ?)", (item['quantity'], item['total_price'],current_time, bestellNr,kundenNr,iName))

            conn.commit()
            flash( "Bestellung erfolgreich aufgegeben!")
            session['cart'] = []  #Vider la corbeille apres avoir passé une commande
            socketio.emit('new_order', {'message': 'Sie haben eine neue Bestellung !!'}, namespace='/restaurants')
            return redirect(url_for('show_restaurants'))
        
        except Exception as e:
            conn.rollback()  # Bei einem Fehler Transaktion rückgängig machen
            return "Fehler beim Aufgeben der Bestellung: " + str(e)
        
        finally:conn.close()

    return render_template('cart.html')  

##gesamt Übersicht
@app.route('/user_order_history0')
@login_required
def user_order_history0():
    # Logique pour récupérer l'historique des commandes de l'utilisateur
    user_id = current_user.id
    user_order_history = get_user_order_history0(user_id)
    return render_template('Bestellung.html', user_order_history=user_order_history)

def get_user_order_history0(user_id):
    conn = get_db_connection()
    user_order_history = conn.execute('SELECT * FROM Bestellung WHERE kundenNr = ?  ORDER BY created DESC', (user_id,)).fetchall()
    conn.close()
    return user_order_history

##In bearbeitung
@app.route('/user_order_history')
@login_required
def user_order_history():
    # Logique pour récupérer l'historique des commandes de l'utilisateur
    user_id = current_user.id
    user_order_history = get_user_order_history(user_id)
    return render_template('Bestellung.html', user_order_history=user_order_history)

def get_user_order_history(user_id):
    conn = get_db_connection()
    user_order_history = conn.execute('SELECT * FROM Bestellung WHERE kundenNr = ? AND STATUS= ? ORDER BY created DESC', (user_id,'In Bearbeitung')).fetchall()
    conn.close()
    return user_order_history

##In Zubereitung
@app.route('/user_order_history2')
@login_required
def user_order_history2():
    # Logique pour récupérer l'historique des commandes de l'utilisateur
    user_id = current_user.id
    user_order_history = get_user_order_history2(user_id)
    return render_template('Bestellung.html', user_order_history=user_order_history)

def get_user_order_history2(user_id):
    conn = get_db_connection()
    user_order_history = conn.execute('SELECT * FROM Bestellung WHERE kundenNr = ? AND STATUS= ? ORDER BY created DESC', (user_id,'In Zubereitung')).fetchall()
    conn.close()
    return user_order_history

##Abgeschlossen
@app.route('/user_order_history3')
@login_required
def user_order_history3():
    # Logique pour récupérer l'historique des commandes de l'utilisateur
    user_id = current_user.id
    user_order_history = get_user_order_history3(user_id)
    return render_template('Bestellung.html', user_order_history=user_order_history)

def get_user_order_history3(user_id):
    conn = get_db_connection()
    user_order_history = conn.execute('SELECT * FROM Bestellung WHERE kundenNr = ? AND STATUS= ? ORDER BY created DESC', (user_id,'Abgeschlossen')).fetchall()
    conn.close()
    return user_order_history

##Storniert
@app.route('/user_order_history4')
@login_required
def user_order_history4():
    # Logique pour récupérer l'historique des commandes de l'utilisateur
    user_id = current_user.id
    user_order_history = get_user_order_history4(user_id)
    return render_template('Bestellung.html', user_order_history=user_order_history)

def get_user_order_history4(user_id):
    conn = get_db_connection()
    user_order_history = conn.execute('SELECT * FROM Bestellung WHERE kundenNr = ? AND STATUS= ? ORDER BY created DESC', (user_id,'Storniert')).fetchall()
    conn.close()
    return user_order_history

#################################################
#general history of Restaurant
@app.route('/restaurant/orders')
@login_required
def restaurant_orders():
    # Logik, um dem Restaurant neue Bestellungen anzuzeigen
    new_orders = get_new_orders_for_restaurant(current_user.id)
    return render_template('restaurant_orders.html', new_orders=new_orders)

def get_new_orders_for_restaurant(restaurant_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Logik, um dem Restaurant neue Bestellungen anzuzeigen
        cursor.execute('SELECT * FROM Bestellung WHERE restaurant_ID = ?  ORDER BY created DESC ', (restaurant_id,))

        new_orders = cursor.fetchall()
        return new_orders

    finally:
        conn.close()

@app.route('/view_orders')
def view_orders():
    bestellNr = request.args.get('bestellNr')
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM Items WHERE BestellNr = ?', (bestellNr,))
    orders= cursor.fetchall()
    return render_template('view_orders.html', orders=orders)

#In Bearbeitung
@app.route('/restaurant/orders2')
@login_required
def restaurant_orders2():
    # Logik, um dem Restaurant neue Bestellungen anzuzeigen
    new_orders = get_new_orders_for_restaurant2(current_user.id)
    return render_template('restaurant_order_history.html', new_orders=new_orders)

def get_new_orders_for_restaurant2(restaurant_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Logik, um dem Restaurant neue Bestellungen anzuzeigen
        cursor.execute('SELECT * FROM Bestellung WHERE restaurant_ID = ? AND status = ? ORDER BY created DESC', (restaurant_id,'In Bearbeitung'))
        new_orders = cursor.fetchall()
        return new_orders

    finally:
        conn.close()

#In Zubereitung
@app.route('/restaurant/orders3')
@login_required
def restaurant_orders3():
    # Logik, um dem Restaurant neue Bestellungen anzuzeigen
    new_orders = get_new_orders_for_restaurant3(current_user.id)
    return render_template('restaurant_orderEND.html', new_orders=new_orders)

def get_new_orders_for_restaurant3(restaurant_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Logik, um dem Restaurant neue Bestellungen anzuzeigen
        cursor.execute('SELECT * FROM Bestellung WHERE restaurant_ID = ? AND status = ? ORDER BY created DESC', (restaurant_id,'In Zubereitung'))
        new_orders = cursor.fetchall()
        return new_orders

    finally:
        conn.close()

#Abgeschlossen
@app.route('/restaurant/orders4')
@login_required
def restaurant_orders4():
    # Logik, um dem Restaurant neue Bestellungen anzuzeigen
    new_orders = get_new_orders_for_restaurant4(current_user.id)
    return render_template('restaurant_order_ABG.html', new_orders=new_orders)

def get_new_orders_for_restaurant4(restaurant_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Logik, um dem Restaurant neue Bestellungen anzuzeigen
        cursor.execute('SELECT * FROM Bestellung WHERE restaurant_ID = ? AND status = ? ORDER BY created DESC', (restaurant_id,'Abgeschlossen'))
        new_orders = cursor.fetchall()
        return new_orders

    finally:
        conn.close()

#storniert
@app.route('/restaurant/orders5')
@login_required
def restaurant_orders5():
    # Logik, um dem Restaurant neue Bestellungen anzuzeigen
    new_orders = get_new_orders_for_restaurant5(current_user.id)
    return render_template('restaurant_order_ABG.html', new_orders=new_orders)

def get_new_orders_for_restaurant5(restaurant_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Logik, um dem Restaurant neue Bestellungen anzuzeigen
        cursor.execute('SELECT * FROM Bestellung WHERE restaurant_ID = ? AND status = ? ORDER BY created DESC', (restaurant_id,'Storniert'))
        new_orders = cursor.fetchall()
        return new_orders

    finally:
        conn.close()

############################################
@app.route('/restaurant/confirm_order/<int:order_id>/', methods=['POST'])
@login_required
def restaurant_confirm_order(order_id):
    # Hier die Bestellung in der Datenbank bestätigen und den Status auf "in Zubereitung" setzen
    conn = get_db_connection()
    conn.execute('UPDATE Bestellung SET status = ? WHERE bestellNr = ?', ('In Zubereitung', order_id))
    conn.commit()
    conn.close()

    flash('Bestellung bestätigt und wird zubereitet.', 'success')
    socketio.emit('new_order', {'message': 'Ihre bestellung wurde bestätigt!!'}, namespace='/restaurants')
    return redirect(url_for('restaurant_orders3'))

@app.route('/restaurant/reject_order/<int:order_id>/', methods=['POST'])
@login_required
def restaurant_reject_order(order_id):
    # Hier die Bestellung in der Datenbank ablehnen und den Status auf "storniert" setzen
    conn = get_db_connection()
    conn.execute('UPDATE Bestellung SET status = ? WHERE bestellNr = ?', ('Storniert', order_id))
    conn.commit()
    conn.close()

    flash('Bestellung wurde abgelehnt.', 'info')
    socketio.emit('new_order', {'message': 'Ihre bestellung wurde abgelehnt!!'}, namespace='/restaurants')
    return redirect(url_for('restaurant_orders'))

@app.route('/restaurant/end_order/<int:order_id>/', methods=['POST'])
@login_required
def restaurant_end_order(order_id):
    # Hier die Bestellung in der Datenbank ablehnen und den Status auf "storniert" setzen
    conn = get_db_connection()
    conn.execute('UPDATE Bestellung SET status = ? WHERE bestellNr = ?', ('Abgeschlossen', order_id))
    conn.commit()
    conn.close()

    flash('Bestellung abgeschlossen.', 'info')
    socketio.emit('new_order', {'message': 'Ihre bestellung wurde versendet!!'}, namespace='/restaurants')
    return redirect(url_for('restaurant_orders4'))


if __name__ == '__main__':
    #app.run(debug=True)
    socketio.run(app)