def prime_nums(num):
    for i in range(2, num):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i, end=' ')


def is_prime(num):
    print()
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                print(num, " is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


if __name__ == '__main__':
    num = int(input("Enter the Number : "))
    prime_nums(num)
    is_prime(num)
