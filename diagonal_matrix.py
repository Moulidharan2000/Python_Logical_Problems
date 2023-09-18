# An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right.
# The rest are 0s.
# The identity matrix has applications ranging from machine learning to the general theory of relativity.
# Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge,
# if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.
# It does not matter if the mirror image is left-right or top-bottom.
#
# Examples
# id_mtrx(2) ➞ [
#   [1, 0],
#   [0, 1]
# ]
#
# id_mtrx(-2) ➞ [
#   [0, 1],
#   [1, 0]
# ]
#
# id_mtrx(0) ➞ []
# Notes
# Incompatible types passed as n should return the string "Error".


def identity_matrix(size):
    if size == 0:
        return []
    identity = [[0] * abs(size) for _ in range(abs(size))]
    for i in range(abs(size)):
        identity[i][i] = 1
    if size > 0:
        return identity
    else:
        return [row[::-1] for row in identity]


if __name__ == '__main__':
    print(identity_matrix(2))
    print(identity_matrix(0))
    print(identity_matrix(-4))
