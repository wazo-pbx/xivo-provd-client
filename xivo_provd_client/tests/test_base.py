# -*- coding: utf-8 -*-

# Copyright (C) 2015 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import unittest
import urllib2

from xivo_provd_client.base import not_found_error_on_404
from xivo_provd_client.error import NotFoundError


class TestNotFoundError(unittest.TestCase):

    def test_no_exception(self):
        with not_found_error_on_404():
            pass

    def test_404_http_error(self):
        try:
            with not_found_error_on_404():
                raise self._new_http_error(404)
        except NotFoundError:
            pass

    def test_non_404_http_error(self):
        code = 500
        try:
            with not_found_error_on_404():
                raise self._new_http_error(code)
        except urllib2.HTTPError as e:
            self.assertEqual(e.code, code)

    def test_other_exception(self):
        e = Exception('foo')
        try:
            with not_found_error_on_404():
                raise e
        except Exception as expected_e:
            self.assertIs(e, expected_e)

    def _new_http_error(self, code):
        return urllib2.HTTPError('', code, '', '', None)
