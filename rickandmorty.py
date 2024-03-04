from flask import Flask, render_template
import requests
character = 'Morty'
#creates the application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', character = character)
peeps = ['Rick', 'Morty', 'Picklerick']

@app.route('/loop')
def loop():
    return render_template('loops.html', p = peeps)
#run the application
if __name__ == '__main__':
    app.run(debug = True)