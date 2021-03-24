# Tämä on painonhallintasovelluksen pääohjelma

# kirjastojen ja modulien käyttöönotot
import laskenta
import kysymys
# Varsinaisen pääohjelman alku

# työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto true on aina voimassa)
uusi = 'K'
while True:

    # tehdään kysymykset modulin kysymys.py funktiota käyttämällä
    paino = kysymys.kysy_liukuluku('paino(kg)', 30, 500)
    pituus = kysymys.kysy_liukuluku('pituus (cm)', 100, 300)
    ika = kysymys.kysy_liukuluku('ikä (v)', 3 ,125)
    sukupuoli = kysymys.kysy_liukuluku('sukupuolinaine: 0, mies:1', 0 , 1)

    # Lasketaan ja tulostetaan painoindeksi
    bmi = laskenta.bmi(paino, pituus)
    print('Henkilön painoindeksi on:',round(bmi, 1))

    # lasketaan ja tulostetaan kehonrasvaprosentti
    rasvaprosentti = laskenta.rasvaprosentti(bmi, ika, sukupuoli)
    print('Laskennallinen kehonrasva prosentti on:', round(rasvaprosentti, 1))

    # poistuminen ikuisesta silmukasta
    uusi = input('lasketaanko uuden henkilön rasvaprosentti? (K/e)')
    if uusi.upper() == 'E':
        break