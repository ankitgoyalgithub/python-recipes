import random 

def partition(a, start, end):
    pivot = a[end]
    partition_index = start

    for i in range(start,end):
        if a[i] <= pivot:
            a[i], a[partition_index] = a[partition_index], a[i]
            partition_index += 1
    a[partition_index], a[end] = a[end], a[partition_index]

    return partition_index

def rand_partition(a, start, end):
    rand = random.randrange(start, end+1)
    a[rand], a[start] = a[start], a[rand]
    return partition(a, start, end)

def quick_sort(a, start, end):
    if start <= end:
        pivot = rand_partition(a, start, end)
        quick_sort(a, start, pivot-1)
        quick_sort(a, pivot+1, end)

if __name__ == '__main__':
    a = [4,3,1,5,2]
    quick_sort(a, 0, len(a)-1)
    print(a)