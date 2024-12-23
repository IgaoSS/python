from flask import Flask, request, jsonify
from models.diet import Diet
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3307/daily-diet'

db.init_app(app)

@app.route('/hello-world', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

# Rota de registro de refeição
@app.route('/diet', methods=['POST'])
def register_diet():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    date_time = data.get('date_time')
    is_on_diet = data.get('is_on_diet')

    if name and description and date_time:
        diet = Diet(name=name, description=description, date_time=date_time, is_on_diet=is_on_diet)
        db.session.add(diet)
        db.session.commit()
        return jsonify({"message": "Refeição registrada com sucesso!"})
    
    return jsonify({"message": "Informações inválidas!"}), 400

# Rota de atualização de uma refeição
@app.route('/diet/<int:id_diet>', methods=['PUT'])
def update_diet(id_diet):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    date_time = data.get('date_time')
    is_on_diet = data.get('is_on_diet')

    diet = Diet.query.get(id_diet)
    if diet:
        new_name = name if name else diet.name
        new_description = description if description else diet.description
        new_date_time = date_time if date_time else diet.date_time
        new_is_on_diet = is_on_diet if is_on_diet else diet.is_on_diet

        diet.name = new_name
        diet.description = new_description
        diet.date_time = new_date_time
        diet.is_on_diet = new_is_on_diet
        db.session.commit()
        
        return jsonify({"message": "Atualização realizada com sucesso"})

    return jsonify({"message": "Refeição não localizada!"}), 404

# Rota de exclusão de uma refeição
@app.route('/diet/<int:id_diet>', methods=['DELETE'])
def delete_diet(id_diet):
    diet = Diet.query.get(id_diet)

    if diet:
        db.session.delete(diet)
        db.session.commit()
        return jsonify({"message": "Refeição excluída com sucesso!"})
    
    return jsonify({"message": "Refeição não localizada!"}), 404

# Rota para buscar todas refeições do usuário
@app.route('/diet', methods=['GET'])
def getd_diets():
    diet = Diet.query.all()
    print(diet)

    if diet:
        diet_list = [d.to_dict() for d in diet ]

        output = {
            "diets": diet_list,
            "total_diets": len(diet_list)
        }

    return jsonify(output)

# Rota para buscar uma refeição específica
@app.route('/diet/<int:id_diet>', methods=['GET'])
def get_diet(id_diet):
    diet = Diet.query.get(id_diet)

    if diet:
        return jsonify(diet.to_dict())
    
    return jsonify({"message": "Refeição não localizada!"}), 404

if __name__ == '__main__':
    app.run(debug=True)