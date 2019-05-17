def fib(n):
    if(n==0 or n==1):
        return n
    else:
         return fib(n-1)+fib(n-2) 





def feb1(n):
    first=1
    second=1
    for i in range(2, n):
        third=first+second
        first=second
        second=third
   
    return third

# print(fib(100))
print(feb1(1))
# print(feb1(110))
# print(feb1(10))
# print(feb1(1))
# print(feb1(5))
# print(feb1(3))

