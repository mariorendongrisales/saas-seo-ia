import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Usar host='0.0.0.0' para permitir conexiones externas (necesario en producción)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))