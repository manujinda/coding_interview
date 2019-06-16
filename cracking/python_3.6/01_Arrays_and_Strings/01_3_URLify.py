# Author: Manujinda Wathugala
# Cracking the Coding Interview
# Chapter 1 - Arrays and Strings
# 1.3 - URLify

# O(n)
def URLify(str, str_len):
    # Count the number of spaces
    spaces = 0
    for idx in range(str_len):
        if str[idx] == ' ':
            spaces += 1

    last_idx = str_len + 2 * spaces - 1

    str_lst = list(str)

    for idx in range(str_len-1, -1, -1):
        if str[idx] != ' ':
            str_lst[last_idx] = str[idx]
            last_idx -= 1
        else:
            str_lst[last_idx-2 : last_idx+1] = '%20'
            last_idx -= 3

    last_idx = str_len + 2 * spaces
    return ''.join(str_lst[:last_idx])


if __name__ == '__main__':
    str = 'Mr John Smith            '

    print(URLify(str, 13))
