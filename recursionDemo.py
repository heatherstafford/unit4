#Heather Stafford
#3/29/18
#recusionDemo.py - recursive version of countdown

def countdownr(n):
    if n == 0: #base case
        print('BOOM!') 
    else:
        print(n)
        countdownr(n-1)
        
countdownr(5)
