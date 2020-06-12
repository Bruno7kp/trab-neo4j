### Instalação

Clone o repositório

```
git clone https://github.com/bruno7kp/mural-virtual.git
```

No diretório raiz do projeto, execute os seguintes comandos para criar o ambiente virtual e instalar as bibliotecas utilizadas

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

O banco de dados está  no arquivo `banco-de-dados.txt`, execute o arquivo completo em uma única vez.
A senha configurada no código é `1234`, caso precise alterar a senha, a mesma está no arquivo `app.py`

Por fim, execute os comandos abaixo para rodar o projeto

```
set FLASK_ENV='development'
set FLASK_DEBUG=1
python -m flask run
```
