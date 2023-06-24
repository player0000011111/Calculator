
while True:
    first_number = int(input("Son kiriting: "))
    second_number = int(input("Son kiriting: "))
    sign = input("Amal kiriting")
    try:
        if sign == '+':
            print(first_number + second_number)
        elif sign == '-':
            print(first_number - second_number)
        elif sign == '*':
            print(first_number * second_number)
        elif sign == '/':
            print(float(first_number / second_number))
    except ZeroDivisionError:
        print("Nolga bo'lish mumkin emas")
    except ValueError:
        print("Harf kiritdingiz")
    finally:
        print("Dasturni ishlatganingiz uchun raxmat! ")