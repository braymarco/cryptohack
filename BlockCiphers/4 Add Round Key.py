state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    arr = ""
    for i in matrix:
        for j in i:
            arr += chr(j)
    return arr

def add_round_key(s, k):
    a=[]
    for i in range(len(s)):
        a.append([])
        for j in range(len(s[i])):
            a[i].append(s[i][j] ^ k[i][j])
    return a


print(matrix2bytes(add_round_key(state, round_key)))
