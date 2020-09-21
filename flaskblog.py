from flask import Flask, render_template

# Use render template for rendering the html pages.
app = Flask(__name__)
posts_list = [
    {
        'author': 'Roshan Gardi',
        'title': 'First Blog Post',
        'content': 'My content',
        'date': 'September 21 2020'
    },
    {
        'author': 'James Pitt',
        'title': 'Second Blog Post',
        'content': 'My content',
        'date': 'September 22 2020'
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
