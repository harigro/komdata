import itertools
from enum import Enum
from typing import Dict, List

def saring_nilai(bb: List[bool], nilai_benar: bool) -> List[bool]:
    """
    Deskripsi:
        - Membentuk daftar baru berupa nilai-nilai benar atau salah dari sebuah daftar
    """
    if nilai_benar:
        return list(filter(lambda x: x, bb))
    else:
        return list(itertools.filterfalse(lambda x: x, bb))

def ambil_perbedaan_daftar(data1: List[str], data2: List[str]) -> List[str]:
    """
    Deskripsi:
        - Membentuk elemen-elemen baru dari data2 yang tidak ada di data1
    """
    set1 = set(data1)
    set2 = set(data2)
    result_set = set2.difference(set1)
    return sorted(list(result_set))

def kombinasi_enum(kategori: Enum) -> Dict[str, str]:
    """
    Deskripsi:
        - Membentuk kamus baru yang berisi  kombinasi yang mungkin berdasarkan panjang data kelas Enum
    """
    combinations = itertools.chain.from_iterable(
        itertools.combinations(kategori, r)
        for r in range(1, len(kategori) + 1))
    data_kamus = {}
    for combination in combinations:
        combined_string = ''.join(category.value for category in combination)
        key_name = '_'.join(category.name for category in combination)
        data_kamus[key_name] = combined_string
    return data_kamus

def kombinasi_kamus(kategori: Dict[str, str]) -> Dict[str, str]:
    """
    Deskripsi:
        - Membentuk kamus baru yang berisi kombinasi yang mungkin berdasarkan panjang data kamus
    """
    combinations = itertools.chain.from_iterable(
        itertools.combinations(kategori.keys(), r)
        for r in range(1, len(kategori) + 1))
    data_kamus = {}
    for combination in combinations:
        combined_string = ''.join(kategori[key] for key in combination)
        key_name = '_'.join(combination).upper()
        data_kamus[key_name] = combined_string
    return data_kamus

def kombinasi_kamus_indeks(kategori: Dict[str, str]) -> Dict[str, list]:
    """
    Deskripsi:
        - Membentuk kamus baru yang berisi kombinasi kunci dan nilai yang mungkin beserta informasi indeks.
    """
    keys = list(kategori.keys())
    n = len(keys)
    data_kamus = {}
    for r in range(1, n + 1):
        combinations = itertools.combinations(keys, r)
        for combination in combinations:
            indices = [keys.index(key) for key in combination]
            false_indices = [i for i in range(n) if i not in indices]
            combined_string = ''.join(kategori[key] for key in combination)
            key_name = '_'.join(combination).upper()
            data_kamus[key_name] = [combined_string, indices, false_indices]
    return data_kamus
