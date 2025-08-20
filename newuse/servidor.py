from flask import *

app = Flask(__name__)

@app.route('/')
def pag_principal():
    return render_template('paginainicial.html')

@app.route('/cadastraritem')
def cadastro_item():
    return render_template('cadastraritem.html')


if __name__ == '__main__':
    app.run()