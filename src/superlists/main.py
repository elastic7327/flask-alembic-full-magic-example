from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        do_the_login()
    else:
        show_the_login_form()

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('superlists/hello.html', name=name)

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


with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='DANIEL KIM')

if __name__ == "__main__":
    app.run(debug=True)
