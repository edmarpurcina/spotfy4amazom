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

def get_token_spoty():
    usuario = input('Usuario:')
    senha = input('Senha: ')
    base = usuario+senha
    print(base)
    basic = base64.b64encode(base.encode())
    print(str(basic))
    url = 'https://api.spotify.com/api/token'
    headers = {
        'Autorization': "Basic "+str(basic),
        'Content-Type': "application/x-www-form-urlencoded"
    }
    payload = "grant_type=client_credentials"

    response = requests.request("POST", url, data=payload, headers=headers )
    print(response.text)
    exit()
get_token_spoty()
headers = {
     'Accept': ": application/json",
     'Content-Type': ": application/json",
     'Authorization': ': Bearer BQD8e9d_xsKwjrBAJTgCekzr53kqYWcSOG2jAVIFgoEEUylINT6oU3J-3c1prqKygjl4HwoWwdGYjnzwfb3-HY_MbqCjB3068ms_97W7jj29FohRCyinxWyEVqdrg5GEX5Q6qNIYuf6UGJ95_lFnWrM30z9vA6-6zAxJXskFsmQwbh7pA9c0aXXvu1VCaNnxlzE3_mS_YMz3IrsmuCk8n4j2t04bs9HHaZgBoxVEQD8U56_c3ntl_GTjkIcgAoBf5xyF4176UGbF3dcr66s"'
 }

jsontext = get_playlist_name(headers)
#playlist = json_explore_playlist(jsontext, headers)

