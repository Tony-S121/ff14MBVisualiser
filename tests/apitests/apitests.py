import unittest
from unittest.mock import AsyncMock

import pytest

from apiclient.apiclient import Client, APICalls


class APITests(unittest.IsolatedAsyncioTestCase):
 #    def setUp(self):
 #        self.universalis_client = Client(base_url='https://universalis.app/api/v2')
 #        self.api_caller = APICalls(self.universalis_client)
 #
 # #   @pytest.fixture
 # #   def cli(self, loop, api_caller):
 #
 #  #      return loop.run_until_complete(api_caller)
 #
 #    async def test_get_worlds(self):
 #        mock = AsyncMock()
 #        #mock.return_value = 200
 #        awaited_res = await self.universalis_client.check_endpoint('/worlds')
 #        self.assertEqual(200, awaited_res)
 #
