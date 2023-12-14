def main():
    #вводим числа
    num1 = input("Введите первое число: ")
    num1 = int(num1)
    num2 = input("Введите второе число: ")
    num2 = int(num2)

    #вывод
    print("НОД (", end='')
    print(num1, num2, sep=';', end='')
    print(") = ", euclid(num1, num2))

def euclid(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

if __name__ == '__main__':
    main()