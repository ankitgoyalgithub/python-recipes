t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d=[0]*(n)
    d[n-1]=max(l[-1],0)
    for i in range(n-2,-1,-1):
        if i+2>=n:
            d[i]=max(d[i+1],l[i])
        else:
            d[i]=max(l[i]+d[i+2],d[i+1])
    print(d)
    print(d[0])