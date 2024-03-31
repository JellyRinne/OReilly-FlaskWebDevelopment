from flask import Flask, request, make_response, redirect
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello, world</h1>\n<p>Your browser is {}.</p>'.format(user_agent)

@app.route('/cookie')
def cookie():
    response = make_response('<p>this document contains a cookie</p>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def redirectpage():
    return redirect('http://github.com')


#or:

#def index():
#    return '<h1>Hello, world</h1>'
#
#app.add_url_rule('/', 'index', index)

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello, old {}!</h1>'.format(name)

app.run(debug=True, host='0.0.0.0', port='8000')