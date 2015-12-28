def count_neighbours(grid, row, col):
    
    dirx = [1, 1, 1, -1, -1, -1, 0, 0]
    diry = [1, -1, 0, 1, -1, 0, 1, -1]
    
    ans = 0
    for i in range(0, 8):
        if row+dirx[i]>=0 and row+dirx[i]<len(grid) and col+diry[i]>=0 and col+diry[i]<len(grid[0]) and grid[row+dirx[i]][col+diry[i]] == 1:
            ans = ans + 1
    return ans
​
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
