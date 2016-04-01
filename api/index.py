#!/usr/bin/env python

import sys
sys.path.insert(0, '.')

from correios.services import Rastro, AtendeCliente
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class RastroJson(Resource):

    def get(self, objeto):
        result = Rastro.RastroJson(objeto)
        return result


class ConsultaCEP(Resource):

    def get(self, cep):
        result = AtendeCliente.consultaCEP(cep)
        return result

api.add_resource(RastroJson, '/rastreamento/<string:objeto>')
api.add_resource(ConsultaCEP, '/consultacep/<string:cep>')

if __name__ == '__main__':
    app.run(debug=True)
