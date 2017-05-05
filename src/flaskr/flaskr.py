import os
from flask import Flask, url_for, render_template, session, escape, request, redirect
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = os.path.join(BASE_DIR, '../../databases/db.sqlite3'),
DEBUG = True
SECRET_KEY = 'AMNAS@#(@#9===ASKDj)KAS=/ASDKK(@(#KDASDJKAAAL)@(I@#U))'

USERNAME = 'admin'
PASSWORD = 'incorrect'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    else:
        return 'You are not logged in \n ps: I KNOW WHO YOU ARE %s' % (session.get('username','Daniel'))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return '''
            <form action='' method='POST'>
                <p><input type=text name=username></p>
                <p><input type=submit value=Login></p>
            <form>
        '''

@app.route('/logout', methods=["GET"])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('flaskr/hello.html', name=name)

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects')
def projects():
    return 'The projects page'

@app.route('/about')
def about():
    return 'The projects page'


#with app.test_request_context():
#    print url_for('index')
#    print url_for('login')
#    print url_for('login', next='/')
#    print url_for('profile', username='DANIEL KIM')

if __name__ == "__main__":
    app.run(debug=True)
