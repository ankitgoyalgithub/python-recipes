def findstr(input_string, search_string):
    if len(search_string) > len(input_string):
        return -1
    
    l_ss = len(search_string)
    l_is = len(input_string)

    for i in range(l_is-l_ss+1):
        # print(input_string[i:i+l_ss])
        if input_string[i:i+l_ss] == search_string:
            return i
    
    return -1

if __name__ == '__main__':
    input_string = "ankit"
    search_string = "it"

    print(findstr(input_string, search_string))