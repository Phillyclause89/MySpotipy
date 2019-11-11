import unittest
import myspotipy as ms


class TestMySpotipy(unittest.TestCase):
    def setUp(self):
        print("id:", self.id())
        # Initialize Test Variables
        self.vms = ms.Main(test=True)
        self.valid_creds = self.vms.load_spoty_creds(output=True)
        self.ivms = ms.Main(test=True)
        self.invalid_creds = {"Username": 0,
                              "Scope": 0,
                              "Client_id": 0,
                              "Client_secret": 0,
                              "Redirect_uri": 0}

    def tearDown(self):
        pass

    def test___init__(self):
        print("id:", self.id())
        print("Test 1:")
        # Test __init__ method of MySpotipy with invalid creds and auto_connect off.
        self.myspot_acf_invalid = ms.MySpotipy(self.invalid_creds["Username"],
                                               self.invalid_creds["Scope"],
                                               self.invalid_creds["Client_id"],
                                               self.invalid_creds["Client_secret"],
                                               self.invalid_creds["Redirect_uri"],
                                               auto_connect=False)
        print("Test 1.1.1:")
        self.assertIsInstance(self.myspot_acf_invalid,
                              ms.MySpotipy,
                              f"{self.id()}: IsInstance Failure: self.myspot_acf_invalid is not an instance of the"
                              f" MySpotipy class.")
        print("Test 1.1.2:")
        self.assertEqual(self.invalid_creds["Username"],
                         self.myspot_acf_invalid.username,
                         f"{self.id()}: IsEqual Failure: self.invalid_creds['Username'] ({self.invalid_creds['Username']}"
                         f")does not equal self.myspot_acf_invalid.username({self.myspot_acf_invalid.username})")
        print("Test 1.1.3:")
        self.assertEqual(self.invalid_creds["Scope"],
                         self.myspot_acf_invalid.scope,
                         f"{self.id()}: IsEqual Failure: self.invalid_creds['Scope'] ({self.invalid_creds['Scope']})"
                         f"does not equal self.myspot_acf_invalid.scope({self.myspot_acf_invalid.scope})")
        print("Test 1.1.4:")
        self.assertEqual(self.invalid_creds["Client_id"],
                         self.myspot_acf_invalid.client_id,
                         f"{self.id()}: IsEqual Failure: self.invalid_creds['Client_id'] ({self.invalid_creds['Client_id']})"
                         f"does not equal self.myspot_acf_invalid.client_id({self.myspot_acf_invalid.client_id})")
        print("Test 1.1.5:")
        self.assertEqual(self.invalid_creds["Client_secret"],
                         self.myspot_acf_invalid.client_secret,
                         f"{self.id()}: IsEqual Failure: self.invalid_creds['Client_secret'] ({self.invalid_creds['Client_secret']})"
                         f"does not equal self.myspot_acf_invalid.client_secret({self.myspot_acf_invalid.client_secret})")
        print("Test 1.1.6:")
        self.assertEqual(self.invalid_creds["Redirect_uri"],
                         self.myspot_acf_invalid.redirect_uri,
                         f"{self.id()}: IsEqual Failure: self.invalid_creds['Redirect_uri'] ({self.invalid_creds['Redirect_uri']})"
                         f"does not equal self.myspot_acf_invalid.redirect_uri({self.myspot_acf_invalid.redirect_uri})")

        print("Test 1.2.0:")
        # Test Exception is tossed if __init__ method gets invalid creds and auto_connect is on.
        with self.assertRaises(Exception) as e:
            self.myspot_act_invalid = ms.MySpotipy(self.invalid_creds["Username"],
                                                   self.invalid_creds["Scope"],
                                                   self.invalid_creds["Client_id"],
                                                   self.invalid_creds["Client_secret"],
                                                   self.invalid_creds["Redirect_uri"],
                                                   auto_connect=True)

        print("Test 1.3.0:")
        # Test __init__ method of MySpotipy with valid creds and auto_connect off.
        self.myspot_acf_valid = ms.MySpotipy(self.valid_creds["Username"],
                                             self.valid_creds["Scope"],
                                             self.valid_creds["Client_id"],
                                             self.valid_creds["Client_secret"],
                                             self.valid_creds["Redirect_uri"],
                                             auto_connect=False)
        print("Test 1.3.1:")
        self.assertIsInstance(self.myspot_acf_valid,
                              ms.MySpotipy,
                              f"{self.id()}: IsInstance Failure: self.myspot_acf_valid is not an instance of the"
                              f" MySpotipy class.")
        print("Test 1.3.2:")
        self.assertEqual(self.valid_creds["Username"],
                         self.myspot_acf_valid.username,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Username'] ({self.valid_creds['Username']})"
                         f"does not equal self.myspot_acf_valid.username({self.myspot_acf_valid.username})")
        print("Test 1.3.3:")
        self.assertEqual(self.valid_creds["Scope"],
                         self.myspot_acf_valid.scope,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Scope'] ({self.valid_creds['Scope']})"
                         f"does not equal self.myspot_acf_valid.username({self.myspot_acf_valid.scope})")
        print("Test 1.3.4:")
        self.assertEqual(self.valid_creds["Client_id"],
                         self.myspot_acf_valid.client_id,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Client_id'] ({self.valid_creds['Client_id']})"
                         f"does not equal self.myspot_acf_valid.client_id({self.myspot_acf_valid.client_id})")
        print("Test 1.3.5:")
        self.assertEqual(self.valid_creds["Client_secret"],
                         self.myspot_acf_valid.client_secret,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Client_secret'] ({self.valid_creds['Client_secret']})"
                         f"does not equal self.myspot_acf_valid.client_secret({self.myspot_acf_valid.client_secret})")
        print("Test 1.3.6:")
        self.assertEqual(self.valid_creds["Redirect_uri"],
                         self.myspot_acf_valid.redirect_uri,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Redirect_uri'] ({self.valid_creds['Redirect_uri']})"
                         f"does not equal self.myspot_acf_valid.redirect_uri({self.myspot_acf_valid.redirect_uri})")

        print("Test 1.4.0:")
        # Test  __init__ method of MySpotipy with valid creds and auto_connect is on.
        self.myspot_act_valid = ms.MySpotipy(self.valid_creds["Username"],
                                             self.valid_creds["Scope"],
                                             self.valid_creds["Client_id"],
                                             self.valid_creds["Client_secret"],
                                             self.valid_creds["Redirect_uri"],
                                             auto_connect=True)
        print("Test 1.4.1:")
        self.assertIsInstance(self.myspot_act_valid,
                              ms.MySpotipy,
                              f"{self.id()}: IsInstance Failure: self.myspot_act_valid is not an instance of the "
                              f"MySpotipy class.")
        print("Test 1.4.2:")
        self.assertEqual(self.valid_creds["Username"],
                         self.myspot_act_valid.username,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Username'] ({self.valid_creds['Username']}) "
                         f"does not equal self.myspot_act_valid.username({self.myspot_act_valid.username})")
        print("Test 1.4.3:")
        self.assertEqual(self.valid_creds["Scope"],
                         self.myspot_act_valid.scope,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Scope'] ({self.valid_creds['Scope']}) "
                         f"does not equal self.myspot_act_valid.scope({self.myspot_act_valid.scope})")
        print("Test 1.4.4:")
        self.assertEqual(self.valid_creds["Client_id"],
                         self.myspot_act_valid.client_id,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Client_id'] ({self.valid_creds['Client_id']}) "
                         f"does not equal self.myspot_act_valid.client_id({self.myspot_act_valid.client_id})")
        print("Test 1.4.5:")
        self.assertEqual(self.valid_creds["Client_secret"],
                         self.myspot_act_valid.client_secret,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Client_secret'] ({self.valid_creds['Client_secret']}) "
                         f"does not equal self.myspot_act_valid.client_secret({self.myspot_act_valid.client_secret})")
        print("Test 1.4.6:")
        self.assertEqual(self.valid_creds["Redirect_uri"],
                         self.myspot_act_valid.redirect_uri,
                         f"{self.id()}: IsEqual Failure: self.valid_creds['Redirect_uri'] ({self.valid_creds['Redirect_uri']}) "
                         f"does not equal self.myspot_act_valid.redirect_uri({self.myspot_act_valid.redirect_uri})")
        print("Test 1.4.7:")
        self.assertTrue(self.myspot_act_valid.token,
                        f"{self.id()}: IsTrue Failure: self.myspot_act_valid.token {self.myspot_act_valid.token} "
                        f"does not equal True")
        print("Test 1.4.8:")
        self.assertIsInstance(self.myspot_act_valid.sp,
                              ms.spotipy.client.Spotify,
                              f"{self.id()}: IsInstance Failure: ms.spotipy.client.Spotify is not an instance of the "
                              f"spotipy.client.Spotify class.")

    def test_get_token(self):
        print("id:", self.id())
        with self.assertRaises(Exception) as e:
            do_something()
        pass

    def test_liked_songs_to_csv(self):
        print("id:", self.id())
        pass

    def test_update_token(self):
        print("id:", self.id())
        pass


if __name__ == '__main__':
    unittest.main()
