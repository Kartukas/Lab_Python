# TODO Найдите количество книг, которое можно разместить на дискете
V = (1.44 * 1024 * 1024)
Count = int(V // (100 * 50 * 25 * 4))
print("Количество книг, помещающихся на дискету:", Count)
