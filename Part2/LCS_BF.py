import time


def longest_common_sequence1(X, Y, m, n):
    L = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    longest_common_sequence1 = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            longest_common_sequence1 += X[i - 1]
            i -= 1
            j -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1

        else:
            j -= 1

    longest_common_sequence1 = longest_common_sequence1[::-1]

    print("1st String:" + X.strip() + "\nString two: " + Y + "\nLength of LCS:")
    print(len(longest_common_sequence1))


f = open("LCS2.txt", "r")
X = f.readline()
Y = f.readline()
m = len(X)
n = len(Y)
start = float(time.time() * 1000)
print(start)# print the start time
longest_common_sequence1(X, Y, m, n)
end = float(time.time() * 1000)
print(end)# print the end time
total = end - start # print the total time
print('time taken in execution : ' + str(total))
