from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm

# Use render template for rendering the html pages.
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ATApePBVzvG8U438SDzzbtJtPkTT8Jfk'

posts_list = [
    {
        'author': 'Roshan Gardi',
        'title': 'Blog Post1',
        'content': 'My content',
        'date': 'Sep 21 2020'
    },
    {
        'author': 'James Pitt',
        'title': 'Blog Post2',
        'content': 'My content',
        'date': 'Sep 22 2020'
    }
]

@app.route('/')  # when opened main page it will go to below function
@app.route('/home')  # can use multiple routes for single function
def home():
    # return '<h2>Home Page</h2>'  # instead of inline html tags, use template html files
    return render_template('home.html', posts=posts_list)

@app.route('/about')
def about():
    # return '<h1>About details coming soon!</h1>'
    return render_template('about.html',title='About')

if __name__ == "__main__":
    #Run the flask application by calling run on the object
    app.run(debug=True)  # we set debug=True so that whenever we make any new changes in file, we don't have to restart
    # the server for them to take effect
