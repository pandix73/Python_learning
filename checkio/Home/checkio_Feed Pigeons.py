def checkio(number):
    minute = 1
    pigeons = 1
    while number > pigeons:
        number -= pigeons
        minute += 1
        pigeons += minute
    return max(number, pigeons-minute)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"