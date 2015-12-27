def checkio(text):

    #replace this for solution
    
    class letter:
        def __init__(self, name, num):
            self.name = name
            self.num = num
    
    count = []
    for i in range(0, 26):
        count.append( letter( chr(i+ord('a')), text.count(chr(i+ord('a')))+text.count(chr(i+ord('A')))) )
    
    from operator import attrgetter 
    
    for i in count:
        i.num = 26-i.num
    count.sort(key = attrgetter('num', 'name'))
    
    return count[0].name

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
