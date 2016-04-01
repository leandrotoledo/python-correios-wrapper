#!/usr/bin/env python

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
    def _request(objeto, **kwargs):
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

    @staticmethod
    def RastroJson(objeto):
        return Rastro._request(objeto, **Rastro.WSDL_BOOTSTRAP)
