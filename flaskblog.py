from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2>Aey, Hallo!</h2>'

@app.route('/about')
def rosh_image():
    return '<h1>About details coming soon!</h1>'

if __name__ == "__main__":
    app.run(debug=True)