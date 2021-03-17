# Tämä on painonhallintasovelluksen pääohjelma

# kirjastojen ja modulien käyttöönotot
import sanity2
import laskenta

# Varsinaisen pääohjelman alku

# työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto true on aina voimassa)
uusi = 'K'
while True:

    # Kysytään Käyttäjältä paino
    tapahtui_virhe = True
    
    while tapahtui_virhe == True:
        paino_str = input('paino (kg)?')
        tulokset = sanity2.liukuluvuksi(paino_str)

        #katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan
        if tulokset[0] == 0:
            paino = tulokset[2]
            tarkistettu_paino =  sanity2.rajatarkistus(paino, 40, 300)

            # Katsotaan onko arvo sallitujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_paino[0] == 0:
                tapahtui_virhe = False
            else:
                # Tulostetaan virheilmoitus
                print(tarkistettu_paino[1])
                    
        #jos virhekoodi ei ole 0, tulostetaan virheilmoitus
        else:
            print(tulokset[1])

    # testi
    print ('ja paino oli', paino , 'kg')
    
    # poistuminen ikuisesta silmukasta
    uusi = input('lasketaanko uuden henkilön rasvaprosentti? (K/E)')
    if uusi == 'E':
        break