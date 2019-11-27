        word = input()
i = int(input())
letter = input()
if i > len(word) or len(letter) > 1 or i < 0:
    print('Ошибка')
elif word.lower()[i - 1] == letter.lower():
    print('да')
else:
    print('нет')
