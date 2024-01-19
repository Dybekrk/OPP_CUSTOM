gracz_1 = input('Podaj imie 1 gracza: ')
gracz_2 = input('Podaj imie 2 gracza: ')

gracz_1_odpowiedz = input(' %s:Wybierz papier,kamien czy nozyce : ' % gracz_1)
gracz_2_odpowiedz = input(' %s:Wybierz papier,kamien czy nozyce : ' % gracz_2)

def porownaj (odp_1, odp_2):
    if odp_1 == odp_2:
        return('remis')
    elif odp_1 == 'kamien':
        if odp_2 == 'nozyczki':
            return ('kamien win')
        else :
            return('papier win')
                      
    elif odp_1 == 'nozyczki':
        if odp_2 == 'papier':
            return ('nozyczki win')
        else:
            return('kamien win')         
        
    elif odp_1 == 'papier':   
        if odp_2 == 'kamien':
            return ('papier win')
        else:
            return('nozyczki win')
            
    else :
        print ('nie ma takiego wyboru')
  
      
     
    print(porownaj(gracz_1_odpowiedz,gracz_2_odpowiedz))
    