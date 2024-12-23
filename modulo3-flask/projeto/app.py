from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello-world', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

# Rota de registro de dieta
@app.route('/diet', methods=['POST'])
def register_diet():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    date_time = data.get('date_time')
    isOnDiet = data.get('isOnDiet')

    if name and description and date_time and isOnDiet:
        return jsonify({"message": "Refeição registrada com sucesso!"})
    
    return jsonify({"message": "Informações inválidas!"})

if __name__ == '__main__':
    app.run(debug=True)