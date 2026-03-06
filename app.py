from flask import Flask, redirect, render_template, request
import mysql.connector
from model.musica import recuperar_musicas
from model.genero import recuperar_generos
from model.musica import adicionar_musica
from model.musica import excluir_musica
from model.musica import ativar_musica
from model.usuario import adicionar_usuario

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=["GET"])
def pagina_principal():
    # recuperando as musicas
    musicas = recuperar_musicas(True)
    # recuperando os generos
    generos = recuperar_generos()
    # mostrando a pagina
    return render_template("principal.html", musicas = musicas, generos = generos)

@app.route("/admin")
def pagina_admin():
    musicas = recuperar_musicas()
    generos = recuperar_generos()
    return render_template("administracao.html", musicas = musicas, generos = generos)

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("input_titulo")
    cantor = request.form.get("input_cantor")
    duracao = request.form.get("input_duracao")
    url = request.form.get("input_url")
    genero = request.form.get("genero")
    
    if adicionar_musica(cantor, duracao, nome_musica, url, genero):
        return redirect("/admin")
    else:
        return "ERRO AO ADICIONAR MÚSICA"
    
# esse <> é pra colocar o que eu quero pegar
@app.route("/musica/delete/<id>")
def api_deletar_musica(id):
    if excluir_musica(id):
        return redirect ("/admin")
    
    else:
        return "ERRO AO EXCLUIR A MUSICA"
    
@app.route("/musica/ativar/<id>/<status>")
def api_ativar(id,status):
    if ativar_musica(id,status):
        return redirect ("/admin")
    else:
        return "ERRO AO ATIVAR A MUSICA"
    

@app.route("/cadastro", methods=["GET"])
def api_cadastro():
    return render_template("cadastro.html")


@app.route("/cadastro", methods=["POST"])
def pegar_dados():
    nome_usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if adicionar_usuario(nome_usuario, senha):
        return redirect ("/admin")
    else:
        return "ERRO"

@app.route("/login", methods=["GET"])
def fazer_login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

