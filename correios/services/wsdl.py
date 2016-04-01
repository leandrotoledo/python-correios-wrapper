#!/usr/bin/env python

import json


class WSDL(object):

    @staticmethod
    def _request(*args, **kwargs):
        pass

    @staticmethod
    def _toutf8(string):
        try:
            result = string.encode('utf-8')
        except UnicodeEncodeError, e:
            # logging
            result = ''

        return result

    @staticmethod
    def _todict(string):
        try:
            result = json.loads(string)
        except ValueError, e:
            # logging
            result = dict()

        return result

    @staticmethod
    def _toutf8dict(old_dict):
        new_dict = dict()

        if not old_dict:
            return new_dict

        for i in old_dict.__keylist__:
            new_dict[i] = None

            if old_dict[i]:
                new_dict[i] = WSDL._toutf8(old_dict[i])

        return new_dict
