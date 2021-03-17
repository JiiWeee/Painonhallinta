# Modulin funktioilla voidaan laskea painoindeksi (BMI) ja kehon rasvaprosentti

# Funktioiden määrittelyt

# Painoindeksi
def BMI(paino, pituus):
    """Laskee painoindeksin kaavalla paino jaettuna pituuden neliöllä

    Args:
        paino (float):paino kiloina (kg)
        pituus (float):pituus metreinä (m)

    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / pituus ** 2
    return painoindeksi

# Aikuisen rasvaprosentti
def rasvaprosentti(bMI, ika, sukupuoli):
    """Laskee aikuisen henkilön kehon rasvaprosentin

    Args:
        bMI (float): painoindeksi
        ika (float): ikä vuosina
        sukupuoli ([type]): 1 - Miehet , 0 - Naiset

    Returns:
        float : kehon rasvaprosentti
    """
    rprosentti = 1.2 * bMI + 0.23 * ika - 10.8 * sukupuoli - 5.4
    return rprosentti

# Testit
if __name__ == '__main__':

    # 1 testi omapainoindeksi
    pituus = 1.71
    paino = 74.9
    omabmi = BMI(paino, pituus)
    print('pituus:', pituus, 'paino:', paino, 'painoindeksi', BMI(paino, pituus))

    # 2. testi oma rasvaprosentti
    ika = 59
    sukupuoli = 1
    print('rasvaprosentti:', rasvaprosentti(omabmi, ika, sukupuoli))
