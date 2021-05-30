from flask import Flask

app = Flask(__name__)


def convert(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


@app.route('/f/<celsius>')
def f(celsius=""):
    return '{} degrees celsius converts to {} degrees fahrenheit'.format(celsius, convert(celsius))


if __name__ == '__main__':
    app.run()
