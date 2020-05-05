import csv
from bidi.algorithm import get_display
import random
# from urllib.parse import urlencode
import string
import requests

headers = {
    'authority': 'www.atzuma.co.il',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://www.atzuma.co.il',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.atzuma.co.il/lilo1212',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '',
}


session = requests.session()
# proxies = {
#     'http':'socks5://127.0.0.1:9051',
#     'https':'socks5:/127.0.0.1:9051'
# }
session.proxies['http'] = 'socks5h://localhost:9051'
session.proxies['https'] = 'socks5h://localhost:9051'


with open('hebrew_names.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',',)
    line_count = 0
    current_aid = 1588198233
    data = ', '.join([ "'" + row[0] + "'" for row in csv_reader ])

with open('naemes.txt', 'w', encoding="utf8") as fd:
    fd.write(data)