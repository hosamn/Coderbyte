# Coderbyte
# Searching Challenge
# Have the function Searching(strArr) take the array of strings stored in strArr, which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's, exist in the matrix. A contiguous region is one where there is a connected group of 0's going in one or more of four directions: up, down, left, or right. For example: if strArr is ["10111", "10101", "11101", "11111"], then this looks like the following matrix:

# 1 0 1 1 1
# 1 0 1 0 1
# 1 1 1 0 1
# 1 1 1 1 1

# For the input above, your program should return 2 because there are two separate contiguous regions of 0's, which create "holes" in the matrix. You can assume the input will not be empty.
# Examples
# Input: ["01111", "01101", "00011", "11110"]
# Output: 3
# Input: ["1011", "0010"]
# Output: 2


def Searching(strArr):
    import numpy as np

    ll = [j for i in strArr for j in i]
    strArr = np.array(ll).reshape(len(strArr), len(strArr[0])).astype(np.int8)

    # for i in strArr.T:
    #   print(i)

    # will deal with this in rows then columns:

    mx_gap = 0

    for i in strArr:
        zros = np.concatenate(([0], np.equal(i, 0).view(np.int8), [0]))
        dlts = np.abs(np.diff(zros))
        rngs = np.where(dlts == 1)[0].reshape(-1, 2)
        gaps = [i[1] - i[0] for i in rngs]
        if gaps:
            if max(gaps) > mx_gap:
                mx_gap = max(gaps)

    for i in strArr.T:
        zros = np.concatenate(([0], np.equal(i, 0).view(np.int8), [0]))
        dlts = np.abs(np.diff(zros))
        rngs = np.where(dlts == 1)[0].reshape(-1, 2)
        gaps = [i[1] - i[0] for i in rngs]
        if gaps:
            if max(gaps) > mx_gap:
                mx_gap = max(gaps)
    return mx_gap


# Testing : 
print(Searching(["01111", "01101", "00011", "11110"]))
print(Searching(["01111", "01011", "10011", "11110"]))
print(Searching(["1011", "0010"]))
