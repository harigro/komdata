import itertools
import string
from enum import Enum


def kombinasi_enum(kategori):
    # Mengambil kombinasi 1 - n dari enum
    combinations = itertools.chain.from_iterable(
        itertools.combinations(kategori, r)
        for r in range(1, len(kategori) + 1))
    # Membuat dict untuk menyimpan hasil kombinasi
    data_dict = {}
    # Iterasi untuk setiap kombinasi
    for combination in combinations:
        # Menggabungkan elemen dari setiap Enum kombinasi menjadi satu string
        combined_string = ''.join(category.value for category in combination)
        # Membuat nama kunci sesuai dengan kombinasi
        key_name = '_'.join(category.name for category in combination)
        # Menyimpan hasil dalam dict
        data_dict[key_name] = combined_string
    return data_dict

def kombinasi_dict(kategori):
    # Mengambil kombinasi 1 - n dari kamus
    combinations = itertools.chain.from_iterable(
        itertools.combinations(kategori.keys(), r)
        for r in range(1, len(kategori) + 1))
    # Membuat dict untuk menyimpan hasil kombinasi
    data_dict = {}
    # Iterasi untuk setiap kombinasi
    for combination in combinations:
        # Menggabungkan elemen dari setiap tuple kombinasi menjadi satu string
        combined_string = ''.join(kategori[key] for key in combination)
        # Membuat nama kunci sesuai dengan kombinasi
        key_name = '_'.join(combination).upper()
        # Menyimpan hasil dalam dict
        data_dict[key_name] = combined_string
    return data_dict

if __name__ == "__main__":
    import pprint
    # Define Enum for character categories
    class CharCategories(Enum):
        UPPERCASE = string.ascii_uppercase
        LOWERCASE = string.ascii_lowercase
        DIGITS = string.digits
        PUNCTUATION = string.punctuation
        
    # Data yang akan dikombinasikan
    data = {
        'uppercase': string.ascii_uppercase,
        'lowercase': string.ascii_lowercase,
        'digits': string.digits,
        'punctuation': string.punctuation}
        
    kk = kombinasi_enum(CharCategories)
    gg = kombinasi_dict(data)
    pp = pprint.PrettyPrinter(sort_dicts=False)
    pp.pprint(kk)
    print()
    pp.pprint(gg)