size_disket = 1.44 #размер дискеты в мегабайтах
list_book = 100 #количество страниц книги
str_book = 50 #количество строк на странице
symbol_str = 25 #количество символов в строке
size_data = 4 #вес одного символа
size_disket = size_disket * 1024 * 1024 #первод в байты
size_book = symbol_str * str_book * list_book * size_data
print("Количество книг, помещающихся на дискету:", int(size_disket//size_book))
