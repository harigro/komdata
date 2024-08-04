import unittest
from units.kombinasi_data import ambil_perbedaan_daftar

class TestAmbilPerbedaanDaftar(unittest.TestCase):

    def test_str(self):
        list1 = ['apple', 'banana', 'cherry']
        list2 = ['banana', 'cherry', 'date']
        expected_result = ['date']
        self.assertEqual(ambil_perbedaan_daftar(list1, list2), expected_result)

    def test_bool(self):
        list1 = [True, False, True]
        list2 = [False, True, True]
        expected_result = []
        self.assertEqual(ambil_perbedaan_daftar(list1, list2), expected_result)

    def test_int(self):
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        expected_result = [4]
        self.assertEqual(ambil_perbedaan_daftar(list1, list2), expected_result)

    # Tambahkan pengujian untuk kasus lain jika diperlukan

if __name__ == '__main__':
    unittest.main()
