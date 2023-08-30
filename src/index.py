from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/variables')
def variables():
    return render_template('variables.html') 

@app.route('/operadores')
def operadores():
    return render_template('operadores.html')

@app.route('/condicionales')
def condicionales():
    return render_template('condicionales.html') 

@app.route('/funciones')
def funciones():
    return render_template('funciones.html')     

if __name__ == '__main__':
    app.run(debug=True)    