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
