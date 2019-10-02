# codiing: utf-8
import base64
import sys, json, getpass
import requests

def get_playlist_name(headers):
    url = "https://api.spotify.com/v1/users/edmarpurcina/playlists"
    response = requests.request("GET", url, headers=headers)
    #print(response.text)

    json_explore_playlist(response.text, headers)

    return response.text

def get_music_name(playlistid,headers):
    url = "https://api.spotify.com/v1/playlists/"+str(playlistid)+"/tracks"
    response = requests.request("GET", url, headers=headers)
    get_json_music = json.loads(response.text)

    for i in range(0, len(get_json_music['items']), 1):
        get_name = get_json_music['items'][i]
        print("Musica: ",i,get_name['track']['name'])
    qtd_musicas = len(get_json_music['items'])
    return(qtd_musicas)

def json_explore_playlist(jsotext, headers):
    get_json = json.loads(jsotext)
    cont = 0
    for i in range( 0, len(get_json['items']), 1):
        get_name = get_json['items'][i]
        print("\nPlaylist ID: ",get_name['id'])
        print("Playlist Name: ",get_name['name'])

        qtd_musicas = get_music_name(get_name['id'],headers)
        cont += qtd_musicas

    print("Total de Musicas: ",cont)
    return

def get_token_spotify(): # Server to Server Request
    usuario = 'b0c3b87a970c4df797359dd864113be5' #input('Usuario:')
    senha = 'be33913f49ea4361b0d7473d30e7eb66' #input('Senha: ')
    #usuario = input('Usuario: ')
    #senha = input('Senha: ')

    base = usuario+':'+senha
    #print(base)
    basic = base64.b64encode(str(base).encode())
    #print(str(basic, 'utf-8'))
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': "Basic " + str(basic,'utf-8'),
        'Content-Type': "application/x-www-form-urlencoded"
    }
    payload = "grant_type=client_credentials"

    response = requests.request("POST", url, data=payload, headers=headers)
    #print(response.text)
    token_josn = json.loads(response.text)
    token = token_josn['access_token']
    print(token)

    return token

# token temporario expira a cada 3600 s
#token = 'BQDmrCsEY6GSYDfFuOstbmAtTpdEFGGjVjUiW4A6MCOwXKjEayKojaGalrPGDHgmY2QfkWrk1JmWoej8hXXtyp81aUka2FWM-E9xRBVmeGdhiR4alMObv5Cvp9tJJVQZBaXW30Ir-tPW_r4unQNCf19IGgmGh2L9TJP_F8DWMMGEPofc3MleS8KkrY-oJzBi0Pd9I-Gkge7oLSSLBqhWC-qmNpYE9m3Uz-6YTVHTfhR1NMjaVD0eBJDtTcU3EFSTLFD4jE28nbzk-juhDV8'
token = get_token_spotify()
headers = {
    'Accept': ": application/json",
    'Content-Type': ": application/json",
    'Authorization': ': Bearer ' + token
}

jsontext = get_playlist_name(headers)
#playlist = json_explore_playlist(jsontext, headers)

