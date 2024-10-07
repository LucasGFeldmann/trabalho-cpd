import requests
from NFCE import NFCE

urls = open('urls.txt', 'r')

file = open("resultado.txt", "w")
for url in urls:
    if url.rstrip() == '':
        break
    cabeca = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}
    response = requests.get(url.rstrip(), headers=cabeca)



    nfce = NFCE(response.text)


    file.write(nfce.json_data() + '\n' )
file.close()


urls.close()
