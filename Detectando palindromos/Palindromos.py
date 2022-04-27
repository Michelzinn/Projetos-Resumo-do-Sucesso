
def palindrome(word):
    list1 = []
    list2 = []

    for letra in word:
        list1.append(letra)

    for letra in word[::-1]:
        list2.append(letra)

    if list1 == list2:
        print('Esta palavra é um palindromo!')
    else:
        print('Não é um palindromo!')





palindrome('arara')