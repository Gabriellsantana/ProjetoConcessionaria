from flask.views import MethodView
from flask import request, render_template 
from app.db import pymysql

class Veiculo(MethodView):

    def get(self):
        return render_template('index.html')
    
    def post(self):
        vei_tipo = request.form['vei_tipo']
        vei_marca = request.form['vei_marca']
        vei_modelo = request.form['vei_modelo']
        vei_cor = request.form['vei_cor']
        vei_ano_fabricacao = request.form['vei_ano_fabricacao'] 
        vei_estado = request.form['vei_estado']
        vei_quilometragem = request.form['vei_quilometragem']
        vei_passagem = request.form['vei_passagem']
        vei_pagamento = request.form['vei_pagamento']
        # vei_foto = request.form['vei_foto']
        print(vei_tipo, vei_marca, vei_modelo, vei_cor , vei_ano_fabricacao, vei_estado, vei_quilometragem, vei_passagem, vei_pagamento)
        return "Veiculo cadastrado com sucesso!"
    
    @app.route('/cadastrarVeiculo')
    def cadastrarVeiculo():
        return render_template('cadastrarVeiculo.html')
