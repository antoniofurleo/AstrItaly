from flask import Flask, render_template, redirect, request, session, flash, send_file
import secrets
import hashlib
import sqlite3

app = Flask(__name__)
app.permanent_session_lifetime = 604800
app.secret_key = secrets.token_hex(32)
db_path = 'database.db'

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "":
            flash('Username or password undefined')
            return redirect('/register')
        if password == "":
            flash('Username or password undefined')
            return redirect('/register')
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT id FROM users WHERE username=?', (username,))
        user = cursor.fetchone()
        if user is not None:
            flash('Username already existing, choose another one')
            connection.close()
            return redirect('/register')

        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        connection.commit()
        connection.close()
        return redirect('/login')
    return render_template('register.html')

@app.route('/question111')
def question111():
    user_id = session.get('user_id')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT question111 FROM users WHERE id = ?', (user_id,))
    question = cursor.fetchone()[0]
    if not question:
        cursor.execute('UPDATE users SET score = score + ? WHERE id = ?', (0.5, user_id))
        cursor.execute('UPDATE users SET question111 = TRUE WHERE id = ?', (user_id,))
        connection.commit()
    connection.close() 
    return 0

@app.route('/question110')
def question110():
    user_id = session.get('user_id')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT question110 FROM users WHERE id = ?', (user_id,))
    question = cursor.fetchone()[0]
    if not question:
        cursor.execute('UPDATE users SET score = score + ? WHERE id = ?', (0.5, user_id))
        cursor.execute('UPDATE users SET question110 = TRUE WHERE id = ?', (user_id,))
        connection.commit()
    connection.close() 
    return 0

@app.route('/question130')
def question130():
    user_id = session.get('user_id')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT question130 FROM users WHERE id = ?', (user_id,))
    question = cursor.fetchone()[0]
    if not question:
        cursor.execute('UPDATE users SET score = score + ? WHERE id = ?', (0.5, user_id))
        cursor.execute('UPDATE users SET question130 = TRUE WHERE id = ?', (user_id,))
        connection.commit()
    connection.close() 
    return 0

@app.route('/question131')
def question():
    user_id = session.get('user_id')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT question131 FROM users WHERE id = ?', (user_id,))
    question = cursor.fetchone()[0]
    if not question:
        cursor.execute('UPDATE users SET score = score + ? WHERE id = ?', (0.5, user_id))
        cursor.execute('UPDATE users SET question131 = TRUE WHERE id = ?', (user_id,))
        connection.commit()
    connection.close() 
    return 0

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT id FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        connection.close()
        if user is not None:
            session['user_id'] = user[0]
            session.permanent = True 
            return redirect('/')
        else:
            flash('Incorrect username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')

@app.route('/leaderboard', methods=('GET',))
def leaderboard():
    user_id = session.get('user_id')
    if not user_id:
        user_id = None
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    if user_id is not None:
        cursor.execute('SELECT username FROM users WHERE id=?', (user_id,))
        user_id = str(user_id).zfill(4)
        user1 = cursor.fetchone()
    cursor.execute('SELECT username, score FROM users ORDER BY score DESC')
    users = cursor.fetchall()
    print(users)
    connection.close()
    try:
        user = user1[0]
    except:
        user=""
    return render_template('leaderboard.html', session_id=user_id, user=user, users=users)

@app.route('/')
def index():
    user_id = session.get('user_id')
    if not user_id:
        user_id = None
    if user_id is not None:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT username FROM users WHERE id=?', (user_id,))
        user_id = str(user_id).zfill(4)
        user1 = cursor.fetchone()
        connection.close()
    try:
        user = user1[0]
    except:
        user=""
    return render_template('index.html', session_id=user_id, user=user)

@app.route('/sdg11')
def sdg11():
    user_id = session.get('user_id')
    if not user_id:
        user_id = None
    if user_id is not None:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT username FROM users WHERE id=?', (user_id,))
        user_id = str(user_id).zfill(4)
        user1 = cursor.fetchone()
        connection.close()
    try:
        user = user1[0]
    except:
        user=""
    return render_template('sdg11.html', session_id=user_id, user=user)

@app.route('/sdg13')
def sdg13():
    user_id = session.get('user_id')
    if not user_id:
        user_id = None
    if user_id is not None:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT username FROM users WHERE id=?', (user_id,))
        user_id = str(user_id).zfill(4)
        user1 = cursor.fetchone()
        connection.close()
    try:
        user = user1[0]
    except:
        user=""
    return render_template('sdg13.html', session_id=user_id, user=user)