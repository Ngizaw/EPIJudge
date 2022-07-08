from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    # given an integer, return an integer with the digits reverese
    # ex: 247 -> 742
    result = 0
    rem_x = abs(x)

    while rem_x:
        result = rem_x % 10 + (result * 10)
        rem_x //= 10

    return result if x > 0 else -result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
