import json
import spotipy
import webbrowser
import sys
import spotipy.util as util
import spotipy.oauth2 as oauth2
from json.decoder import JSONDecodeError
import collections
import queue
import random


def get_id_for_artist(artist_name):
    searchResults = spotify.search(artist_name, 1, 0, "artist")
    artist_id = searchResults['artists']['items'][0]['id']
    return artist_id


def get_related_artists(id):
    child_artists = []
    related_artists = spotify.artist_related_artists(id)
    for child_artist in related_artists['artists']:
        artist_node = artist(child_artist['id'], child_artist['name'])
        child_artists.append(artist_node)
    return child_artists

def bfs_shortest_path(start_artist, goal_artist):
    explored = []
    queue = [[start_artist]]
    while queue:
        path = queue.pop(0)
        artist = path[-1]
        if artist not in explored:
            neighbours = get_related_artists(artist.id)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal_artist:
                    return new_path
            explored.append(artist)



client_id = ""
client_secret = ""

artist_name = sys.argv[1]
artist_name2 = sys.argv[2]

artist = collections.namedtuple('artist', 'id name')
credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

if token:
    spotify = spotipy.Spotify(auth=token)
    spotify.trace = False
    artists = []

    tmp_artist_id = get_id_for_artist(artist_name)
    tmp_artist_id2 = get_id_for_artist(artist_name2)

    start_artist = artist(tmp_artist_id, artist_name)
    goal_artist = artist(tmp_artist_id2, artist_name2)
    print (start_artist.name)
    print(goal_artist.name)
    path = bfs_shortest_path(start_artist, goal_artist)
    print("Path found! Nr of degrees:", len(path)-1)
    print("Path:")
    for i in range(len(path)-1):
        print(path[i].name, "-->", end =" ")
    print(path[len(path)-1].name)
