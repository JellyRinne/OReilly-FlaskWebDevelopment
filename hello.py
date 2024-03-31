from flask import Flask, request, make_response, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #chapters 1 & 2
    #user_agent = request.headers.get('User-Agent')
    #return '<h1>Hello, world</h1>\n<p>Your browser is {}.</p>'.format(user_agent)

    #chapter 3
    #3-3
    return render_template('index.html')

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
    #chapters 1 & 2
    #return '<h1> Hello, old {}!</h1>'.format(name)

    #chapter 3
    #3-3
    return render_template('user.html', name=name)

app.run(debug=True, host='0.0.0.0', port='8000')