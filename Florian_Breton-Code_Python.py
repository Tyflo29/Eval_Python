from colorama import init 
init() 
from colorama import Fore, Back, Style 

mot1='crépis'
motDonner=''
motDonner=input()
motReserve=''

for i in range(0,6):
    if motDonner[i] in mot1:
        print(i)
