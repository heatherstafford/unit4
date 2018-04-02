#Heather Stafford
#4/2/18
#quiz4.py

def count(x):
    for i in range(1,x + 1):
        print(i)
        
def excitedPrint(word1):
    print(word1.upper() + '!!!')
    
def firstLetter(word2): 
    letter = ''
    for ch in word2:
        if ch not in letter:
            letter = letter + ch
        return(letter)

def repeats(a,b,c):
    if a == b or a == c or b ==c:
        return(True)
    else:
        return(False)

count(7)
excitedPrint('I <3 programming')
print(firstLetter('Stafford'))
print(repeats(5,6,5))