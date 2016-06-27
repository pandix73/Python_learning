def safe_pawns(pawns):
    count = 0
    for pawn in pawns:
        check1 = chr(ord(pawn[0])-1) + chr(ord(pawn[1])-1)
        check2 = chr(ord(pawn[0])+1) + chr(ord(pawn[1])-1)
        if check1 in pawns or check2 in pawns:
            count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
