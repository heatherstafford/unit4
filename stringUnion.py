#Heather Stafford
#3/29/19
#stringUnion.py

def stringunion(word1,word2):
    answer = ''
    for ch in word1 + word2:
        if ch not in answer:
            answer = answer + ch
    return(answer)
    
print(stringunion('mississippi', 'pennsylvania'))
