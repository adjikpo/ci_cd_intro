from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/hello/<name>')
def show_user_profile(name):
    return 'Hello %s' % escape(name)

if __name__ == "__main__":
    app.run()