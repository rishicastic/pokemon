import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pokemon/<name>', methods=['GET'])
def get_pokemon_by_name(name):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        data = response.json()
        height = data['height']
        id = data['id']
        name = data['name']
        weight = data['weight']
        types = [t['type']['name'] for t in data['types']]
        return jsonify(height=height, id=id, name=name, weight=weight, types=types)
    except:
        return jsonify(error='Pokemon not found'), 404

@app.route('/pokemon/<int:index>', methods=['GET'])
def get_pokemon_by_index(index):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{index}')
        data = response.json()
        height = data['height']
        id = data['id']
        name = data['name']
        weight = data['weight']
        types = [t['type']['name'] for t in data['types']]
        return jsonify(height=height, id=id, name=name, weight=weight, types=types)
    except:
        return jsonify(error='Pokemon not found'), 404

@app.route('/pokedex', methods=['GET'])
def get_pokedex():
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokedex')
        data = response.json()
        return jsonify(data)
    except:
        return jsonify(error='Pokedex not found'), 404

if __name__ == '__main__':
    app.run(debug=True)

