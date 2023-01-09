import requests
import lxml.html as html
import pandas as pd

HOME_URL = 'https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon_seg%C3%BAn_la_Pok%C3%A9dex_de_Paldea'
URL_POKES = 'https://www.wikidex.net'

LINK_BY_NAME = '//table/tbody/tr/td[4]/a/@href'
NAME_POKE = '//*[@id="Paldea-0"]/table/tbody/tr/td[4]/a/@title'
TYPE_1 = '//tr[@title="Tipos a los que pertenece"]/td/a[1]/@title'
TYPE_2 = '//tr[@title="Tipos a los que pertenece"]/td/a[2]/@title'
MAX_PS = '//table[@class="tabpokemon"][1]/tbody/tr[2]/td[6]/text()'
MAX_ATTACK = '//table[@class="tabpokemon"][1]/tbody/tr[3]/td[6]/text()'
MAX_DEFENCE = '//table[@class="tabpokemon"][1]/tbody/tr[4]/td[6]/text()'
MAX_SPATTACK = '//table[@class="tabpokemon"][1]/tbody/tr[5]/td[6]/text()'
MAX_SPDEFENCE = '//table[@class="tabpokemon"][1]/tbody/tr[6]/td[6]/text()'
MAX_SPEED = '//table[@class="tabpokemon"][1]/tbody/tr[7]/td[6]/text()'
MIN_PS = '//table[@class="tabpokemon"][1]/tbody/tr[2]/td[5]/text()'
MIN_ATTACK = '//table[@class="tabpokemon"][1]/tbody/tr[3]/td[5]/text()'
MIN_DEFENCE = '//table[@class="tabpokemon"][1]/tbody/tr[4]/td[5]/text()'
MIN_SPATTACK = '//table[@class="tabpokemon"][1]/tbody/tr[5]/td[5]/text()'
MIN_SPDEFENCE = '//table[@class="tabpokemon"][1]/tbody/tr[6]/td[5]/text()'
MIN_SPEED = '//table[@class="tabpokemon"][1]/tbody/tr[7]/td[5]/text()'


new_links = []
pokelist = []

def parse_info(link, link2, num):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            link_name = response.content.decode('utf-8')
            parsed = html.fromstring(link_name)
            name = parsed.xpath('//table/tbody/tr[' + str(num+2) + ']/td[4]/a/@title')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)    


    try:
        response = requests.get(link2)
        if response.status_code == 200:
            link_name = response.content.decode('utf-8')
            parsed = html.fromstring(link_name)
            type1 = parsed.xpath(TYPE_1)
            type2 = parsed.xpath(TYPE_2)
            for m in range(5):
                if len(parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[1]/th[2]/text()')) > 0:
                    if parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[1]/th[2]/text()')[0] == "Características base\n":
                        max_ps = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[2]/td[6]/text()')
                        max_at = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[3]/td[6]/text()')
                        max_df = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[4]/td[6]/text()')
                        max_spat = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[5]/td[6]/text()')
                        max_spdf = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[6]/td[6]/text()')
                        max_spd = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[7]/td[6]/text()')
                        min_ps = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[2]/td[5]/text()')
                        min_at = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[3]/td[5]/text()')
                        min_df = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[4]/td[5]/text()')
                        min_spat = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[5]/td[5]/text()')
                        min_spdf = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[6]/td[5]/text()')
                        min_spd = parsed.xpath('//table[@class="tabpokemon"][' + str(m) + ']/tbody/tr[7]/td[5]/text()')
                        break
                else:
                    max_ps = parsed.xpath(MAX_PS)
                    max_at = parsed.xpath(MAX_ATTACK)
                    max_df = parsed.xpath(MAX_DEFENCE)
                    max_spat = parsed.xpath(MAX_SPATTACK)
                    max_spdf = parsed.xpath(MAX_SPDEFENCE)
                    max_spd = parsed.xpath(MAX_SPEED)
                    min_ps = parsed.xpath(MIN_PS)
                    min_at = parsed.xpath(MIN_ATTACK)
                    min_df = parsed.xpath(MIN_DEFENCE)
                    min_spat = parsed.xpath(MIN_SPATTACK)
                    min_spdf = parsed.xpath(MIN_SPDEFENCE)
                    min_spd = parsed.xpath(MIN_SPEED)
            return (name, type1, type2, max_ps, max_at, max_df, max_spat, max_spdf, max_spd, min_ps, min_at, min_df, min_spat, min_spdf, min_spd)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            starterlink = parsed.xpath(LINK_BY_NAME)
            for i in range(400):
                new_links.append(URL_POKES + starterlink[i])
            i = 0
            for link in new_links:
                pokelist.append(parse_info(HOME_URL, link, i))
            #for j in range(30):
            #    pokelist.append(parse_info(HOME_URL, new_links[j], i))
                i += 1
                print(i)
            df = pd.DataFrame(pokelist)
            df.to_csv('datos2.csv', header=False)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()
