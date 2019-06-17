# Author: Manujinda Wathugala
# Cracking the Coding Interview
# Chapter 1 - Arrays and Strings
# 1.4 - Palindrome Permutation

def is_palindrome_permutation_1(str):
    counts = {}

    for chr in str.lower():
        if chr == ' ':
            continue

        if chr in counts:
            counts[chr] += 1
        else:
            counts[chr] = 1

    odd_counts = False

    for count in counts.values():
        if count % 2 == 1:
            if odd_counts:
                return False
            else:
                odd_counts = True

    return True


# O(n log n)
def is_palindrome_permutation_2(str):

    odd_counts = False

    str_sorted = sorted(str.lower())

    idx = 0
    while idx < len(str_sorted):

        if str_sorted[idx] == ' ':
            idx += 1
            continue

        chr = str_sorted[idx]
        count = 1

        idx += 1

        while idx < len(str_sorted) and chr == str_sorted[idx]:
            idx += 1
            count += 1

        if count % 2 == 1:
            if odd_counts:
                return False
            else:
                odd_counts = True

    return True


# Works only for alphabetic characters
# Ignores case and spaces
# O(n)
def is_palindrome_permutation_3(str):
    odd_even = 0

    for chr in str.lower():
        if chr == ' ':
            continue

        if ord(chr) < ord('a') or ord(chr) > ord('z'):
            print('Error: Not a lowercase letter - {}'.format(chr))
            return None

        chr_index = ord(chr) - ord('a')
        mask = 1 << chr_index

        if odd_even & mask == 0:
            odd_even |= mask
        else:
            odd_even &= ~mask

    return (odd_even & (odd_even - 1)) == 0


if __name__ == '__main__':

    str = 'Tact Coa'

    print(is_palindrome_permutation_1(str))
    print(is_palindrome_permutation_2(str))
    print(is_palindrome_permutation_3(str))

    str = 'abcdba'

    print(is_palindrome_permutation_1(str))
    print(is_palindrome_permutation_2(str))
    print(is_palindrome_permutation_3(str))
