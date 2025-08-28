from flask import *

app = Flask(__name__)

roupas = [['Cuecão', 'cueca', 'G', '12', 'éssa bvosta ai']]
vendedores = []
clientes = []
logado = False
cliente = False
vendedor = False


@app.route('/')
def pag_principal():
    return render_template('paginainicial.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastrousuario.html')

@app.route('/cadastrar', methods = ['post'])
def cadastrar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    tipouser = request.form.get('tipouser')
    msg = ''
    login = [usuario, senha]
    repetido = False

    global vendedores, clientes

    if tipouser == 'vendedor':
        for vendedor in vendedores:
            if usuario == vendedor[0]:
                repetido = True

        if repetido:
            msg = "Usuário já existe."
            return render_template('cadastrousuario.html', saida=msg)

        else:
            vendedores.append(login)
            msg = 'Usuário cadastrado com sucesso!'

        print(vendedores)
        return render_template('cadastrousuario.html', saida = msg)

    else:
        for cliente in clientes:
            if usuario == cliente[0]:
                repetido = True

        if repetido:
            msg = "Usuário já existe."
            return render_template('cadastrousuario.html', saida=msg)

        else:
            clientes.append(login)
            msg = 'Usuário cadastrado com sucesso!'
        print(clientes)
        return render_template('cadastrousuario.html', saida = msg)








@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logar', methods=['post'])
def logar ():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    global logado, cliente, vendedor
    for cliente in clientes:
        if usuario == cliente[0] and senha == cliente[1]:
            logado = True
            cliente = True
            vendedor = False
            break
        else:
            for vendedor in vendedores:
                if vendedor == vendedores[0] and senha == vendedor[1]:
                    logado = True
                    vendedor = True
                    cliente = False
                    break


    if logado:
        return render_template('paginainicial.html')

    msg = 'Usuário ou senha incorretos'
    return render_template('login.html', erro=msg)

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