import sys

def solution(array):
    last_start_index = 0
    index_map = {}
    max_in_set = -999999
    min_in_set = sys.maxsize

    max_length = 0
    max_subarray_start_index = -1
    
    for idx, i in enumerate(array):
        if i in index_map:
            last_start_index = index_map[i] + 1
        else:
            if i < min_in_set:
                min_in_set = i
            
            if i > max_in_set:
                max_in_set = i

            index_map[i] = idx

        if (max_in_set - min_in_set + 1) == len(index_map):
            if len(index_map) > max_length:
                max_length = len(index_map)
                max_subarray_start_index = last_start_index
    
    return array[max_subarray_start_index: max_subarray_start_index + max_length]
if __name__ == '__main__':
    array = [2, 0, 2, 1, 4, 3, 5, 0]
    subarray = solution(array)
    print(subarray)