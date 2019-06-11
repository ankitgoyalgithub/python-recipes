def bubble_sort(num):
    len_list = len(num)

    for i in range(len_list):
        for j in range(len_list - i - 1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

if __name__ == '__main__':
    num = [7,1,3,2,0,9,4,6,5,8]
    bubble_sort(num)
    print(num)