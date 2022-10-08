try:
    list = []
    while True:
        num = int(input('enter number->'))
        if num != 7:
            list.append(num)
        else:
            print(f'Summary: {sum(list)}\n Maximum number: {max(list)}\n Minimum number: {min(list)}\n Good bye.')
except Exception as ex:
    print(f'Error:', {ex})