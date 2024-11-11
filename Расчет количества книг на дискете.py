# TODO Найдите количество книг, которое можно разместить на дискете
i = 0
kol = 0
kniga = 50 * 25 * 4 * 100 #одна книга
disketa = 1.44 * 1048576 #объёма дискеты в байтах
while i < disketa:
    i = i + kniga
    if i < disketa:
        kol = kol + 1
    else:
        break
print("Количество книг, помещающихся на дискету:", kol)
