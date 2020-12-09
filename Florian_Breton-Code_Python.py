from colorama import init 
init() 
from colorama import Fore, Back, Style 
from random import randrange

nombreChoisie=randrange(3)
listeDeMots=['crepis','crabe','parfum']
mot1= listeDeMots[nombreChoisie]
motDonner=''
motDonner=input()
motReserve=''
motReserve1=''
motFinal = ''
print(mot1)
for i in range(0,6):
    motReserve += str(ord(motDonner[i]))
    motReserve += ','
    
    motReserve1 += str(ord(mot1[i]))
    motReserve1 += ','
    
    if (motReserve[i] == motReserve1[i]):
        motFinal += str(Back.RED + motDonner[i])
    if motDonner[i] in mot1:
        motFinal += str(Back.YELLOW + motDonner[i])
        print(Style.RESET_ALL)


print(motReserve)
print(motReserve1)
print(mot1)
print(motFinal)