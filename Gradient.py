import numpy as np
def myfun(a):
    result = 0
    for count in range(0, a.shape[1], 2):
        for i in a[:, count]:
            result += i
    return result


A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(myfun(A))







