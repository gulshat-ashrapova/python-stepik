s = [int(i) for i in input().split()]
spisok = []
if len(s) == 1:
    print('нет повторяющихся элементов')
for elem in s:
    if s.count(elem) > 1:
        if elem not in spisok:
            spisok.append(elem)
for elem in spisok:
    print (elem, end=' ')