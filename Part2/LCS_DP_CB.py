from numpy import *
import time

def LCS_LENGTH(X, Y):
    m: int = len(X) + 1  # taking the length of the string1 m = 4
    n: int = len(Y) + 1  # taking the length of the string2 n = 6
    b_matrix = [[' ' for i in range(n)] for j in range(m)]  # declaring b_matrix matrix m x n, with default blank value
    c_matrix = [[0 for i in range(n)] for j in range(m)]  # declaring c_matrix matrix m x n, with default 0 value
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                c_matrix[i][j] = c_matrix[i - 1][j - 1] + 1
                b_matrix[i][j] = '\\'
            elif c_matrix[i - 1][j] >= c_matrix[i][j - 1]:
                c_matrix[i][j] = c_matrix[i - 1][j]
                b_matrix[i][j] = '^'
            else:
                c_matrix[i][j] = c_matrix[i][j - 1]
                b_matrix[i][j] = '<'
            # print('b_matrix after update = ', b_matrix)
            # print('c_matrix after update = ', c_matrix)
    for j in range(0, n):
        if j == 0:
            print('  Y', end='')
        else:
            print('', Y[j - 1], end='')
    print('')
    for i in range(0, m):
        if i == 0:
            print('X', end='')
        else:
            print(X[i - 1], end='')
        for j in range(0, n):
            print(b_matrix[i][j], end='')
            print(c_matrix[i][j], end='')
        print('')
    return b_matrix, c_matrix


def printLCS(b, X, xlen, ylen, a):

    if xlen == 0 or ylen == 0:
        print('The length of the longest common subsequence is :', len(a))
        print('The longest common subsequence of \"', X, '\" and \"', Y, '\" is \"', a[::-1],'\"')
        # reverse the string to get the output
        # ref - https://www.w3schools.com/python/python_howto_reverse_string.asp
        return 0
    if b[xlen][ylen] == '\\':
        a += X[xlen - 1]# stores the values that form a LCS
        #print('A =', a)
        printLCS(b, X, xlen - 1, ylen - 1, a)
        # print(X[xlen - 1], end='')# LCS with respective to the algorithm
    elif b[xlen][ylen] == '^':
        printLCS(b, X, xlen - 1, ylen, a)
    else:
        printLCS(b, X, xlen, ylen - 1, a)


if __name__ == '__main__':
    file = open('LCS2.txt', 'r')  # 'r' is optional
    X = file.readline().rstrip('\n')
    # reference - https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
    Y = file.readline().rstrip('\n')
    print('X = ', X)
    print('Y = ', Y)
    startmilliseconds20 = int(time.time() * 1000000000)
    print("startmilliseconds", startmilliseconds20)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    b, c = LCS_LENGTH(X, Y)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # print('c in main', c)
    # print('b in main', b)
    endmilliseconds20 = int(time.time() * 1000000000)
    print("endmilliseconds", endmilliseconds20)
    a = ''
    printLCS(b, X, len(X), len(Y), a)
    file.close()
