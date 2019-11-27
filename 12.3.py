n = int(input())
buy_list = []
j = []
for i in range(n):
    j.clear()
    naimen = input()
    count = input()
    j.append(naimen)
    j.append(count)
    buy_list.append(j)
    print(buy_list)
print(buy_list)
# for i in range(n, 0, -1):
#     for b in range(2):
#         print(buy_list[i][b])
