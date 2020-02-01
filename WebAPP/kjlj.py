import requests
import json

url = 'https://ltool.net/chinese-simplified-and-traditional-characters-pinyin-to-katakana-converter-in-simplified-chinese.php'

data = {
    'contents': 'zhao',
    'firstinput': 'OK',
    'option': '1',
    'optionext': 'zenkaku'
}
hearder = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'ltool.net',
    'Cookie': '__utmc=79062217; __utmz=79062217.1578708086.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=79062217.728046565.1578708085.1578708085.1578708085.1; __utmt=1; __utmb=79062217.12.10.1578708086'
}
a = requests.post(url, data, headers=hearder)
print(a.content)
