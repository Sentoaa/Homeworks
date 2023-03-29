def staff():
    while True:
        try:
            a = int(input('Input the "a" number: ' ))
            b = int(input('Input the "b" number: ' ))
            print(a**2/b)
        except ValueError:
            print('It would be great if you input numbers :) try again ')
        except ZeroDivisionError:
            print('b = 0 does not work :) try again ')
        else:
            break

staff()


