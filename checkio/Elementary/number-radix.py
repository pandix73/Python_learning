def checkio(str_number, radix):
    ans = 0
    for i in str_number:
        num = (10+ord(i)-ord('A')) if ord(i)>=ord('A') else ord(i)-ord('0')
        if num >= radix:
            return -1
        else:
            ans = ans*radix + num
    return ans
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
