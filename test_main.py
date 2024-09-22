import unittest
from unittest import TestCase

from requests import HTTPError
from requests import Response

import main


class Test(TestCase):
    def test_check_for_redirect_throws_if_redirect(self):
        redirect_response = Response()
        redirect_response.status_code = 302
        with self.assertRaises(HTTPError):
            main.check_for_redirect(redirect_response)

    def test_check_for_redirect_silient_if_ok(self):
        ok_response = Response()
        ok_response.status_code = 200
        try:
            main.check_for_redirect(ok_response)
        except HTTPError:
            self.fail("check_for_redirect throws HTTPError unexpectedly")



if __name__ == '__main__':
    unittest.main()
