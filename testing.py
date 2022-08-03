Phone_book = {
              'user1': 11111,
              'user2': 22222,
              'user3': 33333,
              'user4': 44444,
              'user5': 55555
             }
Phone_book = dict()

while True:
    try:
        if (number := int(input('Enter a number (or 0 to end): '))) == 0:
            break
        if number in Phone_book.values():
            print(f'Number {number} already exists')
        else:
            if (name := input('Please enter a username: ')) == '' or name in Phone_book:
                print(f'Name {name} already exists or is invalid')
            else:
                Phone_book[name] = number
    except ValueError:
        print('Invalid input. Please try again')

print(Phone_book)