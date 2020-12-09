from colorama import init 
init(wrap = False) 
from colorama import Fore, Back, Style 
from random import randrange


mot1='parfum'
motDonner='bacfgd'
motReserve=''
motReserve1=''
motFinal = ''
print(mot1)
print(motDonner)

for i in range(0,6):
    motReserve += str(ord(motDonner[i]))
    motReserve += ','
    
    motReserve1 += str(ord(mot1[i]))
    motReserve1 += ','

for i in range(0,6):   
    a = motReserve[i]
    b = motReserve1[i]
    if (a == b):
        motFinal += str(Back.RED + motDonner[i] + Style.RESET_ALL)
    elif a in motReserve1:
        motFinal += str(Back.YELLOW + motDonner[i] + Style.RESET_ALL)
    else:
        motFinal += str(Back.BLUE + motDonner[i] + Style.RESET_ALL)
    
print(motReserve)
print(motReserve1)
print(mot1)
print(motDonner)
print(motFinal)