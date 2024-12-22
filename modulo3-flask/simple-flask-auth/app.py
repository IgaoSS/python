import os
from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
os.makedirs(app.instance_path, exist_ok=True)

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
#view login
login_manager.login_view = 'login'
#Session <- conexão ativa

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@app.route('/login', methods=["POST"])
def login():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username and password:
   # Login
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
      login_user(user)
      return jsonify({"message": "Autenticação realizada com sucesso!"})

  return jsonify({"message": "Credenciais inválidas"}), 400

@app.route("/hello-world", methods=["GET"])
def hello_world():
  return "Hello world"

if __name__ == '__main__':
  app.run(debug=True)