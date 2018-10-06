def solve(n):
    s=0
    while n!=0:
        s=s+n%10
        n=n//10
    return s

assert solve(2**15)==26
print(solve(2**1000))


