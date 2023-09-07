from flask import Flask
from app.routers.veiculoRouters import *
app = Flask(__name__)

app.add_url_rule(routers["rota"],view_func=routers["itemVeiculo"])