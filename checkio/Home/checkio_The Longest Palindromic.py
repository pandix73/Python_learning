def longest_palindromic(text):
    maxi = 0
    maxr = 0
    for i in range(0, len(text)):
        r = 0
        while i-r >= 0 and i+r < len(text) and text[i+r] == text[i-r]:
            r += 1
        if r-1 > maxr:
            maxi = i
            maxr = r-1
    return text[maxi-maxr:maxi+maxr+1]
​
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"