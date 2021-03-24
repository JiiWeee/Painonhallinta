# Tässä modulissa määritellään luokat painonhallintasovellukseen

#modulien ja kirjastojen lataukset


# henkilö-luokka

class Henkilo:
    """yliluokka kaikille henkilötyypeille."""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):
       
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        
    def painoindeksi(self):
        bmi = self.paino / (self.pituus / 100) ** 2
        return bmi

class Aikuinen(Henkilo):
    """Aliluokka aikuiselle henkilölle, perii Henkilo-luokan ominaisuudet 
    ja metodit"""

    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        self.arg = tavoitepaino

    def rasvaprosentti(self):
        
        rasvaprosentti = 1.2 * self.painoindeksi() + 0.23 * self.ika - 10.8 * self.sukupuoli - 5.4
        return rasvaprosentti




if __name__ == "__main__":
    mikaV = Henkilo('mika', 'vainio', 171, 74, 59, 1)
    print('henkilö painaa', mikaV.paino)

    mikaV.painoindeksi()

mikaV2 = Aikuinen('mika', 'Vainio', 171, 74, 59, 1, 70)
print(mikaV2.etunimi, 'painoindeksi', mikaV2.painoindeksi())
print(mikaV2.etunimi,'Rasvaprosentti', mikaV2.rasvaprosentti())



