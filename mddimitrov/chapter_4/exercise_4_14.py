def spanish_days():
    """
    Asks the user to input a weekday in English.
    If the weekday is valid, print the Spanish equivalent.
    Otherwise do not print anything.
    """
    weekday = input("Please enter a weekday such as 'Monday': ").lower()
    if weekday == 'monday':
        print('lunes')
    elif weekday == 'tuesday':
        print('martes')
    elif weekday == 'wednesday':
        print('miércoles')
    elif weekday == 'thursday':
        print('jueves')
    elif weekday == 'friday':
        print('viernes')
    elif weekday == 'saturday':
        print('sábado')
    elif weekday == 'sunday':
        print('domingo')


if __name__ == '__main__':
    spanish_days()
