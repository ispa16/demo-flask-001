from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo desde mi PC :333 </h1>"

@app.route('/suma')
def suma():
    resultado = 0 + 0
    return "<h3>0 + 0 = %d</h3>" % (resultado)
@app.route('/listado')
def listado():
	bb= ("<h1>Mis cervezas favoritas</h1>"+
	"<ol>"+
	"<li>Cusquena</li>"+
	"<li>Pilsener</li>"+
	"<li>Corona</li>"+
	"<li>Harbin</li>"+
	"<li>Budweiser</li>"+
	"<li>Heineken</li>"+
	"<li>Club</li>"+
	"</ol>")

	return bb

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
