#Heather Stafford
#3/30/18
#stringIntersect.py

def stringIntersect(word1,word2):
    answer = ''
    for ch in word1:
        if ch in word2 and ch not in answer:
            answer = answer + ch
    return(answer)
    
print(stringIntersect('mississippi', 'pensylvania'))
        
