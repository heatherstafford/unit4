#Heather Stafford
#3/29/19
#stringUnion.py

def stringunion(word1,word2):
    for ch in word1 + word2:
        print(ch)
    answer = (' ')
    if ch not in answer:
        answer = answer + ch
    
print(stringunion('mississippi', 'pennsylvania'))
