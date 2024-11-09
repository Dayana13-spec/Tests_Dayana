# TODO Найдите количество книг, которое можно разместить на дискете
stran = 100
stroki = 50
simbols = 25
all_simbols = simbols * stroki * stran
perevod = 1.44 * 1024 * 1024
ves = all_simbols * 4
ok = round(perevod/ves)

print("Количество книг, помещающихся на дискету:", ok)
