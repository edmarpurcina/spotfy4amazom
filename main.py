# codiing: utf-8
import base64
import sys, json, getpass
import requests

def get_playlist_name(headers):
    url = "https://api.spotify.com/v1/users/playlists"
    response = requests.request("GET", url, headers=headers)
    print(response.text)

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
    usuario = 'usuario api spotify'
    senha = 'senha api spotify'
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
    #exit()
    return token

# token temporario expira a cada 3600 s
#token = ''
token = get_token_spotify()
headers = {
    'Accept': ": application/json",
    'Content-Type': ": application/json",
    'Authorization': ': Bearer ' + token
}

jsontext = get_playlist_name(headers)
#playlist = json_explore_playlist(jsontext, headers)

