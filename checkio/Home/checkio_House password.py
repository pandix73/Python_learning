def checkio(data):

    upper = 0
    lower = 0
    digit = 0
    for i in data:
        if i <= 'z' and i >= 'a':
            lower = 1
        elif i <= 'Z' and i >= 'A':
            upper = 1
        elif i <= '9' and i >= '0' :
            digit = 1
    len10 = (len(data) > 9)
    #replace this for solution
    return upper and lower and digit and len10

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
