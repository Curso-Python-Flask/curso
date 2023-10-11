import urllib.request, json

url = "https://api.themoviedb.org/3/movie/popular?api_key=a5cbd2ce5a2a71d078031e22cd831b13"

resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])