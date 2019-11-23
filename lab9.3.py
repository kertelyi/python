n = int(input('кол-во имен:'))
x = 0
sp = []
sp2 = []
for i in range(n):
    ime = input()
    if ime not in sp:
        sp.append(ime)
        sp2.append(ime)
    elif ime in sp2:
        x += 2
        sp2.remove(ime)
    else:
        x += 1
print(x)