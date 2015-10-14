from flask import Flask, render_template, request, make_response
from flask import session
from flask import flash, get_flashed_messages

username = "Guest" # menjace se po potrebi, za sada je po difoltu definisano..

# app is WSGI app
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/tasks')
def tasks():
    response = make_response(render_template('index.html'))
    return response


@app.route('/user/<int:userid>')
def user(userid):
    return '%s' % userid

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == "GET":
        render_template('index.html',name='name')
    elif request.method == "POST":
        print(request.form.items())

if __name__ == '__main__':
    app.run(debug=True)

    # SESSIONS #
    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'