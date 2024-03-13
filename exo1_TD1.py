f = open("frenchssaccent.dic",'r')
liste=[]
for ligne in f:
    liste.append(ligne[0:len(ligne)-1])
f.close()