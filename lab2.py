from csv import reader 
def open_data(): 
    try: 
        with open('books-en.csv', 'r', newline='') as in_file: #newline управляет переводом на след строку
            data = list(reader(in_file, delimiter=';'))[1:] 
            return data 
    except FileNotFoundError: #если нет файла 
        print("File isn't found") 
        return [] 
    
def longname(): 
    data = open_data() 
    if data:  #если файл существует
        result = sum([1 for i in data if len(i[1]) > 30]) 
        print(result) 
        return result 
    print("File isn't found") 
    return [] 

def fbook():
    author = input("Write the author's name: ").strip().upper() #убирает пробелы и переводит в большие буквы
                                                                
    data = open_data()
    if data:
        authors_books = []
        for row in data:
            try:
                if (int(row[3]) in [1997, 1998, 1999, 2000]) and (author in row[2].upper()):
                    authors_books.append(row)
            except ValueError:
                if (int(row[-3]) in [1997, 1998, 1999, 2000]) and (author in row[-4].upper()): #на случай, если ячейки автора и года перепутаны в файле
                    authors_books.append(row)
        if authors_books:
            print(f'N name year')
            for i in range(len(authors_books)):
                print(f'{str(i + 1)} {authors_books[i][1]}   {authors_books[i][3]}')  
        else:
            print("No book")
        return authors_books
    print("File isn't found")
    return []


def write_books():
    data = open_data()[:20]
    if data:
        with open('write_books.txt', 'w', newline='') as out_file:
            out_file.write(f'N  Author  Title    Year\n')
            for i in range(20):
                out_file.write(f'{str(i + 1)} {data[i][2]} {data[i][1]} - {data[i][3]}\n')
        return data
    print("File isn't found")
    return []
        
 
# longname() 
# fbook() 
# write_books() 
         
# дополниетльное задание 
def publishers(): 
    data = open_data() 
    if data: 
        publishers_m = list(set([i[4] for i in data])) #достаем ячейку издатедя, set убирает дубликаты, собираем обратно в лист, чтобы млжнл было обращаться
        for i in range(len(publishers_m)): 
            print(i + 1, publishers_m[i]) 
            print("File isn't found") 
            return [] 
        
def mostpopular(): 
    data = open_data() 
    if data: 
        data.sort(key=lambda x: float(x[-2]), reverse=True) #сортирует массив по -2 элементу (кол-во скачиваний) 
        for i in range(20): 
            print(f'{i + 1}.', data[i][1]) 
        return data 
    print("File isn't found") 
    return [] 
# publishers() 
# mostpopular()