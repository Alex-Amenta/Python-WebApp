import os
from flask import Flask, render_template

app = Flask(__name__)

# Obtén la ruta completa al directorio actual (donde se encuentra index.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta completa al archivo requirements.txt dentro de la carpeta src
requirements_file = os.path.join(current_dir, 'src', 'requirements.txt')

# Lee las dependencias desde el archivo requirements.txt
with open(requirements_file) as f:
    dependencies = f.read().splitlines()

# Instala las dependencias
for dependency in dependencies:
    if dependency:
        os.system(f'pip install {dependency}')

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