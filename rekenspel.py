# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:38:29 2019

@author: K
"""
#MENU
naam = input('Hoe heet jij? ')
print('Hello ' + naam + '! Laten we beginnen')
from random import randint
def main():
    menu = input('''Maak een keuze: 
        
        (1) Plussom, 
        (2) Minsom, 
        (3) Keersom,
        (4) Deelsom.
        
        > ''')
    menu = int(menu)
   
    if menu == 1:
        print('Plussom')
        score_1 = 0
        teller = 0
        for teller in range (5):
            getal1 = randint(1,20)
            getal2 = randint(1,20)
            som = getal1 + getal2
            print(str(getal1), '+', str(getal2), '=')
            answer = int(input())
            if som == answer: 
                print('Je bent correct')
                score_1 += 1
            else:
                print('Helaas, slechte antwoord. Goede antwoord is: ' + str(som))
        print('Geweldig', naam +', je score:', str(score_1))
        keuze = input(''' 
        Wilt u nog oefenen? 
        Ja of nee? (j/n)
        > ''')
        if keuze == 'j':
            main() 
        else:
            print('Bedankt en tot ziens!')
            
    elif menu == 2:
        print('Minsom')        
        score_2 = 0
        teller = 0
        for teller in range (5):
            getal1 = randint(1,25)
            getal2 = randint(1,25)
            getal3 = getal1 + getal2
            som = getal3 - getal2
            print(str(getal3) + '-' + str(getal2), '=')
            answer = int(input())
            if som == answer: 
                print('Je bent correct!')
                score_2 += 1
            else:
                print('Helaas, slechte antwoord. Goede antwoord is: ' + str(som))   
        print('Geweldig', naam +', je score:', str(score_2))
        keuze = input('''
        Wilt u nog oefenen? 
        Ja of nee? (j/n)
        >''')
        if keuze == 'j':
            main()
        else:
            print('Bedankt en tot ziens!')
            
    elif menu == 3:
        print('Keersom')
        score = 0
        teller = 0
        for teller in range (5):
            getal1 = randint(1,20)
            getal2 = randint(1,10)
            som = getal1 * getal2
            print(str(getal1) + '*' + str(getal2), '=')
            answer = int(input())
            if som == answer: 
                print('Je bent correct!')
                score += 1
            else:
                print('Helaas, slechte antwoord. Goede antwoord is: ' + str(som))  
        print('Geweldig', naam +', je score:', str(score))
        keuze = input('''
        Wilt u nog oefenen? 
        Ja of nee? (j/n)
        >''')
        if keuze == 'j':
            main()
        else:
            print('Bedankt en tot ziens!')
            
    else:
        print('Deelsom')
        score = 0
        teller = 0
        for teller in range (5):
            getal1 = randint(1,10)
            getal2 = randint(1,10)
            getal3 = getal1 * getal2
            som = getal3 / getal1
            print(str(int(getal3)) + ' / ' + str(getal1), '=')
            answer = int(input())
            if som == answer: 
                print('Je bent correct!')
                score += 1
            else:
                print('Helaas, slechte antwoord. Goede antwoord is: ' + str(int(som)))   
        print('Geweldig', naam +', je score:', str(score))
        keuze = input('''
        Wilt u nog oefenen? 
        Ja of nee? (j/n)
        >''')
        if keuze == 'j':
            main()
        else:
            print('Bedankt en tot ziens!')
            
main()