def gcd(a,b):
    if b == 0:
        return a
    else: 
        print(b,a%b)
        return gcd(b, a%b)

if __name__ == '__main__':
    print(gcd(20,25))