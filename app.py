# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# New Function Added
@app.route('/status')
def status():
    return "Bot is active!"

if __name__ == '__main__':
    app.run(debug=True)