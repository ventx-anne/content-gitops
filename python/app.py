from flask import Flask
from jinja2 import Markup

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hallo Version 1.2!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
