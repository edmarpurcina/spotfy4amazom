from django.shortcuts import render
import http.client, json, base64

# Create your views here.


def home(request):
    import http.client

    conn = http.client.HTTPSConnection("accounts.spotify.com")

    headers = {
        'cache-control': "no-cache",
        'postman-token': "fb0edc0b-8f05-c668-b1a9-f39dc3c9fa27"
    }

    conn.request("GET",
                 "/authorize?client_id=b0c3b87a970c4df797359dd864113be5&response_type=code&redirect_uri=https%3A%2F%2F127.0.0.1%3A8000%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    #return HttpResponse(conn.getresponse())
    return render(request, 'getmusic/index.html', data.decode("utf-8"))
