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

from mock import patch
from xivo_provd_client import client


class TestNewProvisioningClient(unittest.TestCase):

    @patch('xivo_provd_client.client.new_provisioning_client')
    def test_new_from_config_minimal(self, mock_new_provisioning_client):
        provd_config = {}

        provd_client = client.new_provisioning_client_from_config(provd_config)

        expected_url = 'http://localhost:8666/provd'
        mock_new_provisioning_client.assert_called_once_with(expected_url, None)
        self.assertIs(provd_client, mock_new_provisioning_client.return_value)

    @patch('xivo_provd_client.client.new_provisioning_client')
    def test_new_from_config_full(self, mock_new_provisioning_client):
        provd_config = {
            'host': 'example.org',
            'port': 9999,
            'username': 'foo',
            'password': 'bar',
            'https': True,
        }

        provd_client = client.new_provisioning_client_from_config(provd_config)

        expected_url = 'https://example.org:9999/provd'
        expected_credentials = ('foo', 'bar')
        mock_new_provisioning_client.assert_called_once_with(expected_url, expected_credentials)
        self.assertIs(provd_client, mock_new_provisioning_client.return_value)
