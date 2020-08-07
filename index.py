from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/datos', methods = ['POST','GET'])
def datos():
	cars = ["Ford", "Volvo", "BMW"] 
	nombre= request.form['nombre'];
	return render_template('mesa.html',nombre=nombre)

@app.route('/datos/<nombre>')
def funcion1(nombre):
	return "hola" %nombre


if __name__ == '__main__':
	app.run(debug=True)


