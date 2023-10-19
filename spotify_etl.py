import requests
import base64
import json
import pandas as pd
from bs4 import BeautifulSoup


# ------------Scraping Artists Name-----------
url = 'https://kworb.net/itunes/'

# Send an HTTP GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

td_with_a = [td for td in soup.find_all('td') if td.find('a')]
list_of_artists = []
for td in td_with_a:
    link = td.find('a')
    list_of_artists.append(link.text)

# ------------Spotify Web Api-------------
# client credentials
client_id = 'd30734dd944248088a702484a17a0e61'
client_secret = '3050f1cc55f94daeaa9b6d52ca9cea12'


# --------------- Spotify Api Authorization------------


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",

    }
    result = requests.post(url, headers=headers, data=data)

    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return(token)


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


token = get_token()
# print(token)
header = get_auth_header(token)

# ----------Extraction------------


def get_artist(artist_name):
    url = f'https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1'
    response = requests.get(url, headers=header)
    artist_data = response.json()

    id = artist_data['artists']['items'][0]['id']
    name = artist_data['artists']['items'][0]['name']
    followers = artist_data['artists']['items'][0]['followers']['total']
    try:
        genre = artist_data['artists']['items'][0]['genres'][0]
    except:
        genre = "NA"
    popularity = artist_data['artists']['items'][0]['popularity']

    redefined_artist_data = {"id": id,
                             "name": name,
                             "followers": followers,
                             "genre": genre,
                             "popularity": popularity}
    return redefined_artist_data


artists_list = []
for artist in list_of_artists:
    if artist not in artists_list:
        artists_list.append(get_artist(artist))
print(artists_list)

df = pd.DataFrame(artists_list)
df.to_csv('refined_artist_details.csv')
