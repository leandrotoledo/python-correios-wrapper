#!/usr/bin/env python

from suds.client import Client, WebFault

import json


class Rastro(object):

    WSDL_URL = 'http://webservice.correios.com.br/service/rastro/Rastro.wsdl'
    WSDL_BOOTSTRAP = {
        'usuario': 'ECT',
        'senha': 'SRO',
        'tipo': 'L',
        'resultado': 'T',
        'lingua': '101'
    }

    @staticmethod
    def _request(objeto, **kwargs):
        client = Client(Rastro.WSDL_URL)

        request = {
            'objetos': objeto,
        }
        request.update(kwargs)

        try:
            result = client.service.RastroJson(**request)
        except WebFault, e:
            print(e)

            return []

        try:
            result = result.encode('utf-8')
        except UnicodeEncodeError, e:
            print(e)

            return []

        try:
            result = json.loads(result)
            result = result['sroxml']['objeto']['evento']
        except ValueError, e:
            print(e)

            return []

        return result

    @staticmethod
    def RastroJson(objeto):
        result = Rastro._request(objeto, **Rastro.WSDL_BOOTSTRAP)

        return result
