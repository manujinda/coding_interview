# Author: Manujinda Wathugala
# Cracking the Coding Interview
# Chapter 1 - Arrays and Strings
# 1.2 - Check Permutation


# O(n)
def check_permutation_1(str1, str2):

    if len(str1) != len(str2):
        return False

    chars = {}

    for chr in str1:
        if chr in chars:
            chars[chr] += 1
        else:
            chars[chr] = 1

    for chr in str2:
        if chr in chars:
            chars[chr] -= 1
            if chars[chr] < 0:
                return False
        else:
            return False

    return True


def check_permutation_2(str1, str2, alph_size):
    if len(str1) != len(str2):
        return False

    counts = [0] * alph_size

    for chr in str1:
        counts[ord(chr)] += 1

    for chr in str2:
        counts[ord(chr)] -= 1

        if counts[ord(chr)] < 0:
            return False

    return True


# O(n log n)
def check_permutation_3(str1, str2):

    if len(str1) != len(str2):
        return False

    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)

    #for idx, chr1 in enumerate(str1_sorted):
    #    if chr1 != str2_sorted[idx]:
    #        return False

    #return True

    return str1_sorted == str2_sorted



if __name__ == '__main__':
    str1 = 'abcde'
    str2 = 'eabdc'
    str3 = 'abcdd'

    print(check_permutation_1(str1, str2))
    print(check_permutation_2(str1, str2, 256))
    print(check_permutation_3(str1, str2))

    print(check_permutation_1(str1, str3))
    print(check_permutation_2(str1, str3, 256))
    print(check_permutation_3(str1, str3))
