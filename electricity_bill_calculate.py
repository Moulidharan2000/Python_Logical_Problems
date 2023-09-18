def bill_calculate(total_unit):
    bill = 0
    if total_unit <= 100:
        pass
    elif 100 < total_unit <= 200:
        bill = (total_unit - 100) * 5
    elif 200 < total_unit <= 350:
        bill = 100 * 5 + (total_unit - 200) * 7
    elif total_unit > 350:
        bill = 100 * 5 + 150 * 7 + (total_unit - 350) * 10
    return bill


if __name__ == '__main__':
    total_unit = int(input("Enter the units : "))
    print("Bill amount : ", bill_calculate(total_unit))
