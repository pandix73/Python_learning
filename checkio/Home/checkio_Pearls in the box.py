def calculate(marbles, step):
    ret = 0
    if marbles == "":
        ret = 0
    elif step == 1:
        ret = marbles.count('w') / len(marbles)
    else:
        ret += marbles.count('w') * calculate(marbles.replace('w', 'b', 1), step-1) / len(marbles)
        ret += marbles.count('b') * calculate(marbles.replace('b', 'w', 1), step-1) / len(marbles)
    return ret
def checkio(marbles, step):
    return float("%.2f" % calculate(marbles, step))
    
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"