import requests as r
from bs4 import BeautifulSoup
from colorama import Fore as f
import os
import html

os.system('clear')

class Main():
    def __init__(self):
        
        self.url = 'https://www.ucheba.ru/for-abiturients/vuz/ege/'
        self.subjects = {
            'Математика':'mathematics',
            'Химия':'chemistry',
            'Обществознание':'social',
            'История':'history',
            'Английский':'foreignlanguage',
            'Биология':'biology',
            'География':'geography',
            'Физика':'physics',
            'Информатика':'informatics',
            'Литература':'literature'
        }

        self.sub = []
        print(f.YELLOW + 'Первый предмет')
        for i, (k, _) in enumerate(self.subjects.items()):
            print(f.RESET + f'{i}. {k}')
        firsub = int(input())
        os.system('clear')
        print(f.YELLOW + f'Первый предмет: {self.elbi(self.subjects, firsub)}')
        self.sub.append(self.subjects[self.elbi(self.subjects, firsub)])
        print(f.YELLOW + 'Второй предмет (-1 если нет)')
        for i, (k, _) in enumerate(self.subjects.items()):
            print(f.RESET + f'{i}. {k}')
        secsub = int(input())
        os.system('clear')
        self.prSubjects(firsub, secsub)

        self.dbinit(firsub, secsub)
        self.fmenu(firsub, secsub, 0)


    def cmenu(self, firsub, secsub, v, u):
        while True:
            os.system('clear')
            self.prSubjects(firsub, secsub)
            print(f.GREEN + v[0] + f.RESET)
            self.intfc2(v[1])
            a = int(input())
            if a >= 0 and a < len(v[1]):
                os.system('clear')
                self.prSubjects(firsub, secsub)
                print(f.GREEN + f'Название программы: {v[1][a][0]}' + f.RESET)
                print(f'Проходной балл: {v[1][a][1]}')
                print(f'Бюджетных мест: {v[1][a][2]}')
                print(f'Cтоимость обучения: {v[1][a][3]}')
                print(f.YELLOW + '\n(ENTER чтобы выйти)' + f.RESET)
                input()
                continue
            elif a == -1:
                os.system('clear')
                self.fmenu(firsub, secsub, u)
            else:
                os.system('clear')
                self.prSubjects(firsub, secsub)
                continue


    def fmenu(self, firsub, secsub, u):
        arrLen = len(self.arr)
        while True:
            print(f.YELLOW + f'Страница: {u+1}/{arrLen}' + f.RESET)
            self.intfc1(u)
            a = int(input())
            if a < 10 and a >= 0:
                try:
                    os.system('clear')
                    self.prSubjects(firsub, secsub)
                    self.v = self.arr[u][a]
                except:
                    os.system('clear')
                    self.prSubjects(firsub, secsub)
                    continue
                self.cmenu(firsub, secsub, self.v, u)
            elif a == 10 and arrLen != u+1:
                os.system('clear')
                self.prSubjects(firsub, secsub)
                u += 1
            elif a == 11 and u != 0:
                os.system('clear')
                self.prSubjects(firsub, secsub)
                u -= 1
            elif a == 12:
                os.system('clear')
                Main()
            else:
                os.system('clear')
                self.prSubjects(firsub, secsub)
                continue

    def dbinit(self, firsub, secsub):
        mu = 1
        i = 2
        self.arr = []
        self.arr.append(self.parse(self.getUrl(page=1)))
        print(f.GREEN + 'Загрузка 9%' + f.RESET)
        while mu:
            mu = self.getUrl(page=i)
            i+=1
            os.system('clear')
            self.prSubjects(firsub, secsub)
            print(f.GREEN + f'Загрузка {i*9-9}%' + f.RESET)
            a = self.parse(mu)
            if a[0][0] != self.arr[0][0][0]:
                self.arr.append(a)
            else:
                break
        os.system('clear')
        self.prSubjects(firsub, secsub)

    def elbi(self, dict, i):
        return list(dict.keys())[i]
    
    def prSubjects(self, firsub, secsub):
        print(f.YELLOW + f'Первый предмет: {self.elbi(self.subjects, firsub)}')
        if secsub != -1:
            print(f.YELLOW + f'Второй предмет: {self.elbi(self.subjects, secsub)}' + f.RESET)
            self.sub.append(self.subjects[self.elbi(self.subjects, secsub)])
        else:
            pass

    def intfc2(self, v):
        for i,j in enumerate(v):
            print(f'{i}. {j[0]}({j[1]})')
        print(f.YELLOW + '(Введите -1 для выхода)' + f.RESET)

    def intfc1(self, page):
        for i, j in enumerate(self.arr[page]):
            print(f'{i}. {j[0]}')
        print(f.YELLOW + '10. Вперед' + f.RESET)
        print(f.YELLOW + '11. Назад' + f.RESET)
        print(f.YELLOW + '12. Вернуться к выбору предмета' + f.RESET)

    def getUrl(self, page):
        if len(self.sub) == 1:
            prUrl = f'https://www.ucheba.ru/for-abiturients/vuz/ege/{self.sub[0]}'
        else:
            prUrl = f'https://www.ucheba.ru/for-abiturients/vuz/ege/{self.sub[0]}/{self.sub[1]}'
        match page:
            case 1:
                try:
                    return r.get(prUrl).text
                except:
                    return False
            case _:
                try:
                    return r.get(prUrl+str(f'?s={page-1}0')).text
                except:
                    return False
                
    def dopParse(self, l):
        soup = BeautifulSoup(r.get(f'https://www.ucheba.ru{l}').text, features="lxml")
        a = soup.find_all('section', 'search-results-info-item')
        return [[i.find('a').contents[0], 
                 i.find_all('div', 'big-number-h2')[0].contents[0].replace('\n', '').replace('\t', ''), 
                 i.find_all('div', 'big-number-h2')[1].contents[0].replace('\n', '').replace('\t', ''),
                 i.find_all('div', 'big-number-h2')[2].contents[0].replace('\n', '').replace('\t', '').replace('\xa0','')] for i in a]
    
    def parse(self, mu):

        self.fsoup = BeautifulSoup(mu, features="lxml")
        queryArr = self.fsoup.find_all('h2', "search-results-title")
        vuzArr = [i.a.contents[0] for i in queryArr]
        queryArr2 = self.fsoup.find_all('a', 'search-results-more-info')
        progArr = [i.attrs['data-programs-url'] for i in queryArr2]
       # print(progArr)
        arr = []
        
        for i, j in enumerate(vuzArr):
            arr.append([j, self.dopParse(progArr[i])])
        
        return arr
        
        
        

if __name__ == '__main__':
    Main()