import os
from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"

#app.instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
#app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'database.db')}"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#os.makedirs(app.instance_path, exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# Rota de carregamento do usuário
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

# Rota de login e autenticação
@app.route('/login', methods=["POST"])
def login():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username and password:
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
      login_user(user)
      return jsonify({"message": "Autenticação realizada com sucesso!"})

  return jsonify({"message": "Credenciais inválidas!"}), 400

# Rota de logout e desautenticação
@app.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  return jsonify({"message": "Logout realizado com sucesso!"})

# Rota de criação de usuário
@app.route('/user', methods=['POST'])
def create_user():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')

  if username and password:
    user_exist = User.query.filter_by(username=username).first()
    if user_exist:
      return jsonify({"message": "Nome de usuário já cadastrado no sistema. Por favor, informe os dados novamente!"})
    
    hash_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
    user = User(username=username, password=hash_password, role='user')
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuário cadastrado com sucesso!"})

  return jsonify({"message": "Dados inválidos!"}), 400

# Rota de retorno de usuário
@app.route('/user/<int:id_user>', methods=['GET'])
@login_required
def read_user(id_user):
  user = User.query.get(id_user)

  if user:
    return jsonify({"id": user.id, "username": user.username})
  
  return jsonify({"message": "Usuário não encontrado!"}), 404

# Rota de atualização de senha usuário
@app.route('/user/<int:id_user>', methods=['PUT'])
@login_required
def update_password(id_user):
  user = User.query.get(id_user)
  data = request.get_json()
  password = data.get('password')

  if id_user != current_user.id and current_user.role == "user":
    return jsonify({"message": "Operação não permitida!"}), 403
  
  if user and password:
    hash_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
    user.password = hash_password
    db.session.commit()
    
    return jsonify({"message": f"Usuário {id_user} atualizado com sucesso!"})
      
  return jsonify({"message": "Usuário não encontrado!"}), 404

# Rota de exclusão de usuário
@app.route('/user/<int:id_user>', methods=['DELETE'])
@login_required
def delete_user(id_user):
  user = User.query.get(id_user)

  if current_user.role != 'admin':
    return jsonify({"message": "Operação não permitida!"}), 403
  
  if id_user == current_user.id:
    return jsonify({"message": "Não é permitido excluir o próprio usuário!"}), 403

  if user:
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"Usuário {id_user} deletado com sucesso!"})
  
  return jsonify({"message": "Usuário não encontrado!"}), 404

if __name__ == '__main__':
  app.run(debug=True)