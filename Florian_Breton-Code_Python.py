from colorama import init 
init(wrap = False) 
from colorama import Fore, Back, Style 
from random import randrange


mot1='parfum'
motDonner='bacfgd'
motReserve=[]
motReserve1=[]
motFinal = ''
print(mot1)
print(motDonner)
lettrebonne=''
malposition=''
pasdedans=''


for i in range(0,6):
    if (ord(mot1[i]) == ord(motDonner[i])):
        lettrebonne += str(Back.RED + motDonner[i] + Style.RESET_ALL)
        
    elif ord(motDonner[i]) in motReserve1:
        malposition += str(Back.YELLOW + motDonner[i] + Style.RESET_ALL)
        
    else:
        pasdedans += str(Back.BLUE + motDonner[i] + Style.RESET_ALL)

print("Vous avait les lettres",lettrebonne,"qui est bon")
print("Vous avait les lettres",malposition,"qui est pas a la bonne place") 
print("Vous avait les lettres",pasdedans,"qui est pas dedans")  

print(motReserve1)
print(mot1)
print(motDonner)