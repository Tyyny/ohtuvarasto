import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuuden_nollaus(self):
        self.varasto = Varasto(-3)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)
    
    def test_alku_saldo_nollaus(self):
        self.varasto = Varasto(10, -3)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_alku_saldo_suurempi_kuin_tilavuus(self):
        self.varasto = Varasto(3, 10)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisaa_varastoon_alle_nolla_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisaa_varastoon_ylimenevat_hukataan(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_alle_nollan_ottaminen_palauttaa_nolla(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(-5)
        
        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_yli_saldon_ottaminen_ottaa_kaiken_mita_voidaan(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(200)

        self.assertAlmostEqual(saatu_maara, 5)
    
    def test_yli_saldon_ottaminen_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(200)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_varaston_tulostus_toimii_oikein(self):
        tulostus = str(self.varasto)
        self.assertEqual(tulostus, "saldo = 0.0, vielä tilaa 10")