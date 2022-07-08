from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    # parity bit is 1 if the number of bits in num are odd
    par = 0
    while x:
        x &= x-1
        par ^= 1

    return par


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
