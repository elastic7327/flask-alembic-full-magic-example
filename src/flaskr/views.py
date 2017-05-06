from __future__ import absolute_import
import os
from flask import Flask, url_for, render_template, session, escape, request, redirect
from flaskr import app

#@app.teardown_appcontext
#def shutdown_session(exception=None):
#    db_session.remove()

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

if __name__ == "__main__":
    app.run(debug=True)
