"""Напишите ф-ю search_substr(subst, st), которая принимает 2 строки
и определяет, имеется ли подстрока subst в строке st.
В случае нахождения подстроки, возвращается фраза "Есть контакт!", а иначк "Мимо!"
Должно быть найдено совпадение независимо от регистра обеих строк."""

# def search_substr(subst, st):
#     if subst.lower() in st.lower():
#         return "Есть контакт!"
#     return "Мимо!"
#
# # print(search_substr('a', 'Alba'))
# # print(search_substr('A', 'Alba'))
# print(search_substr('o', 'alba'))

# или
# def search_substr(subst, st):
#     return "Есть контакт!"  if subst.lower() in st.lower() else  "Мимо!"
#
# print(search_substr("Star", "A"))


"""Требуется определить индексы первого и последнего вхождения буквы в строке.
для этого нужно написать ф-ю first_last(letter, st), включающую 2 параметра:
letter - искомый символ, st - целевая строка.
В случае отстутствия буквы в строке, нужно вернуть кортеж (None, None), если же 
она есть, то кортеж будет состоять из первого и последнего тндекса этого символа"""

def first_last(letter, st):

    index = st.find(letter)
    if index < 0:
        return (None, None)
    last_index = st.find(letter)
    return index, last_index

print(first_last('a', 'banana'))
print(first_last('c', 'banana'))


"""очистить строку от лишних символов -  гр@oo@лк@оц@ва"""
"""голова"""

def str_clean(st):
    l = []
    for i in st:
        if i != '@':
            l.append(i)
        else:
            l.pop()
    return "".join(l)
print(str_clean("гр@oo@лк@оц@ва"))


