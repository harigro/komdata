import unittest
import string
from units.kombinasi_data import kombinasi_kamus

data = {
        'uppercase': string.ascii_uppercase,
        'lowercase': string.ascii_lowercase,
        'digits': string.digits,
        'punctuation': string.punctuation
    }

class TestKombinasiEnum(unittest.TestCase):

    def setUp(self):
        self.result = kombinasi_kamus(data)

    def test_combinations_length(self):
        # Test panjang data
        self.assertEqual(len(self.result), 15)

    def test_combination_existence(self):
        # Test apakah kombinasi tertentu ada dalam hasil
        self.assertIn('UPPERCASE', self.result)
        self.assertIn('LOWERCASE', self.result)
        self.assertIn('DIGITS', self.result)
        self.assertIn('PUNCTUATION', self.result)
        self.assertIn('UPPERCASE_LOWERCASE', self.result)
        self.assertIn('UPPERCASE_DIGITS_PUNCTUATION', self.result)
        self.assertIn('LOWERCASE_DIGITS', self.result)

    def test_combination_values(self):
        # Test nilai dari kombinasi tertentu
        self.assertEqual(self.result['UPPERCASE'], string.ascii_uppercase)
        self.assertEqual(self.result['LOWERCASE'], string.ascii_lowercase)
        self.assertEqual(self.result['DIGITS'], string.digits)
        self.assertEqual(self.result['PUNCTUATION'], string.punctuation)
        self.assertEqual(self.result['UPPERCASE_LOWERCASE'], string.ascii_uppercase + string.ascii_lowercase)
        self.assertEqual(self.result['UPPERCASE_DIGITS_PUNCTUATION'], string.ascii_uppercase + string.digits + string.punctuation)
        self.assertEqual(self.result['LOWERCASE_DIGITS'], string.ascii_lowercase + string.digits)

if __name__ == '__main__':
    unittest.main()

