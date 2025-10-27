from flask import Flask

#WSGI application is created which required to communicate between web application and web server
sample_app=Flask(__name__)

@sample_app.route("/")
def welcome():
    return "Welcome to my Page"

if __name__ == "__main__":
    sample_app.run(debug=True)