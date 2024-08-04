import unittest
from units.kombinasi_data import kombinasi_kamus_indeks


class TestKombinasiKamusIndeks(unittest.TestCase):

    def test_empty_input(self):
        result = kombinasi_kamus_indeks({})
        self.assertEqual(result, {})

    def test_single_category(self):
        input_data = {'A': 'apple', 'B': 'banana'}
        result = kombinasi_kamus_indeks(input_data)
        expected_keys = ['A', 'B']
        for key in expected_keys:
            self.assertIn(key.upper(), result)

    def test_multiple_categories(self):
        input_data = {'A': 'apple', 'B': 'banana', 'C': 'cherry'}
        result = kombinasi_kamus_indeks(input_data)
        expected_keys = ['A', 'B', 'C', 'A_B', 'A_C', 'B_C', 'A_B_C']
        for key in expected_keys:
            self.assertIn(key.upper(), result)

    def test_key_value_combinations(self):
        input_data = {'A': 'apple', 'B': 'banana', 'C': 'cherry'}
        result = kombinasi_kamus_indeks(input_data)
        self.assertEqual(result['A'], ['apple', [0], [1, 2]])
        self.assertEqual(result['B'], ['banana', [1], [0, 2]])
        self.assertEqual(result['C'], ['cherry', [2], [0, 1]])
        self.assertEqual(result['A_B'], ['applebanana', [0, 1], [2]])
        self.assertEqual(result['A_C'], ['applecherry', [0, 2], [1]])
        self.assertEqual(result['B_C'], ['bananacherry', [1, 2], [0]])
        self.assertEqual(result['A_B_C'], ['applebananacherry', [0, 1, 2], []])

if __name__ == '__main__':
    unittest.main()
