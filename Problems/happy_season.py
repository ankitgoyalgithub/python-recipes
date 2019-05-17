n = int(input())
x = input()
result = 0
count_map = { chr(i + 97):0 for i in range(0,26) }

for b in range(n):
    valid_chars = 0
    for d in range(b+1, n):
        if x[b] == x[d]:
            result += valid_chars
        valid_chars += count_map[x[d]]
    count_map[x[b]] += 1
    # print(count_map)
print(result)