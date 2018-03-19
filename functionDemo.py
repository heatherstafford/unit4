#Heather Stafford
#3/9/18
#fuctionDemo.py - how to write our own functions

def hw():
    print('Hello, World')

def double(thingToDouble):
    print(thingToDouble *2)

def bigger(a,b):
    if a>b:
        print(a)
    else:
        print(b)
        
def slope(x1, y1,x2, y2):
    print((y2-y1)/(x2-x1))

print("The max if 3 and 4 is", max(3,4))
print("The max if 3 and 4 is", bigger(3,4))

"""
hw()
double(12)
double('w')
bigger(4,3)
bigger("Stafford", "Heath")
slope(1,1,2,2)
"""