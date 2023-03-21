from flask import Flask, render_template

app = Flask(__name__) #app é uma instância da classe flask
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/espaço")
def espaço():
    return render_template('espaço.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/planos")
def planos():
    return render_template('planos.html')

if __name__ == '__main__': #if sempre será o finalizador. Não pode nada após o if
    app.run(debug=True)

