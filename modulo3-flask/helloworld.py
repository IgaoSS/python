from flask import Flask

# Toda vez que é executado de forma manual, o name vem como main
# __name__ = " __main__"
app = Flask(__name__)

# Toda vez que alguém acessar essa rota "/", ele irá executar essa função hello_world
@app.route("/")
def hello_world():
    return "Hello, World!"

# Rota de sobre
@app.route("/about")
def cadastro():
    return "Tela de sobre nós"

# Se for executado de forma manual, rodar o Debug, que são logs para verificar o andamento da aplicação
# Recomendado esse trecho de código para que seja visto apenas no momento do desenvolvimento
# Ou seja, só será visto o debug quando roda manualmente
if __name__ == "__main__":
    app.run(debug=True)