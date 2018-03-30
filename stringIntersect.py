#Heather Stafford
#3/30/18
#stringIntersect.py

def stringIntersect(word1,word2):
    answer = ''
    for ch in word1 + word2:
        if ch in answer:
            answer = answer - ch
    return(answer)

stringIntersect('mississippi', 'pensylvania')
        
