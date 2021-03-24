# Modulin funktioilla voidaan laskea painoindeksi (bmi) ja kehon rasvaprosentti

# Funktioiden määrittelyt

# Painoindeksi
def bmi(paino, pituus):
    """Laskee painoindeksin kaavalla paino jaettuna pituuden sadasosan neliöllä

    Args:
        paino (float):paino kiloina (kg)
        pituus (float):pituus senttimetreinä (cm)

    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / (pituus/100) ** 2
    return painoindeksi

# rasvaprosentti
def rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee henkilön kehon rasvaprosentin

    Args:
        bMI (float): painoindeksi
        ika (float): ikä vuosina
        sukupuoli (int): 1 - Miehet , 0 - Naiset

    Returns:
        float : kehon rasvaprosentti
    """

    if ika >= 18:
        #aikuisen rasvaprosentti
        rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    else:
        #lapsen rasvaprosentti
        rprosentti = 1.51 * bmi - 0.70 * ika - 3.6 *sukupuoli + 1.4

    return rprosentti

# Testit
if __name__ == '__main__':

    # 1 testi omapainoindeksi
    pituus = 171
    paino = 74.9
    omabmi = bmi(paino, pituus)
    print('pituus:', pituus, 'paino:', paino, 'painoindeksi', bmi(paino, pituus))

    # 2. testi oma rasvaprosentti
    ika = 59
    sukupuoli = 1
    print('rasvaprosentti:', rasvaprosentti(omabmi, ika, sukupuoli))
