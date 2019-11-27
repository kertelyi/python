n = input()
x = int(n.split()[0])
fin_sum = int(n.split()[1])
obshet = []
obsh_sum = 0
for i in range(x):
    n_str = input
    price = int(n_str.split()[0])
    col_tow = int(n_str.split()[1][1::])
    temp_sum = int(n_str.split()[2][1::])
    if price * col_tow != temp_sum:
        obshet.append(i)
    obsh_sum += price * col_tow
if obsh_sum == fin_sum:
    print(0)
else:
    print(max(obsh_sum, fin_sum) - min(obsh_sum, fin_sum))
    print(obshet)
