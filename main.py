try:
    sign = input('Enter sigh->')
    length = int(input('Enter length->'))

    for x in range(0,length):
         print(sign)

except Exception as ex:
    print(f'Error',{ex})