# mysql-connector-python==8.1.0
# protobuf==3.20.0


# no replit instale
# https://replit.com/@otimistarj/rasa
# rasa, spacy, dataparser, gunicorn, Flask
# spacy download en_core_web_md (não instalou nada...)
# no shell faça: pip list
# rasa init (crie diretorio tesauro)
# cd tesauro
# rasa rasa shell

# No hostgator existe o acesso terminal e ambiente virtual disponivel
# digite python --version
# mas apenas Python 3.5.1
# https://suporte.hostgator.com.br/hc/pt-br/articles/115000384693-Quais-s%C3%A3o-as-compatibilidades-da-HostGator-
# o rasa versão atual exige Python 3.7
# https://rasa.com/docs/rasa/installation/environment-set-up
# para ter acesso ao Python 3.7 tem que ter plano VPS
# https://www.hostgator.com.br/servidor-vps

# para criar ambiente virtual no terminal do cpanel do hostgator:
# no Cpanel escolha Terminal
# python3 --version
# veja que está instalado o python 3.6.8
# para criar ambiente virtual
# python -m venv list
# virtualenv -p python3 env
# módulos instalados
# pip list
# para ativar ambiente virtual criado env
# source env/bin/activate
# (env) cienti42@cientistaspatentes.com.br [~]#

# como descobrir a versão do RASA que roda em python 3.6.8
# a versão atual do rasa é 3.6.0
# prompt DOS
# cd anaconda3/condabin
# conda env list
# conda create -n python3_6_8 python=3.6.8
# conda activate python3_6_8
# python --version
# https://bard.google.com/
# qual a versao do rasa 3.4 disponivel ?
# o rasa 3.4.16 roda em que python ?
# pip install rasa==2.8.26

# abra janela View terminal
# pip install rasa
# rasa init (crie diretorio tesauro)
# cd tesauro
# rasa shell
# pip freeze > requirements.txt

# pip install Flask
# pip install gunicorn
# pip install arrow
# pip install dateparser
# pip install spacy
# spacy download en_core_web_md
# pip list

# Rodando o chatbot
# va para diretorio (GUI_Rasa) PS C:\Users\otimi\PycharmProjects\GUI_Rasa> cd tesauro
# rode rasa shell
# aguarde mensagem Loading model models\20230910-213348-knurled-button.tar.gz..
# aguarde o prompt: Your input ->
# digite /stop

# em uma outra janela Terminal rodar em  cd tesauro (isso faz rodar actions.py)
# rasa run actions
# aguardar Action endpoint is up and running on http://0.0.0.0:5055

# para rodar o navegador do chatbot no browser
# anote o arquivo com rede treinada e copie no comando abaixo cd tesauro e executando numa outra janela do terminak
# rasa run --enable-api -m ./models/20230806-134947-witty-baluster.tar.gz --cors "*"
# rasa run --enable-api -m ./models/20230804-093217-isometric-property.tar.gz --cors "*"
# rasa run --enable-api -m ./models/20230910-213348-knurled-button.tar.gz --cors "*"
# rasa run --enable-api -m ./models/20240103-220920-ivory-loop.tar.gz --cors "*"
# certifique-se do modelo ter sido lido e vir a mensagem Rasa server is up and running

# agora rode (clique na seta verde) este programa chatbot.py
# clique em http://127.0.0.1:8080 para abrir no navegador

# Para atualizar este projeto no GITHUB:
# atualize diretorio "C:\Users\otimi\OneDrive\Documentos\GitHub\Chatbot"
# verifique https://www.github.com/antonioabrantes/Chatbot
# https://containers.back4app.com/apps
# selecione chatbot

# pip install rasa-x --extra-index-url https://pypi.rasa.com/simple



from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Defina uma senha simples para a demonstração (substitua por algo mais seguro em produção)
senha_correta = "senha123"

@app.route("/")
def homepage():
    return render_template("login.html")
    # return render_template("tkinter3_codepen.htm")

@app.route("/tkinter3.htm", methods=["GET", "POST"])
def tkinter3():
    if request.method == "POST":
        senha_digitada = request.form.get("senha")

        if senha_digitada == senha_correta:
            return render_template("tkinter3_codepen.htm")
        else:
            return redirect("/?senhaIncorreta=true")

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # Recebe os dados da requisição
        data = request.json

        # Direciona a requisição para o servidor Rasa
        rasa_url = "http://10.128.0.4:5005/webhooks/rest/webhook"
        response = requests.post(rasa_url, json=data)

        # Retorna a resposta do servidor Rasa
        return jsonify(response.json())
    except Exception as e:
        print(f"Erro no webhook: {str(e)}")
        return jsonify({"error": "Erro interno no servidor"}), 500

if __name__ == '__main__':
    app.run()

# from flask import Flask, render_template
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  
# # This enables CORS for all routes

# @app.route("/")
# def homepage():
#     # return render_template("tkinter3.htm")
#     # return render_template("tkinter3_rasa.htm")
#     return render_template("tkinter3_codepen.htm")

# @app.route("/tkinter3.htm")
# def tkinter3():
#     return render_template("tkinter3.htm")


# if __name__ == "__main__":
#     # app.run(debug=True)
#     app.run(host='0.0.0.0', port=8080)
