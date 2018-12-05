import os
from flask import Flask, request, render_template
from flask_sslify import SSLify

app = Flask(__name__)

KEY_PATH = "privkey.pem"
CRT_PATH = "fullchain.pem"


@app.route("/")
def renderHTML():
    """
    Render home page
    :return: home.html
    """
    return render_template("pages/home.html")


@app.route("/mosquito")
def renderInfo():
    """
    :return: the mosquito-monitoring project
    """
    pass


if __name__ == "__main__":
    """
    Launch flask application, with SSL certificate if available
    """
    if os.path.exists(CRT_PATH) and os.path.exists(KEY_PATH):
        print("Loading with certificate")
        # Forcing https:// connections
        sslify = SSLify(app)
        # Running the app with certificates
        app.run(host='0.0.0.0', ssl_context=(CRT_PATH, KEY_PATH), port='8000')
    else:
        print("Loading HTTP")
        app.run(host='0.0.0.0', port='8000')
