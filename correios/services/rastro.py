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

from suds.client import Client, WebFault
from correios.services import WSDL


class Rastro(WSDL):

    WSDL_URL = 'http://webservice.correios.com.br/service/rastro/Rastro.wsdl'
    WSDL_BOOTSTRAP = {
        'usuario': 'ECT',
        'senha': 'SRO',
        'tipo': 'L',
        'resultado': 'T',
        'lingua': '101'
    }

    @staticmethod
    def RastroJson(objeto):
        client = Client(Rastro.WSDL_URL)

        try:
            result = client.service.RastroJson(objetos=objeto,
                                               **Rastro.WSDL_BOOTSTRAP)
        except WebFault, e:
            # logging
            result = ''

        result = Rastro._toutf8(result)
        result = Rastro._todict(result)

        try:
            return result['sroxml']['objeto']['evento']
        except KeyError:
            return dict()
