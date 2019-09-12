def solution(array):
    previous_zero_index = -1
    count = 0
    max_length_sequence = -1
    max_index = -1

    for idx, i in enumerate(array):
        if i == 1:
            count += 1
        else:
            count = idx - previous_zero_index
            previous_zero_index = idx
        
        if count > max_length_sequence:
            max_length_sequence = count
            max_index = previous_zero_index
    
    return max_index

if __name__ == '__main__':
    array = [0,0,1,0,1,1,1,0,1,1]
    index = solution(array)
    print(index)