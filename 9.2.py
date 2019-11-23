n = int(input('кол во уроков'))  # количество уроков
num1 = int(input('кол во учеников'))  # кол-во учеников
sim = set()
dob = set()
for a in range(num1):
    zap = input('имена учеников')
    sim.add(zap)
for i in range(n-1):
    num = int(input('кол во учеников'))
    for с in range(num):
        b = input('имена учеников2')
        dob.add(b)
    sim = sim.intersection(dob)
    dob.clear()
for elem in sim:
    print(elem)
