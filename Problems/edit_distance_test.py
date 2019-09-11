def convert(str1, str2, m, n):
    if m == 0:
        return n
    
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return convert(str1, str2, m-1, n-1)
    else:
        return 1 + min(convert(str1, str2, m, n-1), convert(str1, str2, m-1, n), convert(str1, str2, m-1, n-1))

if __name__ == '__main__':
    str1 = "sunday"
    str2 = "saturday"

    result = convert(str1, str2, len(str1), len(str2))

    print(result)