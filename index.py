from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/datos', methods = ['POST','GET'])
def datos():
	cars = ["Ford", "Volvo", "BMW"] 
	nombre= request.form['nombre'];
	int(request.args.get('player_move',0))
	return render_template('mesa.html',nombre=nombre)

@app.route('/datos/numero',methods = ['POST','GET'])
def funcion2(request):
    print("ah")
    if request.method == 'POST':
        id1 = request.POST['id1']
        return render_template('index.html')
    else:
        return HttpResponse("Peticion no valida")



if __name__ == '__main__':
	app.run(debug=True)


