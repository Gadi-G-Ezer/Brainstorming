from _datetime import datetime, timedelta


def day_calculator(days_number):
    """
    this function receives a number of days (as integer), and returns the date and time in
    number of days from now, in iso format, like so:
    :param days_number:
    :return: iso formart of the date and time in the given number of days
    """
    try:
        return (datetime.now() + timedelta(days=days_number)).isoformat()
    except:
        print('invalid input. try again')


def main():
    print(day_calculator(5))


if __name__ == '__main__':
    main()