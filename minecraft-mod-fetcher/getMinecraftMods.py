import json
import os
from typing import BinaryIO, TextIO

import cfscrape
from bs4 import BeautifulSoup, ResultSet
from cfscrape import CloudflareScraper

URL: str = "https://www.curseforge.com/minecraft/mc-mods?filter-game-version=2020709689:6756&filter-sort=2&page={current_page}"
FILE: str = "cache/output{current_page}.html"


def getModsForPage(count: int):
    if os.path.isfile(FILE.format(current_page=count)):
        file: BinaryIO = open(FILE.format(current_page=count), 'rb')
        content: bytes = file.read()
    else:
        scraper: CloudflareScraper = cfscrape.create_scraper()
        content = scraper.get(URL.format(current_page=count)).content
        file = open(FILE.format(current_page=count), 'wb')
        file.write(content)
    return content


modList = []
for x in range(1, 21):
    soup: BeautifulSoup = BeautifulSoup(getModsForPage(x), features="html.parser")
    result: ResultSet = soup.find_all("div", class_="my-2")

    for entry in result:
        link: str = entry.div.div.div.a['href']
        name: str = entry.find("h3").text
        modList.append({"name": name, "link": link})

    file: TextIO = open("output.json", "w")
    json.dump(modList, file)
