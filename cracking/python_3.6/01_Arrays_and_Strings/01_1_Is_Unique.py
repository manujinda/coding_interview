# Author: Manujinda Wathugala

# n - Length of the string
# c - Size of the alphabet

# Using a hash set - O(min(n, c))
def is_unique_1(str):
    seen = set()

    for chr in str:
        if chr in seen:
            return False

        seen.add(chr)

    return True


# Using bit operations - O(min(n, c))
# Only works for lowercase alphabetic characters
# In Python integers can be of unlimited precision
# Therefore, we can use this method to any size of
# alphabet
def is_unique_2(str):
    seen = 0

    for chr in str:
        if ord(chr) < 97 or ord(chr) > 122:
            print('Error: Non-lowercase alphabetic character found - {}'.format(chr))
            return None

        # Index of this character in the alphabet
        # with index of 'a' being 0 and 'z' being 25
        char_index = ord(chr)-ord('a')

        # Set the char_index bit of an integer to 1
        flag = 1 << char_index

        # Check whether we have see this character before
        if seen & flag != 0:
            return False

        # Set the bit for this character in seen
        seen |= flag

    return True


# Using a bit array of alphabet size
# O(min(n, c))
def is_unique_3(str, alph_size):
    if len(str) > alph_size:
        return False

    seen = [False] * alph_size

    for chr in str:
        if seen[ord(chr)]:
            return False

        seen[ord(chr)] = True

    return True


# Without using an additional buffer
# Using sorting - O(nlog(n))
def is_unique_4(str):
    str_sorted = sorted(str)

    for idx in range(len(str_sorted)-1):
        if str_sorted[idx] == str_sorted[idx+1]:
            return False

    return True


# Using two loops - O(n^2)
def is_unique_5(str):
    str_len = len(str)
    for idx1 in range(str_len - 1):
        for idx2 in range(idx1 + 1, str_len):
            if str[idx1] == str[idx2]:
                return False

    return True


# A recursive approach - O(n^2)
def is_unique_6(str):
    if len(str) == 1:
        return True

    for chr in str[1:]:
        if str[0] == chr:
            return False

    return is_unique_6(str[1:])


if __name__ == '__main__':

    str = 'axbdefg'
    print(is_unique_1(str))
    print(is_unique_2(str))
    print(is_unique_3(str, 256))
    print(is_unique_4(str))
    print(is_unique_5(str))
    print(is_unique_6(str))

    str = 'axbdafg'
    print(is_unique_1(str))
    print(is_unique_2(str))
    print(is_unique_3(str, 256))
    print(is_unique_4(str))
    print(is_unique_5(str))
    print(is_unique_6(str))
