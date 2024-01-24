from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/webhook', methods=['POST'])
def webhook():
    # Recebe os dados da requisição
    data = request.json

    # Direciona a requisição para o servidor Rasa
    rasa_url = "http://127.0.0.1:5005/webhooks/rest/webhook"
    response = requests.post(rasa_url, json=data)

    # Retorna a resposta do servidor Rasa
    return jsonify(response.json())

if __name__ == '__main__':
    # Inicia o servidor Flask
    app.run(host='0.0.0.0', port=5004)  # Altere a porta conforme necessário
