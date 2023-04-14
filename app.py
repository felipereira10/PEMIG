from flask import Flask, render_template # """ importa classe flask """

app = Flask ("__name__") #""" cria uma instância dessa classe """

@app.route("/")          #""" cria rotas com o decorator """
def home():
    return render_template ("/index.html")

@app.route("/quemsomos")          
def quemsomos():
    return render_template ("/Quem somos.html")

@app.route("/contato")          
def contatos():
    return render_template ("/Contato.html")