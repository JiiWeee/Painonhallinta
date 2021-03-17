# Moduli syötteen oikeellisuuden (sanity) tarkistamiseen
"""Tarkistaa Käyttäjän syötteen oikeellisuuden tarkistusfunktioiden avulla
"""


# Funktioiden määrittelyt
def on_jarkeva(syote, alaraja, ylaraja):
    """
    Puhdistaa merkkijonosta ylimääräiset tulostumattomat merkit ja välilyönnit ja
    selvittää onko syötetty arvo annettujen  rajojen sisällä. funktio muuttaa desimaali
    pilkun desimaalipisteeksi.


    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alaraja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo

        Returns (float) : käyttäjän syöttämä arvo numeerisena
    """

    # poistetaan whitespace merkit merkkijono alusta
    puhdistettu_syote = syote.lstrip()

    # poistetaan whitespace merkit merkkijono alusta
    puhdistettu_syote = puhdistettu_syote.rstrip()

    # selvitetään onko  merkkijonossa pilkku (,)
    pilkunpaikka = puhdistettu_syote.find(',')

    # Jos pilkku löytyy, korvataan pisteellä
    if pilkunpaikka != -1:
        korjattu_syote = puhdistettu_syote.replace(',', '.')
    else:
        korjattu_syote = puhdistettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi

    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot sallittu')
        luku = 0
    # tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Tarkistetaan, ettei syöte ole ylärajan yläpuolella
    try:
        if luku > ylaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Palautetaan luku
    return luku

def liukuluku_ok(syote, alaraja, ylaraja):
    """Tarkistaa syötteen olevan numeerinen ja muuttaa sen liukuluvuksi. syötteellä on alaraja ja yläraja

    Args:
        syote (string): Syötteen saatu arvo
        alaraja (float): pienin hyväksytty arvo
        ylaraja (float): suurin hyväksytty arvo

    Returns:
        list: palauttaa arvon(float), virhekoodin (int), virhesanoman (string)
    """
    # Puhdistetaan syötteestä ylimääräoset merkit (white space)
    puhdistettumerkkijono = syote.strip()
    
    # Tutkitaan onko syötteessä pilkku ja etsitään sen paikka
    pilkunpaikka = puhdistettumerkkijono.find(',')
    
    # Jos pilkkulöyti, korvataan pisteellä
    if pilkunpaikka != -1: # jos ei löydy indeksi on aina -1
       numeroarvo = puhdistettumerkkijono.replace(',', '.') # Muutetaan
    else:
        numeroarvo = puhdistettumerkkijono # ei muuteta

    # Etsitään desimaalipistettä merkkijonosta
    pisteenpaikka = numeroarvo.find('.')
    
    # Jos desimaalipiste löytyy jaetaan pisteen kohdalta erillisiksi merkkijonoiksi
    if pisteenpaikka != -1:
        osat = numeroarvo.split('.') # syntyy lista osista
        osien_maara = len(osat)
        #Selvitetään onko osia enemmäin kuin 2 so. liikaa pilkkuja tai pisteitä
        if osien_maara > 2:
            virhekoodi = 1
            Virhesanoma = "Syöteessä on useita desimaalipisteitä tai useita arvoja: vain yksi liukuluku on sallittu, esim 12.3"
            arvo = 0

        # Muussa tapauksessa selvitetään onko alkuosassa pelkkiä numeroita
        else:
            osa = str(osat[0])
            if osa.isnumeric() == False:
                virhekoodi = 2
                Virhesanoma = "syöte sisältää tekstiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim 123.5"
                arvo = 0
            # selvitetään onko loppuosassa pelkkiä numeroita
            else:
                osa = str(osat[1])
                if osa.isnumeric() == False:
                    virhekoodi = 2
                    Virhesanoma = "syöte sisältää tekstiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim 123.5"
                    arvo = 0
                # Jos ei ollut asetetaan arvo ja nollataan virheilmoitukset    
                else:
                    virhekoodi = 0
                    Virhesanoma = "Syöte ok"
                    arvo = float(numeroarvo)

    # Jos yksiosainen syöte sisältää muutakin kuin pelkkiä numeroita
    elif numeroarvo.isnumeric() == False:
        virhekoodi = 2
        Virhesanoma = "syöte sisältää tekstiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim 123.5"
        arvo = 0

    # Yksiosainen syöte ok    
    else:
        virhekoodi = 0
        Virhesanoma = "Syöte ok"
        arvo = float(numeroarvo)

              
    # Muodostetaan ja palautetaan funktion paluuarvo        
    tulokset = [virhekoodi, Virhesanoma, arvo]
    return tulokset

# Jos sanity.py-tiedostoa ajetaan terminalissa, suoritetaan testit
if __name__ == '__main__':
    
#     Testataan toimintaa
#     tulos = on_jarkeva('123', 1, 500)
#     print(tulos)
#     syote = ' 10.5   '
#     print(syote.strip(), 'kiloa')

    # Testataan
    syote = '123.5'
    print(liukuluku_ok(syote, 0, 500))