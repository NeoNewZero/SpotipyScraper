import spotipy
import spotipy.oauth2

CLIENT_ID = ''
CLIENT_SECRET = ''
CLIENT_REDIRECT_URI = 'http://localhost:8888' # May need to escape the double backslashes

scp = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=scp)

results = sp.search(q='weezer', limit=50)

for i, t in enumerate(results['tracks']['items']):
    print ' ', i, t['name']

print 'NOW STALKING MYSELF'

user_results = sp.user_playlists('')

print user_results.items()