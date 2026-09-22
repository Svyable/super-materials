import math
import unittest
from super_materials.decision import binary_entropy_bits, posterior_probability, expected_information_gain_bits
from super_materials.kinetics import barrier_for_lifetime
from super_materials.retention import escape_rate, survival_probability, retention_temperature
from super_materials.models import allen_dynes_tc
from super_materials.screening import projected_dos_geomean


class CoreTests(unittest.TestCase):
    def test_entropy(self):
        self.assertAlmostEqual(binary_entropy_bits(0.5), 1.0)
    def test_posterior_positive_increases(self):
        self.assertGreater(posterior_probability(0.25,0.85,0.95,True), 0.25)
    def test_posterior_negative_decreases(self):
        self.assertLess(posterior_probability(0.25,0.85,0.95,False), 0.25)
    def test_information_nonnegative(self):
        self.assertGreater(expected_information_gain_bits(0.25,0.85,0.95), 0)
    def test_kinetic_barrier_77k_days(self):
        e=barrier_for_lifetime(77,3*86400)
        self.assertTrue(0.25 < e < 0.32)
    def test_kinetic_barrier_300k_year(self):
        e=barrier_for_lifetime(300,365*86400)
        self.assertTrue(1.1 < e < 1.3)
    def test_multichannel_escape_rate_exceeds_single_channel(self):
        single=escape_rate(300,[1.2])
        multi=escape_rate(300,[1.2,1.4])
        self.assertGreater(multi,single)
    def test_survival_probability_bounds(self):
        s=survival_probability(300,86400,[1.3])
        self.assertTrue(0 < s < 1)
    def test_retention_temperature_is_finite(self):
        t=retention_temperature(86400,[1.2],target_survival=0.5,max_temperature_k=1000)
        self.assertTrue(250 < t < 400)
    def test_allen_dynes_positive(self):
        self.assertGreater(allen_dynes_tc(1.8,1650),100)
    def test_dos_geomean(self):
        self.assertAlmostEqual(projected_dos_geomean(4,1),2)
    def test_negative_dos_rejected(self):
        with self.assertRaises(ValueError): projected_dos_geomean(-1,1)


if __name__ == '__main__': unittest.main()
