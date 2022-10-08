import math

try:
    list_evens = []
    list_odds = []
    list_nines = []
    num1 = int(input('->'))
    num2 = int(input('->'))

    for i in range(num1,num2+1):
        if i%2 == 0:
            list_evens.append(i)
        if i%2 != 0:
            list_odds.append(i)
        if i%9 == 0:
            list_nines.append(i)
    print(f'Even numbers: {list_evens}\n Sum of even: {sum(list_evens)}\n Avg of even {sum(list_evens) / len(list_evens)}\n')
    print(f'Odd numbers: {list_odds}\n Sum of odd: {sum(list_odds)}\n Avg of odd {sum(list_odds) / len(list_odds)}\n')
    print(f'Nine numbers: {list_nines}\n Sum of nine: {sum(list_nines)}\n Avg of nine {sum(list_nines) / len(list_nines)}\n')
except Exception as ex:
    print(f'Error: {ex} '