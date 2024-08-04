import unittest
from units.kombinasi_data import saring_nilai

class TestSaringNilai(unittest.TestCase):

    def test_saring_nilai_benar(self):
        bb = [True, False, 1, 0, 3.14, '', 'hello']
        expected_result = [True, 1, 3.14, 'hello']

        result = saring_nilai(bb, True)
        self.assertEqual(result, expected_result)

    def test_saring_nilai_salah(self):
        bb = [True, False, 1, 0, 3.14, '', 'hello']
        expected_result = [False, 0, '']

        result = saring_nilai(bb, False)
        self.assertEqual(result, expected_result)

    def test_saring_nilai_with_mixed_types(self):
        bb = [True, False, 1, 0, 3.14, '', 'hello']
        expected_result_true = [True, 1, 3.14, 'hello']
        expected_result_false = [False, 0, '']

        result_true = saring_nilai(bb, True)
        result_false = saring_nilai(bb, False)

        self.assertEqual(result_true, expected_result_true)
        self.assertEqual(result_false, expected_result_false)

    def test_saring_nilai_empty_list(self):
        bb = []
        expected_result_true = []
        expected_result_false = []

        result_true = saring_nilai(bb, True)
        result_false = saring_nilai(bb, False)

        self.assertEqual(result_true, expected_result_true)
        self.assertEqual(result_false, expected_result_false)

if __name__ == '__main__':
    unittest.main()
