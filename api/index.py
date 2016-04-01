#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2016
# Leandro Toledo de Souza <leandrotoledodesouza@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

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

        if result:
            return result, 200
        return '', 404


class ConsultaCEP(Resource):

    def get(self, cep):
        result = AtendeCliente.consultaCEP(cep)

        if result:
            return result, 200
        return '', 404


api.add_resource(RastroJson, '/rastreamento/<string:objeto>')
api.add_resource(ConsultaCEP, '/consultacep/<string:cep>')

if __name__ == '__main__':
    app.run(debug=True)
