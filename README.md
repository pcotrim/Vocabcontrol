Sample Flask Project for Back4app Containers This repository contains a sample Flask application designed to be deployed on Back4app Containers. It serves as a template and guide to help you get started with deploying your own Flask applications on Back4app Containers.

Project Structure ├── app.py # Main Flask application entry point ├── Dockerfile # Dockerfile for building the Docker image ├── requirements.txt # Python dependencies for the Flask application └── README.md # This readme file

Getting Started Clone this repository to your local machine. git clone https://github.com/yourusername/sample-flask-project-back4app-containers.git cd sample-flask-project-back4app-containers Install the required dependencies using pip. pip install -r requirements.txt Run the Flask application locally. export FLASK_APP=app.py export FLASK_ENV=development flask run Your Flask application should now be running locally at http://127.0.0.1:5000/.

Deploying to Back4app Containers Follow the step-by-step guide in the article "Run a Flask Container App"(https://www.back4app.com/docs-containers/run-a-flask-container-app) to deploy this sample Flask application on Back4app Containers.

Customizing the Template Feel free to customize this template by modifying the app.py file and adding your own routes, views, and functionality. Make sure to update the requirements.txt file with any additional dependencies your application requires.

License This sample Flask project is released under the MIT License.


----


Este repositório contém uma aplicação Flask de exemplo projetada para ser implantada nos Back4app Containers. Ele serve como um modelo e guia para ajudá-lo a começar a implantar suas próprias aplicações Flask nos Back4app Containers.

A estrutura do projeto inclui os seguintes arquivos: app.py, que é o ponto de entrada principal da aplicação Flask; Dockerfile, que é utilizado para construir a imagem Docker; requirements.txt, que lista as dependências Python necessárias para a aplicação Flask; e README.md, que é este arquivo de instruções.

Para começar, clone este repositório para sua máquina local utilizando o comando git clone https://github.com/yourusername/sample-flask-project-back4app-containers.git, e em seguida, navegue até o diretório do projeto com cd sample-flask-project-back4app-containers. Instale as dependências necessárias usando pip install -r requirements.txt. Execute a aplicação Flask localmente utilizando os comandos export FLASK_APP=app.py, export FLASK_ENV=development e flask run. Sua aplicação Flask deverá estar rodando localmente em http://127.0.0.1:5000/.

Para implantar a aplicação nos Back4app Containers, siga o guia passo a passo disponível no artigo "Run a Flask Container App" (https://www.back4app.com/docs-containers/run-a-flask-container-app).

Sinta-se à vontade para personalizar este modelo modificando o arquivo app.py e adicionando suas próprias rotas, visualizações e funcionalidades. Certifique-se de atualizar o arquivo requirements.txt com quaisquer dependências adicionais que sua aplicação exigir.

Este projeto Flask de exemplo é distribuído sob a Licença MIT.

---
Os dados neste repositório fazem parte da pesquisa realizada na tese de doutorado de Paula Cotrim de Abrantes, elaborada na linha de pesquisa 1, Comunicação, Organização e Gestão da Informação e do Conhecimento, do Programa de Pós-Graduação em Ciência da Informação (PPGCI), do Instituto Brasileiro de Informação em Ciência e Tecnologia (Ibict), do Ministério da Ciência e Tecnologia e Inovação (MCTI), em associação com a Escola de Comunicação (ECO), da Universidade Federal do Rio de Janeiro (UFRJ).
---

TUTORIAL DE INSTALAÇÃO DO PROTÓTIPO DO CHATBOT NO GOOLGE CLOUD

Este tutorial foi elaborado pela autora desta pesquisa a partir de códigos de programação criados por um profissional da computação contratado para criar tais códigos.


A - PREPARAÇÃO DOS ARQUIVOS NO GITHUB E CRIAÇÃO DA MÁQUINA VIRTUAL NO GOOGLE CLOUD

ATENÇÃO

Observação 1: é necessário criar uma conta no Google Cloud, e, a depender do tempo de uso de uma máquina virtual, ela pode vir a ser paga.
Observação 2: instituições públicas e privadas geralmente possuem servidores computacionais com condições de hospedar e operar o Rasa sem a necessidade de pagamento de outras plataformas. 
Obseervação 3: a pasta intitulada "vocabcontrol" na tese de doutorado, recebeu o nome "tesauro" neste repositório.

INÍCIO DAS INSTRUÇÕES

1) Baixe o aplicativo do GitHub para ser usado no computador – link: https://docs.github.com/pt/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop (GitHub Doc, 2024);
2) Com o modelo já treinado (.tar.gz), copiar o modelo juntamente com os arquivos.yml na respectiva pasta do Projeto no GitHub do seu computador. Certifique-se que tenha apenas um arquivo.tar.gz na pasta models do GitHub;
3) Criar um perfil no Google Cloud;
4) Clicar no botão “Console” na tela superior direita;
5) Pesquise: compute engine; 
6) No Google Console, criar uma nova instância (“nome do chatbot”, E2, Ubuntu 20G, tipo de maquina: e2-msmall 2G, http e https clicados), verifique o IP interno e o IP externo da máquina criada. Obs.: A máquina virtual usada no Google Cloud é paga; o pagamento ocorre no cartão de crédito cadastrado;
7) No arquivo do computador doméstico, na pasta do GitHub que está o arquivo chatbot.py, atualize o IP interno da máquina nova:
rasa_url = "coloque o endereço"
8) No arquivo do computador, na pasta do GitHub que está o arquivo templates\tkinter3_codepen.htm, atualize o IP externo da máquina nova: url = "coloque o endereço";
9) Abra o software do GitHub no desktop do computador e carregue as pastas do Projeto do protótipo do chatbot que precisam estar na sua conta pessoal do GitHub na internet; a coluna “changes” mostra os arquivos modificados em azul que precisam ser atualizados;
10) Escreva no campo “summary” um comentário sobre a atualização feita e faça “commit”, e depois “push origin”.

B - CARREGAMENTO DOS ARQUIVOS DO GITHUB PARA O GOOGLE CLOUD

1) Entre no Google Cloud https://cloud.google.com/?hl=pt_br com o perfil cadastrado no Google;
2) Clique no botão “Console” na tela superior direita;
3) Pesquise “compute engine” e deve encontrar a máquina virtual criada que já está configurada;
4) Abra o terminal clicando em: conectar SSH;

C – EXECUÇÃO DOS COMANDOS NA MÁQUINA VIRTUAL DO GOOGLE CLOUD

sudo apt update

sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

curl https://pyenv.run | bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"

eval "$(pyenv virtualenv-init -)"

pyenv install 3.8.10

pyenv global 3.8.10

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

sudo apt install python3.8 python3.8-dev python3.8-venv

git clone https:// # endereço do Projeto no GitHub
certifique-se que está na raiz, username: login: # aqui insira nome do login no GitHub; chave do GitHub: # aqui insira a chave do GitHub; ela tem que ser gerada no próprio GiTHub

cd Vocabcontrol # insira o nome da pasta que está o Projeto no GitHub;

python -m venv ./venv

source ./venv/bin/activate

pip install --upgrade pip

pip install rasa spacy dataparser gunicorn Flask requests flask_cors
cd tesauro # insira o nome da subpasta do Projeto que fica dentro da pasta maior Tese-Vocabcontrol-Chatbot

pip3 install -r requirements.txt

pip install gunicorn==21.2.0
sudo nano /etc/systemd/system/ Vocabcontrol.service   # em negrito está o nome da pasta do Projeto no GitHub

* Cole o código abaixo dentro da arquivo
[Unit]
Description=Gunicorn instance for a chatbot
After=network.target
[Service]
User=pcotrimdeabr # nome do usuário no Google Cloud
Group=www-data
WorkingDirectory=/home/pcotrimdeabr/Vocabcontrol # nome do usuário no Google Cloud e a nome da pasta do Projeto no GitHub
ExecStart=/home/pcotrimdeabr/Vocabcontrol/venv/bin/gunicorn -b localhost:8000 chatbot:app
Restart=always
[Install]
WantedBy=multi-user.target

depois save: Ctrol X, Yes ENTER

sudo systemctl daemon-reload

sudo systemctl start Vocabcontrol #nome do Projeto no GitHub

sudo systemctl enable Vocabcontrol #nome do Projeto no GitHub

sudo apt-get install nginx
sudo systemctl start nginx

sudo systemctl enable nginx

sudo nano /etc/nginx/sites-available/default
# Cole o bloco antes do primeiro codigo
upstream flaskchatbot {
    server 127.0.0.1:8000;
}
# Procure a linha "location / {" e abaixo dela cole:
    proxy_pass http://flaskchatbot;
# Abaixo do bloco "location / {}" cole os dois blocos abaixo:
location /tkinter3.htm {
    proxy_pass http://flaskchatbot;
}
location /webhook {
    proxy_pass http://flaskchatbot;
}

# reestarte o servidor nginx
sudo systemctl restart nginx
sudo nginx -t

# entre no navegador Chrome e coloque o IP externo da máquina e já deve aparecer uma tela de login
# se o site estiver funcionando com tela de login pule para o passo de rodar o servidor Rasa, se não, execute o seguinte comando: 

nohup gunicorn -b localhost:8000 chatbot:app &

** PARA RODAR O RASA

1)	No terminal, vá para pasta Vocabcontrol /tesauro # nome da pasta e subpasta do Projeto no GitHub;
2)	rasa train;
# anote o nome do modelo gerado
# certifique-se que na pasta tesauro/models tenha apenas este arquivo do modelo novo gerado
3)	rasa shell; e
#certique-se que o modelo está correto, faça perguntas chave para ter certeza de que é esse modelo mesmo.
4)	feche o terminal.

** Abrindo servidor rasa "api"

Abra outro terminal

cd Vocabcontrol # nome da pasta do Projeto no GitHub
source ./venv/bin/activate

cd tesauro # subpasta do Projeto no GitHub

# certifique-se de que a porta 5005 está vazia
sudo lsof -i :5005

# se não estiver vazia, matar o serviço, use o ID do serviço indicado 
kill -9 26784

# certifique-se novamente de que a porta 5005 está vazia
sudo lsof -i :5005

# rode o comando com o nome do seu modelo de treinamento gerado no rasa train
nohup rasa run --enable-api -m ./models/20240413-130536-muted-angle.tar.gz -p 5005 & 
sudo lsof -i :5005

# certifique-se de que já passou o tempo para que o serviço esteja no ar
# o rasa somente está no ar quando esta porta 5005 mostrar o serviço rasa 
sudo lsof -i :5005
Obs: não é necessário parar ou suspender a máquina em NENHUM momento, pois isso a fará ganhar novo IP externo e irá desconfigurar tudo, além de contaminar irreversivelmente o cache, ou seja, não terá mais como voltar para situação inicial, somente criando nova máquina do zero.

Feche o terminal e estará pronto; para visualizar o chatbot, acesse o link do IP externo disponibilizado pelo Google Cloud, vá em “compute engine” que o encontrará.

Observações Gerais:

Os arquivos completos usados na instalação do protótipo do chatbot PatentIA na máquina virtual do Google Cloud podem ser encontrados em: https://github.com/pcotrim/Vocabcontrol.
Para criar um chatbot igual ao desta pesquisa, aconselha-se usar os arquivos disponíveis nesse repositório e mudar somente os dados nos arquivos .yml e os arquivos sinalizados neste tutorial. 
O protótipo do chatbot PatentIA pode ser acessado pelo link: http://35.193.251.126/

