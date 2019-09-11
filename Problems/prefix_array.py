def prefix_array(string=None):
    length = len(string)
    prefix = [0] * length

    j = 0
    i = 1

    while i < length:
        if string[i] == string[j]:
            prefix[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                prefix[i] = 0
                i += 1
            else:
                j = prefix[j-1]
    return prefix

def match_pattern(string, pattern, prefix):
    length = len(string)
    pattern_length = len(pattern)

    i = 0
    j = 0
    start_index = 0

    while (i < pattern_length) and (j<length):

        if pattern[i] == string[j]:
            i += 1
            j += 1
        else:
            if i == 0:
                j += 1
                start_index = j
            else:
                start_index = j - prefix[i-1]
                i = prefix[i-1]

    if i == pattern_length:
        return True, start_index
    
    return False, -1
if __name__ == '__main__':
    string  = "abxabcabcaby"
    pattern = "xab"
    prefix = prefix_array(string=string)
    print(prefix)

    print(match_pattern(string, pattern, prefix))