# Author: Manujinda Wathugala
# Cracking the Coding Interview
# Chapter 1 - Arrays and Strings
# 1.8 - Zero Matrix


def zero_matrix_1(mat):
    zero_rows = set()
    zero_cols = set()

    num_rows = len(mat)
    num_cols = len(mat[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if mat[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)

    for row in zero_rows:
        mat[row] = [0] * num_cols

    for col in zero_cols:
        for row in range(num_rows):
            mat[row][col] = 0

    return mat


# Use first row and first column to
# Keep track of rows and columns to
# zero out
def zero_matrix_2(mat):
    num_rows = len(mat)
    num_cols = len(mat[0])

    zero_1st_row = False
    zero_1st_col = False

    for col in range(num_cols):
        zero_1st_row = zero_1st_row or (mat[0][col] == 0)
        if zero_1st_row:
            break

    for row in range(num_rows):
        zero_1st_col = zero_1st_col or (mat[row][0] == 0)
        if zero_1st_col:
            break

    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if mat[row][col] == 0:
                mat[0][col] = 0
                mat[row][0] = 0

    for row in range(1, num_rows):
        if mat[row][0] == 0:
            mat[row] = [0] * num_cols

    for col in range(1, num_cols):
        if mat[0][col] == 0:
            for row in range(num_rows):
                mat[row][col] = 0

    if zero_1st_row:
        mat[0] = [0] * num_cols

    if zero_1st_col:
        for row in range(num_rows):
            mat[row][0] = 0

    return mat


if __name__ == '__main__':
    mat =  [[1, 2, 0, 3, 4, 6],
            [5, 2, 6, 7, 7, 3],
            [0, 8, 0, 6, 7, 0],
            [5, 7, 2, 8, 4, 5]]

    print(zero_matrix_1(mat))

    mat =  [[1, 2, 0, 3, 4, 6],
            [5, 2, 6, 7, 7, 3],
            [0, 8, 0, 6, 7, 0],
            [5, 7, 2, 8, 4, 5]]

    print(zero_matrix_2(mat))
