#sanity2-modulin testit

#modulin lataus
import sanity2

#raja-Arvotarkastuten testit

#arvo rajojen sisällä virhekoodi 0, virhesanoma arvo ok

def test_rajatarkistus_oikein():
    assert sanity2.rajatarkistus(100, 20, 300) == [0, 'Arvo OK']

# Arvo alle alarajan, virhekoodi 1, virhesanoma 'Arvo on alle alirajan (20)'
def test_rajatarkistus_alle():
    assert sanity2.rajatarkistus(10, 20, 300) == [1,'Arvo on alle alarajan (20)']

    # Arvo yli, virhekoodi 2, virhesanoma 'Arvo on yli ylärajan (300)'
def test_rajatarkistus_yli():
    assert sanity2.rajatarkistus(350, 20, 300) == [2,'Arvo yli ylärajan (300)']

# LIUKULUKUMUUNNOS TESTIT

