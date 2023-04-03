import time


def long_subsequence_common(X, Y, k, l):
    if k == 0 or l == 0:
        return 0
    elif X[k - 1] == Y[l - 1]:
        return 1 + long_subsequence_common(X, Y, k - 1, l - 1);
    else:
        return max(long_subsequence_common(X, Y, k, l - 1), long_subsequence_common(X, Y, k - 1, l));


f = open("LCS2.txt", "r")
X = f.readline()
Y = f.readline()

print("First String :", X.strip())
print("Second String :", Y)
start = int(time.time() * 1000)
print(start)# print the start time
print("Length of substring", long_subsequence_common(X, Y, len(X), len(Y)))
end = int(time.time() * 1000)
print(end)# print the end time
total = end - start # print the total time
print('time taken in execution : ' + str(total))
