from flask import Flask, render_template 

app = Flask ("__name__")

@app.route("/")          
def home():
    return render_template ("/index.html")

@app.route("/quemsomos")          
def quemsomos():
    return render_template ("/Quemsomos.html")

@app.route("/contato")          
def contatos():
    return render_template ("/Contato.html")