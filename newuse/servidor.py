from flask import *

app = Flask(__name__)

roupas = []
vendedores = []
clientes = [['eviby', 'liedso123'],['beabadoobee', 'beabadoobee1',['meia','camisa']]]



@app.route('/')
def pag_principal():
    return render_template('paginainicial.html')

@app.route('/login', methods=['post'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')
    logado = False
    for cliente in clientes:
        if login == cliente[0] and senha == cliente[1]:
            logado = True

    if logado:
        return render_template('logado.html')

    msg = 'voce errou o login e a senha'
    return render_template('login.html', erro = msg)

@app.route('/cadastraritem')
def cadastro_item():
    return render_template('cadastraritem.html')

@app.route('/cadastrarroupa', methods=['post'])
def cadastro_roupa():
    nome = request.form.get('nomeroupa')
    categoria = request.form.get('categoria')
    tamanho = request.form.get('tamanho')
    preco = request.form.get('preco')
    descricao = request.form.get('descricao')


    roupa = [nome, categoria, tamanho, preco, descricao]

    global roupas
    roupas.append(roupa)

    print(roupas)

    return render_template('cadastrarroupa.html')


if __name__ == '__main__':
    app.run()