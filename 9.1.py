knigi_doma = int(input('сколько книг дома?'))
spisok_naleto = int(input('книги на лето'))
knig = set()
spis = []
for i in range(knigi_doma):
    x = input()
    knig.add(x)
for i in range(spisok_naleto):
    a = input()
    spis.append(a)
for i in range(spisok_naleto):
    if spis[i] in knig:
        print('YES')
    else:
        print('NO')
