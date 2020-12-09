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

for i in range(0,6):
    if motDonner[i] in mot1:
        print(i)
print(mot1)