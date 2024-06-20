from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, RadioField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Simula um banco de dados na memória
produtos = []

class ProdutoForm(FlaskForm):
    nome = StringField('Nome do Produto', validators=[DataRequired()])
    descricao = StringField('Descrição do Produto', validators=[DataRequired()])
    valor = DecimalField('Valor do Produto', validators=[DataRequired()])
    disponivel = RadioField('Disponível para Venda', choices=[('sim', 'Sim'), ('não', 'Não')], validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = ProdutoForm()
    if form.validate_on_submit():
        novo_produto = {
            'nome': form.nome.data,
            'descricao': form.descricao.data,
            'valor': form.valor.data,
            'disponivel': form.disponivel.data
        }
        produtos.append(novo_produto)
        return redirect(url_for('listagem'))
    return render_template('cadastro.html', form=form)

@app.route('/listagem')
def listagem():
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    return render_template('listagem.html', produtos=produtos_ordenados)

@app.route('/')
def index():
    return redirect(url_for('listagem'))

if __name__ == '__main__':
    app.run(debug=True)
