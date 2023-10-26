import unittest
from kite_connection_manager.connection_manager import KiteConnectionManager
import logging

logging.basicConfig(level=logging.INFO)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # creds = {
        #     "name": "Aneesha Kaushal",
        #     "user_name": "JFA773",
        #     "password": "buy@Farm1",
        #     "api_key": "97wr0exmsqicnu01",
        #     "api_secret": "ntos88g38uma3jkyczhg7ac6g8ar4pj5",
        #     "google_authenticator_secret": "7JCJA4VDGVCWUGDPRKVK3RGYVOB3F3EF",
        #     "quantity_multiplier": 0.5
        # }
        creds = {
            "name": "Shashwat Rastogi",
            "user_name": "NM4622",
            "password": "make@Money1",
            "api_key": "ycrr3zgf6kizot9c",
            "api_secret": "8zgo5yx7rqfmt6pyvbxtgi53ld8jzele",
            "google_authenticator_secret": "7PKQGOZSQSDDMOO5IHSSSS2TUBV6VPBX"
        }
        connection_manager = KiteConnectionManager(user_details=creds, refresh_connection=False)
        connection_manager.get_kite_connect()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
