from flask import Flask, jsonify, request ## importando flask e seus métodos

app = Flask(__name__) ## criando uma instância da class Flask

## db
users = [
    {'id': 1, 'name': 'Rafael', 'email': 'rafael@email.com'},
    {'id': 2, 'name': 'Diego', 'email': 'diego@email.com'},
    {'id': 3, 'name': 'Rafaela', 'email': 'rafaela@email.com'}
]

## criar um usuário
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

## listar usuários
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

## atualizar usuários
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = next((user for user in users if user['id'] == id), None)
    if user:
        user['name'] = data['name']
        user['email'] = data['email']
        return jsonify(user), 200
    else:
        return jsonify({
        'message': 'Usuário não encontrado'
    })

## deletar usuários
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [user for user in users if user['id'] != id]
    return jsonify({
        'message': 'Usuário deletado com sucesso'
    }), 200


## iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=8080)