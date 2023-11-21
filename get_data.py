import sqlite3 as sq
import aiogram

def get_data(subj, sem):        #
    with sq.connect('books.db') as con:             #создание контекст-менеджера
        cur = con.cursor()                          #перменная, с помощью методов которой выполняется SQL запрос
        cur.execute(f'select Ссылка from "{sem}" where Предмет = "{subj.lower()}"')
        result = cur.fetchall()#получение списка записей из бд с помощью метода fetchall()
        lst = []                                    #преобразование списка списков значений в список значений
        for i in result:
            lst.append(i[0])
        return lst

def get_prefix(subj, sem):          #
    with sq.connect('books.db') as con:
        cur = con.cursor()
        cur.execute(f'select Код_учебника from "{sem}" where Предмет = "{subj}"')
        result = cur.fetchall()
        lst = []
        for i in result:
            lst.append(i[0])
        return lst
def get_books_name(subj, sem):      #
    with sq.connect('books.db') as con:
        cur = con.cursor()
        cur.execute(f'select Название_учебника from "{sem}" where Предмет = "{subj}"')
        result = cur.fetchall()
        lst = []
        for i in result:
            lst.append(i[0])
        return lst

def get_subjects_for_num(sem):          #
    with sq.connect('books.db') as con:
        cur = con.cursor()
        cur.execute(f'select distinct Предмет from "{sem}"')
        result = cur.fetchall()
        lst = []
        for i in result:
            if i[0] != None:
                lst.append(i[0])
        return lst
def get_all_links_for_subject(subject):
    with sq.connect('books.db') as con:
        cur = con.cursor()
        lst_name_books = []
        lst_code_of_book = []
        lst_link_book = []
        for i in range(1, 9):
            cur.execute(f"select Название_учебника, Код_учебника, Ссылка FROM '{i}' where Предмет = '{subject}'")
            result = cur.fetchall()             #результат поиска в виде [(a, b, c), (a, b, c)], где a, b, c - название, код, ссылка на книгу
            if len(result) !=0:
                for item in result:
                    lst_name_books.append(item[0])
                    lst_code_of_book.append(item[1])
                    lst_link_book.append(item[2])
        return lst_name_books,lst_code_of_book, lst_link_book
