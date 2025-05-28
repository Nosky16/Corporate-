# ecn_corporative_app.py

from flask import Flask, render_template, request, redirect, session, g
import sqlite3
from datetime import datetime, timedelta
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'ecn_coop.db'

# Connect to SQLite database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

# Close DB connection after each request
@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db:
        db.close()

# Restrict access to logged-in users
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

# Redirect root to login
@app.route('/')
def index():
    return redirect('/login')

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        is_admin = int(request.form.get('is_admin', 0))  # Default to 0 (staff)
        db = get_db()
        # Check if user already exists
        cursor = db.execute('SELECT id FROM users WHERE name=?', (name,))
        if cursor.fetchone():
            return 'User already exists. Please log in.'
        # Insert new user into the database
        db.execute('INSERT INTO users (name, is_admin) VALUES (?, ?)', (name, is_admin))
        db.commit()
        return redirect('/login')
    return render_template('register.html')

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        db = get_db()
        cursor = db.execute('SELECT id, is_admin FROM users WHERE name=?', (name,))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            session['is_admin'] = user[1]
            return redirect('/dashboard')
        else:
            return 'User not found. Please register first.'
    return render_template('login.html')

# Dashboard after login
@app.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    user_id = session['user_id']
    cursor = db.execute('SELECT name FROM users WHERE id=?', (user_id,))
    name = cursor.fetchone()[0]
    return render_template('dashboard.html', name=name, is_admin=session.get('is_admin'))

# View savings
@app.route('/savings')
@login_required
def savings():
    db = get_db()
    user_id = session['user_id']
    cursor = db.execute('SELECT amount, date FROM savings WHERE user_id=?', (user_id,))
    savings = cursor.fetchall()
    total = sum([row[0] for row in savings])
    return render_template('savings.html', savings=savings, total=total)

# Apply for and view loans
@app.route('/loan', methods=['GET', 'POST'])
@login_required
def loan():
    db = get_db()
    user_id = session['user_id']
    if request.method == 'POST':
        amount = int(request.form['amount'])
        duration = int(request.form['duration'])
        monthly = round(amount / duration, 2)
        today = datetime.now()
        db.execute('INSERT INTO loans (user_id, amount, duration, monthly_repayment, date, status) VALUES (?, ?, ?, ?, ?, ?)',
                   (user_id, amount, duration, monthly, today.strftime('%Y-%m-%d'), 'pending'))
        db.commit()
    cursor = db.execute('SELECT * FROM loans WHERE user_id=?', (user_id,))
    loans = cursor.fetchall()
    return render_template('loan.html', loans=loans)

# View repayment schedule
@app.route('/repayments')
@login_required
def repayments():
    db = get_db()
    user_id = session['user_id']
    cursor = db.execute('SELECT id, monthly_repayment, duration, date FROM loans WHERE user_id=? AND status="approved"', (user_id,))
    loans = cursor.fetchall()
    repayments = []
    for loan in loans:
        loan_id, monthly, duration, date_str = loan
        start_date = datetime.strptime(date_str, '%Y-%m-%d')
        for i in range(duration):
            due_date = (start_date + timedelta(days=30*i)).strftime('%Y-%m-%d')
            repayments.append((due_date, monthly, 0))  # unpaid
    return render_template('repayments.html', repayments=repayments)

# Admin dashboard
@app.route('/admin')
@login_required
def admin():
    if not session.get('is_admin'):
        return redirect('/dashboard')
    return render_template('admin.html')

# Admin adds savings for users
@app.route('/add_savings', methods=['GET', 'POST'])
@login_required
def add_savings():
    if not session.get('is_admin'):
        return redirect('/dashboard')
    if request.method == 'POST':
        staff_id = request.form['staff_id']
        amount = request.form['amount']
        db = get_db()
        db.execute('INSERT INTO savings (user_id, amount, date) VALUES (?, ?, ?)',
                   (staff_id, amount, datetime.now().strftime('%Y-%m-%d')))
        db.commit()
        return redirect('/add_savings')
    return render_template('add_savings.html')

# Admin views all users
@app.route('/users')
@login_required
def users():
    if not session.get('is_admin'):
        return redirect('/dashboard')
    db = get_db()
    cursor = db.execute('SELECT id, name FROM users')
    users = cursor.fetchall()
    return render_template('users.html', users=users)

# Admin views pending loan approvals
@app.route('/approve_loans')
@login_required
def approve_loans():
    if not session.get('is_admin'):
        return redirect('/dashboard')
    db = get_db()
    cursor = db.execute('SELECT id, user_id, amount FROM loans WHERE status = "pending"')
    loans = cursor.fetchall()
    return render_template('approve_loans.html', loans=loans)

# Admin approves a loan
@app.route('/approve/<int:loan_id>')
@login_required
def approve(loan_id):
    if not session.get('is_admin'):
        return redirect('/dashboard')
    db = get_db()
    db.execute('UPDATE loans SET status = "approved" WHERE id = ?', (loan_id,))
    db.commit()
    return redirect('/approve_loans')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# Initialize the database with required tables
def init_db():
    with sqlite3.connect(DATABASE) as db:
        db.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        is_admin INTEGER NOT NULL DEFAULT 0
                    )''')
        db.execute('''CREATE TABLE IF NOT EXISTS savings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        amount REAL,
                        date TEXT,
                        FOREIGN KEY (user_id) REFERENCES users(id)
                    )''')
        db.execute('''CREATE TABLE IF NOT EXISTS loans (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        amount REAL,
                        duration INTEGER,
                        monthly_repayment REAL,
                        date TEXT,
                        status TEXT,
                        FOREIGN KEY (user_id) REFERENCES users(id)
                    )''')
        db.commit()


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
