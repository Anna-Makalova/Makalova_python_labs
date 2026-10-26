from xml.etree import ElementTree

char_nominal = {} 
tree = ElementTree.parse('currency.xml') #парсит файл
root = tree.getroot() #возвращает корневое дерево документ

for el in root:                         #перебираем элементы в root
    char_code = el.find('CharCode').text   #достаем код валюты (char_code)
    nominal = el.find('Nominal').text      #достаем номинал
    char_nominal[char_code] = nominal  #записываем в словарь пару: код валюты и номинал

for code, nom in char_nominal.items(): #печатаем результат
    print(code, nom)