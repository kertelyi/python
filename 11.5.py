word = input()
for i in range(len(word) // 2 + 1):
    print(word[i: len(word) - i])
