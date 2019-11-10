import spotipy
import spotipy.util as util


class MySpotipy:
    def __init__(self, username, scope, client_id, client_secret, redirect_uri='http://localhost:8888/callback/'):
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
        if kwargs["album"]:
            columns.append("Album")
        if kwargs["album_type"]:
            columns.append("Album Type")
        if kwargs["album_type"]:
            columns.append("Album Type")

        df = pdDF(columns=columns)
        off = 0
        i = 0
        while True:
            results = self.sp.current_user_saved_tracks(limit=50, offset=off)
            off += 50
            for item in results['items']:
                row = [item['track']['name'], item['track']['artists'][0]['name']]
                if kwargs["album"]:
                    row.append(item['track']['album']['name'])
                if kwargs["album_type"]:
                    row.append(item['track']['album']['album_type'])
                if kwargs["album_type"]:
                    row.append(item['track']['album']['album_type'])
                df.loc[i] = row
                i += 1
            if results["next"] is None:
                break
        df.to_csv('Finally.csv')

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


if __name__ == '__main__':
    creds = []
    with open('C:\Users\Philip\AppData\Roaming\MySpotipyData\MySpotipyCreds.txt', 'r') as f:
        for line in f:
            creds.append(line)
    ms = MySpotipy(creds[0], creds[1], creds[2], creds[3])
    ms.liked_songs_to_csv()
    print("done")
