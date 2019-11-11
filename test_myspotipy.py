import unittest
import myspotipy as ms


class TestMySpotipy(unittest.TestCase):
    def setUp(self):
        self.vms = ms.Main(test=True)
        self.valid_creds = self.vms.load_spoty_creds(output=True)
        self.ivms = ms.Main(test=True)
        self.invalid_creds = {"Username": 0,
                              "Scope": 0,
                              "Client_id": 0,
                              "Client_secret": 0,
                              "Redirect_uri": 0}
        # for k in self.valid_creds:
        #     print("Valid:", k, self.valid_creds[k])
        # for k in self.invalid_creds:
        #     print("Invalid:", k, self.invalid_creds[k])

    def tearDown(self):
        pass

    def test___init__(self):
        self.myspot_acf_invalid = ms.MySpotipy(self.invalid_creds["Username"],
                                               self.invalid_creds["Scope"],
                                               self.invalid_creds["Client_id"],
                                               self.invalid_creds["Client_secret"],
                                               self.invalid_creds["Redirect_uri"],
                                               auto_connect=False)
        self.assertIsInstance(self.myspot_acf_invalid, ms.MySpotipy)
        with self.assertRaises(Exception) as e:
            self.myspot_act_invalid = ms.MySpotipy(self.invalid_creds["Username"],
                                                   self.invalid_creds["Scope"],
                                                   self.invalid_creds["Client_id"],
                                                   self.invalid_creds["Client_secret"],
                                                   self.invalid_creds["Redirect_uri"],
                                                   auto_connect=True)
            self.assertIsInstance(self.myspot_act_invalid, ms.MySpotipy)

        self.myspot_acf_valid = ms.MySpotipy(self.valid_creds["Username"],
                                             self.valid_creds["Scope"],
                                             self.valid_creds["Client_id"],
                                             self.valid_creds["Client_secret"],
                                             self.valid_creds["Redirect_uri"],
                                             auto_connect=False)
        self.assertIsInstance(self.myspot_acf_invalid, ms.MySpotipy)
        self.myspot_act_valid = ms.MySpotipy(self.valid_creds["Username"],
                                             self.valid_creds["Scope"],
                                             self.valid_creds["Client_id"],
                                             self.valid_creds["Client_secret"],
                                             self.valid_creds["Redirect_uri"],
                                             auto_connect=True)
        self.assertIsInstance(self.myspot_acf_invalid, ms.MySpotipy)

    def test_get_token(self):
        with self.assertRaises(Exception) as e:
            do_something()
        pass

    def test_liked_songs_to_csv(self):
        pass

    def test_update_token(self):
        pass


if __name__ == '__main__':
    unittest.main()
