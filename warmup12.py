#Heather Stafford
#3/29/18
#warmup12.py - returns the GCF of two numbers

def gcf(x,y):
    for i in range(2,x):
        if x%i == 0 and y%i == 0:
            return(i)

print(gcf(12,15))