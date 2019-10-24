from django.shortcuts import render
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from spotipy.oauth2 import SpotifyOAuth
from django.contrib.admin.views.decorators import staff_member_required
import http.client, json, base64, requests, os, spotipy
import spotipy.util as util

# Create your views here.


def home(request):
    #import http.client

    url = "https://accounts.spotify.com/authorize"
    querystring = {"client_id": "b0c3b87a970c4df797359dd864113be5", "response_type": "code",
                   "redirect_uri": "https://localhost", "scope": "user-read-private user-read-email,user-library-read",
                   "state": "34fFs29kd09"}

    '''headers = {
        'cache-control': "no-cache",
        'postman-token': "f1568337-0e77-a733-f124-167611b738c1"
    }'''

    response = requests.request("GET", url,  params=querystring)
    # print(response.text)
    print(response.text)
    teste = {}
    teste['url'] = response.text
    #return redirect(response.text)
    return render(request, 'getmusic/index.html', teste)
    #return HttpResponse( )

@login_required
def logado(request, *args, **kwargs):
    user_spotify ={}
    user_spotify['user'] = request.user
    user_spotify['id'] = request.user.id
    user_spotify['email'] = request.user.email

    print(request.user)
    print('#####', user_spotify)

    return render(request, 'getmusic/home.html', user_spotify)

