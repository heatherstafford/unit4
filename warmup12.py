#Heather Stafford
#3/29/18
#warmup12.py - returns the GCF of two numbers

def gcf(x,y):
    for i in range(x,0,-1):
        if x%i == 0 and y%i == 0:
            return(i)

print(gcf(5,9))