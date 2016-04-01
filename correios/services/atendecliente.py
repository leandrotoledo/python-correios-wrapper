#!/usr/bin/env python

from suds.client import Client, WebFault


class AtendeCliente(object):

    WSDL_URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'

    @staticmethod
    def _request(cep):
        client = Client(AtendeCliente.WSDL_URL)

        request = {
            'cep': cep,
        }

        try:
            result = client.service.consultaCEP(**request)
        except WebFault, e:
            print(e)

            return []

        try:
            new_dict = dict()

            for i in result.__keylist__:
                if result[i]:
                    new_dict[i] = result[i].encode('utf-8')
                else:
                    new_dict[i] = None
        except UnicodeEncodeError, e:
            print(e)

            return []

        return new_dict

    @staticmethod
    def consultaCEP(cep):
        result = AtendeCliente._request(cep)

        return result
