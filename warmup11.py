#Heather Stafford
#3/26/18
#warmup11


def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

print(prime(9))
print(prime(10))
print(prime(11))
    
