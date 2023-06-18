for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        print(f'{number} : Divisível por 3 e por 5')
    elif number % 3 == 0:
        print(f'{number} : Divisível por 3')
    elif number % 5 == 0:
        print(f'{number} : Divisível por 5')
    else:
        print(number)   