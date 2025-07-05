from flask import Flask, request
import hashlib, sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = hashlib.sha256(request.form['clave'].encode()).hexdigest()
        con = sqlite3.connect("usuarios.db")
        con.execute("INSERT INTO usuarios VALUES (?, ?)", (usuario, clave))
        con.commit()
        return "Registrado correctamente"
    return '''<form method='post'>Usuario:<input name='usuario'><br>Clave:<input name='clave'><br><input type='submit'></form>'''

if __name__ == '__main__':
    app.run(port=5800)
