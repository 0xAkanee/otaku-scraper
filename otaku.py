import os
import re  # regex //
import requests
from bs4 import BeautifulSoup as bs
r = requests.Session()


def search(katakunci):
    url = f"https://otakudesu.moe/?s={katakunci}&post_type=anime"
    req = r.get(url)
    parsing = bs(req.text, "html.parser")
    allAnime = parsing.find("div", attrs={"class": "page"}).findAll(
        "li", attrs={"style": "list-style:none;"})
    nomor = 1
    list_url = []
    for anime in allAnime:
        judul = anime.find("h2").find("a").text
        linknya = anime.find("h2").find("a").get("href")
        print(nomor, judul)
        list_url.append(linknya)
        nomor += 1

    pilihan = input("Masukkan nomor anime: ")
    link_anime = list_url[int(pilihan)-1]
    os.system("cls" if os.name == "nt" else "clear")
    req = r.get(link_anime)
    parsing = bs(req.text, "html.parser")
    judul = parsing.find("h1").text
    print("~"*45)
    print("Judul Anime : ", judul)
    print("~"*45)
    detail = parsing.find("div", attrs={"class": "infozingle"}).findAll("p")
    for detail_info in detail:
        print(detail_info.text)

    print("~"*45)
    sinopsis = parsing.find("div", attrs={"class": "sinopc"}).text
    print(sinopsis)
    print("~"*45)
    episode = parsing.findAll("div", attrs={"class": "episodelist"})
    listeps = []
    nomor = 1
    for link in episode:
        episodelist = link.findAll("li")
        for eps in episodelist:
            judul = eps.find("a").text
            link = eps.find("a").get("href")
            print(nomor, judul)
            listeps.append(link)
            nomor += 1
    piliheps = input("Pilih Episode :")
    linkeps = listeps[int(piliheps)-1]
    os.system("cls" if os.name == "nt" else "clear")
    req = r.get(linkeps)
    parsing = bs(req.text, "html.parser")
    judul = parsing.find("div", attrs={"class": "download"}).find("h4").text
    link = parsing.find("div", attrs={"class": "download"}).findAll("li")
    print("=" * 5, "Link Unduhan", "="*5)
    for dunlud in link:
        linkdl = dunlud.find("strong").text
        print("\n{}".format(linkdl))
        for dl in dunlud.find_all('a'):
            if len(dl.string) < 10:
                spasi = 12 - len(dl.string)
                print(dl.string, " " * spasi, dl.get('href'))
            else:
                print(dl.string, " " * 2, dl.get('href'))


os.system("cls" if os.name == "nt" else "clear")
katakunci = input("Masukkan nama anime :")
search(katakunci)
