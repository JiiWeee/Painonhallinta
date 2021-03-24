#kysymysmodulin testit

#Modulien ja kirjastojen lautaukset
import kysymys

#syöte ok
def test_kysymys_ok():
    kysymys.input = lambda: '50'
    assert kysymys.kysy_liukuluku('painosi (kg)', 20, 350) == 50
    
# Syötteessä tietotyyppivirhe

#alle alarajan

#yli ylärajan