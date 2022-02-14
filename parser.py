import os
import requests
from bs4 import BeautifulSoup
from constants import DOMAIN, USER_AGENT, PAGES_LIMIT


def get_urls():
    urls = []
    for i in range(PAGES_LIMIT):
        print("Accediendo a página {}...".format(i))
        response = requests.get(DOMAIN.format(n=i), headers={'User-Agent': USER_AGENT})
        data = response.text
        # etiqueta tipo article, contiene clase "tag-enrique-de-diego"
        soup = BeautifulSoup(data, 'html.parser')

        for j in soup.find_all('article'):
            if "tag-enrique-de-diego" in j['class']:
                urls.append(j.header.a['href'])        
    # Ahora se escriben todas las url al fichero
    links_file = open('urls.txt', 'w')
    for i in urls:
        links_file.write(i)   # recoge los enlaces
        links_file.write("\n")
    links_file.close()

def get_posts():
    with open('urls.txt') as f:
        for line in f:
            print("Reading:", line, end="")
            response = requests.get(line, headers={'User-Agent': USER_AGENT})
            data = response.text

            soup = BeautifulSoup(data, 'html.parser')
            article = soup.find('article')
            id = article['id']
            if os.path.isfile("texts/{}.txt".format(id)):
                print("Se ha llegado a un post ya guardado. Me salgo.")
                exit()  # se ha llegado a posts que ya existen
            text_file = open("texts/{}.txt".format(id), 'w')
            text = ""
            for p in article.find_all('p'):
                if "Enrique de Diego" in p.getText():
                    continue
                text += p.getText()
                text += "\n"
            text_file.write(text)
            print("DONE")

if __name__ == '__main__':
    get_urls()
    get_posts()
