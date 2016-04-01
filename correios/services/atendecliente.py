#!/usr/bin/env python

from suds.client import Client, WebFault
from correios.services import WSDL


class AtendeCliente(WSDL):

    WSDL_URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'

    @staticmethod
    def _request(cep):
        client = Client(AtendeCliente.WSDL_URL)

        try:
            result = client.service.consultaCEP(cep=cep)
        except WebFault, e:
            # logging
            result = ''

        return AtendeCliente._toutf8dict(result)

    @staticmethod
    def consultaCEP(cep):
        return AtendeCliente._request(cep)
