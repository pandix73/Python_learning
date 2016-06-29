def checkio(data):
    result = "M"*(data//1000) + 'D'*(data//500%2) + 'C'*(data%500//100) + 'L'*(data//50%2) + 'X'*(data%50//10) + 'V'*(data//5%2) + 'I'*(data%5)
    return result.replace("DCCCC", "CM").replace("CCCC", "CD").replace("LXXXX", "XC").replace("XXXX", "XL").replace("VIIII", "IX").replace("IIII", "IV")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'