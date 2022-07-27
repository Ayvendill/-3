def season(num):

    if num == 12 or 1 <= num <= 2:

        print("Зима")

    elif 3 <= num <= 5:

        print("Весна")

    elif 6 <= num <= 8:

        print("Літо")

    elif 9 <= num <= 11:

        print("Осінь")

    else:
        print("Неправильно введений місяць")
        
d = int(input("Ведіть номер місяця (1-12): "))
season(d)







