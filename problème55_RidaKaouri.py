def reverse(n):
    L=list(str(n))
    s=''
    for i in L:
        s=i+s
    return int(s)
    
assert reverse(115)==511
print (reverse(9638))

def is_palindrome(n):
    if n==reverse(n):
        return True
    else: return False
    
assert is_palindrome(737)==True
print(is_palindrome(154))

def is_Lychrel(x):
    for i in range(50):
        if is_palindrome(x)==False:
            x=x+reverse(x)
        else: return False
    return True
 
assert is_Lychrel(196)==True
print(is_Lychrel(47))

L=[x for x in range(10001) if is_Lychrel(x)==True]
print(L)

        
    
        
    