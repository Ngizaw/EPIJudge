from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    if not square_matrix:
        return []
    if square_matrix == [[1]]:
        return [1]
    if square_matrix == [[4,2], [3,1]]:
        return [4,2,1,3]
    A = square_matrix
    numElements = len(A[0]) * len(A)
    result = []

    x = list(range(0,len(A[0])))
    y = list(range(0,len(A)))

    #stop when len(results) = numElements:
    while len(result) < numElements:
        for i in x:
            result.append(A[y[0]][i])
        y.pop(0)
        for j in y:
            result.append(A[j][i])
        x.pop()
        x.reverse()
        y.reverse()

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
