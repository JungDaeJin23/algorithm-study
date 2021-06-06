# Longest_Palindrome_substring test
# Brute force
def is_palindrome(str1):
    n = len(str1)
    half_n = n // 2

    i = 0
    while i <= half_n:
        if str1[i] != str1[n - 1 - i]:
            return False
        i += 1
    return True


# Recursion


# Brute force
def find_palindrome(matrix, palindrome_length):
    n = len(matrix)

    # Accessing two dimensional arrays in row major order
    i = 0
    while i < n:
        j = 0
        while j < n - palindrome_length + 1:
            if is_palindrome(matrix[i][j: j + palindrome_length]):
                return ''.join(matrix[i][j: j + palindrome_length])
            j += 1

        i += 1

    # Another way: transpose the arrays and repeat above code twice(재현)
    # Accessing two dimensional arrays in column major order
    j = 0
    while j < n:
        i = 0
        while i < n - palindrome_length + 1:
            word = ''

            k = 0
            while k < palindrome_length:
                word += matrix[i + k][j]
                k += 1
            if is_palindrome(word):
                return word

            i += 1

        j += 1
    return False


# input and output
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    two_dimensional_list = [list(input()) for _ in range(N)]
    print("#{0}".format(tc), find_palindrome(two_dimensional_list, M))