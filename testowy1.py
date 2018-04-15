
plik = open('kroliki.txt','r')
for (numer,text) in enumerate(plik):
    print(numer,":",text,"$")
plik.close()