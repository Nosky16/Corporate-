# ecn_corporative_app.py

from flask import Flask, render_template, request, redirect, session, g
import sqlite3
from datetime import datetime, timedelta
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key in production
DATABASE = 'ecn_coop.db'  # SQLite database file

# Connect to the database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

# Close the database connection after each request
@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db:
        db.close()

# Decorator to ensure the user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

# Redirect the root URL to login
@app.route('/')
def index():
    return redirect('/login')

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        db = get_db()
        cursor = db.execute('SELECT id, is_admin FROM users WHERE name=?', (name,))
        user = cursor.fetchone()
        if user:
            # Save user info in session
            session['user_id'] = user[0]
            session['is_admin'] = user[1]
            return redirect('/dashboard')
        else:
            return 'User not found'
    return render_template('login.html')

# Main dashboard after login
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
    total = sum([row[0] for row in savings])  # Calculate total savings
    return render_template('savings.html', savings=savings, total=total)

# Apply for a loan and view loan history
@app.route('/loan', methods=['GET', 'POST'])
@login_required
def loan():
    db = get_db()
    user_id = session['user_id']
    if request.method == 'POST':
        amount = int(request.form['amount'])  # Loan amount
        duration = int(request.form['duration'])  # Repayment duration in months
        monthly = round(amount / duration, 2)  # Monthly repayment amount
        today = datetime.now()
        # Insert loan request into database
        db.execute('INSERT INTO loans (user_id, amount, duration, monthly_repayment, date, status) VALUES (?, ?, ?, ?, ?, ?)',
                   (user_id, amount, duration, monthly, today.strftime('%Y-%m-%d'), 'pending'))
        db.commit()
    # Retrieve loan history for the user
    cursor = db.execute('SELECT * FROM loans WHERE user_id=?', (user_id,))
    loans = cursor.fetchall()
    return render_template('loan.html', loans=loans)

# Display repayment schedule for approved loans
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
        # Generate monthly due dates
        for i in range(duration):
            due_date = (start_date + timedelta(days=30*i)).strftime('%Y-%m-%d')
            repayments.append((due_date, monthly, 0))  # 0 = unpaid (display only)
    return render_template('repayments.html', repayments=repayments)

# Admin dashboard
@app.route('/admin')
@login_required
def admin():
    if not session.get('is_admin'):
        return redirect('/dashboard')
    return render_template('admin.html')

# Admin: Add savings for any user
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

# Admin: View all users
@app.route('/users')
@login_required
def users():
    if not session.get('is_admin'):
        return redirect('/dashboard')
    db = get_db()
    cursor = db.execute('SELECT id, name FROM users')
    users = cursor.fetchall()
    return render_template('users.html', users=users)

# Admin: View pending loan approvals
@app.route('/approve_loans')
@login_required
def approve_loans():
    if not session.get('is_admin'):
        return redirect('/dashboard')
    db = get_db()
    cursor = db.execute('SELECT id, user_id, amount FROM loans WHERE status = "pending"')
    loans = cursor.fetchall()
    return render_template('approve_loans.html', loans=loans)

# Admin: Approve a specific loan
@app.route('/approve/<int:loan_id>')
@login_required
def approve(loan_id):
    if not session.get('is_admin'):
        return redirect('/dashboard')
    db = get_db()
    db.execute('UPDATE loans SET status = "approved" WHERE id = ?', (loan_id,))
    db.commit()
    return redirect('/approve_loans')

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
