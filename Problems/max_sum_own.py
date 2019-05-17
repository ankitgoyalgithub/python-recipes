def main():
    T = int(input())

    for i in range(T):
        N = int(input())
        elements = list(map(int, input().split()))
        temp_sum = [0] * N
        index_map = { i:[] for i in range(N) }
        
        if elements[0] > 0:
            temp_sum[0] = elements[0]
            index_map[0].append(0)
        else:
            temp_sum[0] = 0

        if temp_sum[0] > elements[1]:
            temp_sum[1] = elements[0]
            index_map[1].append(0)
        else:
            temp_sum[1] = elements[1]
            index_map[1].append(1)

        for i in range(2, N):
            if (elements[i] + temp_sum[i-2]) > temp_sum[i-1]:
                temp_sum[i] =  elements[i] + temp_sum[i-2]
                index_map[i].extend(index_map[i-2])
                index_map[i].append(i)
            else:
                temp_sum[i] = temp_sum[i-1]
                index_map[i].extend(index_map[i-1])
        
        max_sum = -9999999999
        max_sum_indexes = []

        for i in range(N):
            if temp_sum[i] > max_sum:
                max_sum_indexes = [i]
                max_sum = temp_sum[i]
            elif temp_sum[i] == max_sum:
                max_sum_indexes.append(i)
        
        max_start_element = -1001
        max_start_index = 0

        for idx in max_sum_indexes:
            if elements[index_map[idx][-1]] > max_start_element:
                max_start_element = elements[index_map[idx][-1]]
                max_start_index = idx

        for idx in reversed(index_map[max_start_index]):
            print(elements[idx], end='')
        print()
main()