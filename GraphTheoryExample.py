

import MyMethods as mm

def main():

    # Example:
    M = [[0, 1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0]]

    result = mm.maxRegion(M)
    print(result)
    
    M = mm.createRandomMatrix(25, 25)
    mm.maxRegion(M)

main()