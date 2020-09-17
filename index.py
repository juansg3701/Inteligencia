from flask import Flask, render_template,request,redirect,url_for
import  bj as bk

blackjack = bk.blackJ()

app = Flask(__name__)

@app.route(r'/')
def home():
	return render_template('index.html')

@app.route(r'/datos', methods = ['POST','GET'])
def datos():
    #nombre= request.form['nombre'];
    blackjack.menu()
    nombre="Kai"
    return render_template('mesa.html',nombre=nombre)

@app.route(r'/postmethod', methods = ['GET'])
def get_post_javascript_data():
    jsdata = request.args.get("holi",0)
    print("jsdata: "+jsdata)
    blackjack.recibir_opcion(jsdata)
    return jsdata

if __name__ == '__main__':
	app.run(debug=True)

