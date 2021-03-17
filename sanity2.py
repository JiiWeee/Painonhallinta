# Tiivistetty versio Sanity.py-modulista eli suurinpiirtein se, mitä tuhosin vahingossa

def liukuluvuksi(syote):
    """Tarkistaa syötteen ja muuttaa sen liukuluvuksi

    Args:
        syote (string): Käyttäjän syöttämä arvo

    Returns:
        list: virhekoodi, virhesanoma ja syöte liukulukuna
    """

    # Asetetaan palautusarvojen oletukset
    virhekoodi = 0
    virhesanoma = 'Syöte OK'
    arvo = 0

    # Puhdistetaan syöte ylimääräisistä merkeistä (Whitespace)
    syote = syote.strip()

    # Selvitetään sisältääko syöte mahdollisen desimaalipilkun ja korvataan se pisteellä
    if syote.find(',') != -1:
        syote = syote.replace(',', '.')

    # Selvitetään sisältääkö syöte desimaalipisteen ja jaetaan syöte pisteen kohdalta useammaksi merkkijonoksi
    if syote.find('.') != -1:
        osat = syote.split('.')

        # Selvitetään onko osia enemmän kuin 2, eli onko useita pisteitä
        if len(osat) > 2:
            virhekoodi = 1
            virhesanoma = 'Syöte sisältää useita erottimia. Vain yksi arvo on sallittu'
            
        # Jos osia on 2
        else:
            osa = str(osat[0])  

            # Jos ensimmäinen osa on numeerinen ts. ei sisällä muita merkkejä kuin 0...9      
            if osa.isnumeric():
                osa = str(osat[1])

                # Jos toinenkin osa on numeerinen
                if osa.isnumeric():
                    arvo = float(syote)
                else:
                    virhekoodi = 4
                    virhesanoma =  'Desimaalierottimen jälkeen ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu'

            else:
                virhekoodi = 3
                virhesanoma = 'Ennen desimaalierotinta ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu'
                

    # Tarkistetaan onko desimaaliton syöte numeerista
    elif syote.isnumeric():
        arvo = float(syote)
    else:
        virhekoodi = 2
        virhesanoma = 'Syötteessä ylimäärisiä merkkejä: vain numerot ja desimaalipiste on sallittu'   
    
    # Muodostetaan funktion paluuarvo ja palautetaan se
    paluuarvo = [virhekoodi, virhesanoma, arvo]
    return paluuarvo
    
    
#Funktio, Jolla tarkistetaan , että syötetty arvo on haluttujen rajojen sisällä
def rajatarkistus(arvo, alaraja, ylaraja):
        """tarkistaa, että syötetty arvo on suurempi tai yhtäsuuri kuin alaraja ja pienempi

        Args:
            arvo (float): tarkistettava arvo
            alaraja (float): pienin sallittu arvo
            ylaraja (float): suurin sallittu arvo

        Returns:
            list: virhekoodi, virheilmoitus
        """
        # Määritellään virheiden oletusarvot
        virhekoodi = 0
        virhesanoma = 'Arvo OK'

        #arvo alle alarajan
        if arvo < alaraja:
            virhekoodi = 1
            virhesanoma = 'Arvo on alle alarajan (' + str(alaraja) + ')'
        
        
        #arvo yli ylärajan
        if arvo > ylaraja:
            virhekoodi = 2
            virhesanoma = 'Arvo yli ylärajan (' + str(ylaraja) + ')'

        #Paluu arvon määritys ja paulautus
        paluuarvo = [virhekoodi, virhesanoma]
        return paluuarvo

#Funktioiden testaus
if __name__ == '__main__':
    
    # 1. Syötteen tarkistus, Syöte oikein
    syote = '123.5'
    print('syöte:', syote, 'tulokset : ' ,liukuluvuksi(syote))


    # 2. Syötteessä desimaalipilkku, muuten oikein
    syote = '123,5'
    print('syöte:', syote, 'tulokset : ' ,liukuluvuksi(syote))

    # 3. Syötteessä useita osia 
    syote = '12.3.2'
    print('syöte:', syote, 'tulokset : ' ,liukuluvuksi(syote))

    # 4. Syötteessä Alussa tekstiä
    syote = 'paino 75.4'
    print('syöte:', syote, 'tulokset : ' ,liukuluvuksi(syote))

    # 5. Syötteen lopussa  tekstiä
    syote = '75.4kg'
    print('syöte:', syote, 'tulokset : ' ,liukuluvuksi(syote))
    
    # Syöte kokonaisuudessaan tekstiä
    syote = 'sataviisi'
    print('syöte:', syote, 'tulokset : ' ,liukuluvuksi(syote))


    # Rajatarkistukset

    alaraja = 1
    ylaraja = 3

    # 1. Rajojen sisällä 
    arvo = 1.8
    print('arvo:', arvo, 'tulokset:', rajatarkistus(arvo, alaraja, ylaraja))

    # 2. alle alarajan
    arvo = 0.8
    print('arvo:', arvo, 'tulokset:', rajatarkistus(arvo, alaraja, ylaraja))

    # 3. yli ylärajan
    arvo = 3.8
    print('arvo:', arvo, 'tulokset:', rajatarkistus(arvo, alaraja, ylaraja))
