from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Securely generate a secret key

# Dummy user data (for demonstration)
users = {'user1@example.com': {'dob': '01-01-1990', 'password': 'password1'}}

@app.route('/')
def home():
    if 'username' in session:
        return f'Logged in as {session["username"]} <br><a href="/logout">Logout</a>'
    return 'You are not logged in <br><a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            if username in users and users[username]['password'] == password:
                session['username'] = username
                return redirect(url_for('home'))
            else:
                return 'Invalid username/password combination'
        else:
            return 'Please provide both username and password'
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            users[email] = {'password': password}
            return redirect(url_for('login'))
        else:
            return 'Please fill in all details'
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
