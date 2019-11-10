import spotipy
import spotipy.util as util


class MySpotipy:
    def __init__(self,
                 username,
                 scope,
                 client_id,
                 client_secret,
                 redirect_uri='http://localhost:8888/callback/'):
        self.username = username
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token = self.get_token()
        self.sp = spotipy.Spotify(auth=self.token)

    def get_token(self):
        t = util.prompt_for_user_token(
            username=self.username,
            scope=self.scope,
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri
        )
        if t:
            return t
        raise Exception("Failed to get token")

    def liked_songs_to_csv(self, **kwargs):
        from pandas import DataFrame as pdDF
        columns = ['Title', 'Artists']
        if "album" in kwargs:
            columns.append("Album")
        if "album_type" in kwargs:
            columns.append("Album Type")
        if "album_type" in kwargs:
            columns.append("Album Type")

        df = pdDF(columns=columns)
        off = 0
        i = 0
        while True:
            results = self.sp.current_user_saved_tracks(limit=50, offset=off)
            off += 50
            for item in results['items']:
                row = [item['track']['name'], item['track']['artists'][0]['name']]
                if "album" in kwargs:
                    row.append(item['track']['album']['name'])
                if "album_type" in kwargs:
                    row.append(item['track']['album']['album_type'])
                if "album_type" in kwargs:
                    row.append(item['track']['album']['album_type'])
                df.loc[i] = row
                i += 1
            if results["next"] is None:
                break
        df.to_csv('MySpotipyLikedSongs.csv')

    def update_token(self, update=True, **kwargs):
        if "username" in kwargs:
            self.username = kwargs.get("username")
        if "scope" in kwargs:
            self.scope = kwargs.get("scope")
        if "client_id" in kwargs:
            self.client_id = kwargs.get("scope")
        if "client_secret" in kwargs:
            self.client_secret = kwargs.get("client_secret")
        if "redirect_uri" in kwargs:
            self.redirect_uri = kwargs.get("redirect_uri")
        if update:
            self.token = self.get_token()
            self.sp = spotipy.Spotify(auth=self.token)


class Main:
    def __init__(self):
        self.creds = {}
        self.load_spoty_creds()
        ms = MySpotipy(self.creds["Username"],
                       self.creds["Scope"],
                       self.creds["Client_id"],
                       self.creds["Client_secret"],
                       self.creds["Redirect_uri"])
        ms.liked_songs_to_csv()
        print("done")

    def load_spoty_creds(self):
        import pickle
        try:
            pickle_in = open(r'C:/Users/Philip/AppData/Roaming/MySpotipyData/MySpotipyCreds.pickle', "rb")
            self.creds = pickle.load(pickle_in)
            pickle_in.close()
        except FileNotFoundError:
            self.creds = {"Username": input("Enter your Spotify Username:\n"),
                          "Scope": input("Enter your Spotify Scope:\n"),
                          "Client_id": input("Enter your Spotify Client ID:\n"),
                          "Client_secret": input("Enter your Client Secret:\n"),
                          "Redirect_uri": input("Enter your Spotify Redirect URL:\n")}
            pickle_out = open(r'C:/Users/Philip/AppData/Roaming/MySpotipyData/MySpotipyCreds.pickle', "wb")
            pickle.dump(self.creds, pickle_out)
            pickle_out.close()


if __name__ == '__main__':
    Main()
