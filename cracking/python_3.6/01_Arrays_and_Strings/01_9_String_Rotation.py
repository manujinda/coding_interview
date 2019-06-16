# Author: Manujinda Wathugala
# Cracking the Coding Interview
# Chapter 1 - Arrays and Strings
# 1.9 - String Rotation


def isSubstring(str, str_sub):
    sub_len = len(str_sub)

    if len(str) < sub_len:
        return False

    for idx in range(len(str) - sub_len):
        if str[idx : idx + sub_len] == str_sub:
            return True

    return False


def string_rotation(str1, str2):
    return isSubstring(str1+str1, str2)


if __name__ == '__main__':
    str = 'abcdefghij'
    str_sub = 'defg'
    str_no_sub = 'cdfg'

    print(isSubstring(str, str_sub))
    print(isSubstring(str, str_no_sub))

    str_rot = 'cdefghijab'
    str_not_rot = 'cdefghijba'

    print(string_rotation(str, str_rot))
    print(string_rotation(str, str_not_rot))
