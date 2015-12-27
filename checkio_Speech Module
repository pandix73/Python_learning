FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    
    #replace this for solution
    
    num = []
    if number > 99:
        num.append(int(number/100))
        num.append(int(number%100/10))
        num.append(int(number%10))
    elif number > 9:
        num.append(int(number/10))
        num.append(int(number%10))
    else:
        num.append(number)
    
    out = []
    for i in range(0, len(num)):
        if len(num) - i == 3:
            out.append(FIRST_TEN[num[i]-1]+" hundred")
        elif len(num) - i == 2:
            if num[i] == 0:
                continue
            elif num[i] == 1:
                out.append(SECOND_TEN[num[i+1]])
                break
            else:
                out.append(OTHER_TENS[num[i]-2])
        else:
            if num[i] == 0:
                continue
            else:
                out.append(FIRST_TEN[num[i]-1])
    
    ans = ""
    for i in range(0, len(out)):
        if i == 0:
            ans+=out[0]
        else:
            ans+=' '+out[i]
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
