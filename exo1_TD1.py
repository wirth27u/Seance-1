f=open("french.dic",'r')
# print(f)
# exit()
words=[]
for word in f:
    words.append(word[0:len(word)-1])
f.close()

#Exercice 2#

draw=['b', 'd', 'w', 's','y', 'i']

def possible_words(draw):
    possible_word=[]
    for word in words:
        i=0
        jocker_count=0 #on rajoute un conteur pour mettre le mot même si il manque une lettre : jocker_count
        for letter in word:
            if letter in draw:
                i=i+1
            elif letter not in draw and jocker_count<1:
                i=i+1
                jocker_count+=1
        if len(word)==i:
            possible_word.append(word)
    return possible_word

def longestword(draw):
    possible_word = possible_words(draw)
    ans=possible_word[0]
    for word in possible_word:
        if len(word)>len(ans):
            ans=word
    return ans

print(possible_words(draw))

print(longestword(draw))

#Exercice 3#

letters_points={'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'y':10,'x':10,'z':10,'?':0}
word='chat'
def score(word,draw): #pour l'ex4 on a besoin du tirage pour les score
    total_score=0
    for letter in word :
        if letter in draw: # pour l'ex4 on rajoute une condition au score
            total_score=total_score+letters_points[letter]
    return total_score


def max_score(draw):
    possible_word = possible_words(draw)
    best_word=None
    best_score=0
    for word in possible_word:
        if score(word,draw)>best_score:
            best_score=score(word,draw)
            best_word=word
    return best_word,best_score

print(max_score(draw))
