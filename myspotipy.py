import spotipy
import spotipy.util as util


class MySpotipy:
    def __init__(self,
                 username,
                 scope,
                 client_id,
                 client_secret,
                 redirect_uri='http://localhost:8888/callback/',
                 auto_connect=True):
        self.username = username
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        if auto_connect:
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

    def liked_songs_to_csv(self, *args):
        from pandas import DataFrame as pdDF
        columns = ['title', 'artist(s)']
        keys = {"added_at": lambda it: it['added_at'],
                "album": lambda it: it['track']['album']['name'],
                "album_type": lambda it: it['track']['album']['album_type'],
                "release_date": lambda it: it['track']['album']['release_date'],
                "total_tracks": lambda it: it['track']['album']['total_tracks'],
                "disc_number": lambda it: it['track']['disc_number'],
                "duration_ms": lambda it: it['track']['duration_ms'],
                "explicit": lambda it: it['track']['explicit'],
                "popularity": lambda it: it['track']['popularity'],
                "track_number": lambda it: it['track']['track_number'],
                "id": lambda it: it['track']['id'],
                "is_local": lambda it: it['track']['is_local']
                }
        for kw in args:
            if kw.lower() in keys:
                columns.append(kw)
        df = pdDF(columns=columns)
        off = 0
        i = 0
        while True:
            results = self.sp.current_user_saved_tracks(limit=50, offset=off)
            off += 50
            for item in results['items']:
                row = [item['track']['name'], item['track']['artists'][0]['name']]
                if len(columns) > 2:
                    for kw in columns[2:]:
                        row.append(keys[kw](item))
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
    def __init__(self, test=False):
        if not test:
            self.creds = {}
            self.load_spoty_creds()
            ms = MySpotipy(self.creds["Username"],
                           self.creds["Scope"],
                           self.creds["Client_id"],
                           self.creds["Client_secret"],
                           self.creds["Redirect_uri"])
            ms.liked_songs_to_csv("album",
                                  "added_at",
                                  "album_type",
                                  "release_date",
                                  "total_tracks",
                                  "disc_number",
                                  "duration_ms",
                                  "explicit",
                                  "popularity",
                                  "track_number",
                                  "external_urls",
                                  "id",
                                  "is_local")
            print("done")
        else:
            print("Test Init Complete")

    def load_spoty_creds(self, output=False):
        import pickle
        import os
        # \MySpotipyData folder needs to preexist. Must Fix!
        path = os.getenv("LOCALAPPDATA") + "\MySpotipyData\MySpotipyCreds.pickle"
        try:
            pickle_in = open(path, "rb")
            if not output:
                self.creds = pickle.load(pickle_in)
            else:
                c = pickle.load(pickle_in)
            pickle_in.close()
            if output:
                return c
        except FileNotFoundError:
            self.creds = {"Username": input("Enter your Spotify Username:\n"),
                          "Scope": input("Enter your Spotify Scope:\n"),
                          "Client_id": input("Enter your Spotify Client ID:\n"),
                          "Client_secret": input("Enter your Client Secret:\n"),
                          "Redirect_uri": input("Enter your Spotify Redirect URL:\n")}
            pickle_out = open(path, "wb")
            pickle.dump(self.creds, pickle_out)
            pickle_out.close()


if __name__ == '__main__':
    Main()
