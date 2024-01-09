import requests as r
from bs4 import BeautifulSoup
from colorama import Fore as f
import re
import json

class Main():
    def __init__(self):
        self.data = []
        url = 'https://www.ucheba.ru/for-abiturients/vuz/ege/'
        self.subjects = [
            'mathematics',
            'chemistry',
            'social',
            'history',
            'foreignlanguage',
            'biology',
            'geography',
            'physics',
            'informatics',
            'literature'
        ]
        self.subjects2 = list(self.subjects)
        self.urls = []
        for i in self.subjects:
            for j in self.subjects2:
                self.urls.append(f'{url}{i}/{j}/')
            self.subjects2.pop(0)

        for k, url in enumerate(self.urls):
            print(k)
            print(url)
            list_of_names = []
            for i in range(0, 200,10):
                print(i)
                soup = BeautifulSoup(r.get(f'{url}?s={i}').text, 'lxml')
                univers = soup.find_all('section', 'search-results-item')
                for block in univers:
                    uni_name = block.find(attrs={'class':'search-results-title'}).a.text
                    
                    if uni_name in list_of_names:
                        break
                    list_of_names.append(uni_name)

                    url_for_data = block.find('a', 'search-results-more-info').attrs['data-programs-url']
                    data = self.getData(f'https://www.ucheba.ru{url_for_data}')
                    self.construct(uni_name, data, url)
                else:
                    continue
                break
    def getData(self, url):
        soup = BeautifulSoup(r.get(url).text, 'lxml')
        blocks = soup.find_all('section', 'search-results-info-item')
        data = []
        for block in blocks:
            name = block.a.text
            chars = block.find_all('div', 'big-number-h2')

            chars = [re.sub(r'\D', '', char.text.replace('—', '0').replace('.','1234567890')).replace('1234567890','.') for char in chars]
            data.append(
                {
                    'name':name,
                    'point':chars[0],
                    'places':chars[1],
                    'price':chars[2]
                }
            )
        return data
    def construct(self, name, data, url):
        arr = url.split('/')
        for i in arr:
            if i in self.subjects:
                firsub = i
                arr.remove(i)
                for j in arr:
                    if j in self.subjects:
                        secsub = j
                        break
                else:
                    continue
                break
        if firsub == secsub:
            secsub = ''
        obj = {
            'name':name,
            'programs':data,
            'firsub':firsub,
            'secsub':secsub
        }
        self.data.append(obj)
        
        f = open('data.json', 'w', encoding='UTF-8')
        j = json.dump(self.data, f, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    Main()