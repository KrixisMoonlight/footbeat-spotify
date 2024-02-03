import spotipy
from spotipy.oauth2 import SpotifyOAuth


speedURIDict = {
    5: "37i9dQZF1EIVvFvv7tCfYv?si=1ab0487c01ef4d25",
    5.45: "37i9dQZF1EIgOKtiospcqN?si=b14f930bc7834b5e",
    6: "37i9dQZF1EIgrZKdA44WQK?si=b1d00ea9de2741f5",
    6.67: "37i9dQZF1EIdYV92VKrjuC?si=9bd90093931b47b6",
    7.5: "37i9dQZF1EIgfIackHptHl?si=6c896e3b21f842b8",
    8.57: "37i9dQZF1EIerWUrjG2OiJ?si=803596b2dbd4471c",
    10: "37i9dQZF1EIcID9rq1OAoH?si=a98b84e4b2e44000"
}

SPOTIPY_CLIENT_ID = "410611533e5444388d9aa46ddcb4e72e"
SPOTIPY_CLIENT_SECRET = "72bfb3db17334e44b5f5f4d3265cfebd"
scope = "user-read-playback-state user-modify-playback-state user-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri="http://127.0.0.1:8080/"
))

def playPlaylist(speed):
    if sp.me()["product"] != "premium":
        print("NO")
        return False
    
    if speed <= 5.22:
        playlist_uri = speedURIDict[5]
    elif speed <= 5.73:
        playlist_uri = speedURIDict[5.45]
    elif speed <= 6.33:
        playlist_uri = speedURIDict[6]
    elif speed <= 7.08:
        playlist_uri = speedURIDict[6.67]
    elif speed <= 8.04:
        playlist_uri = speedURIDict[7.5]
    elif speed <= 9.28:
        playlist_uri = speedURIDict[8.57]
    else:
        playlist_uri = speedURIDict[10]

    try: #in case there is no active device
        sp.start_playback(context_uri=playlist_uri)
    except:
        return "nodevice"
    else: 
        sp.start_playback(context_uri=playlist_uri)

    return True

#test 
playPlaylist(5.7)