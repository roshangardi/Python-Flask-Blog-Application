from flaskblog import app

if __name__ == "__main__":
    # Run the flask application by calling run on the object
    app.run(debug=True)  # we set debug=True so that whenever we make any new changes in file, we don't have to restart
    # the server for them to take effect
