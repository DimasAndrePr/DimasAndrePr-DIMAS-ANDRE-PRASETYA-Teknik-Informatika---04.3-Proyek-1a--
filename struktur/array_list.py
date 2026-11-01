
from product import Produk


class ArrayListProduk:
    def __init__(self):
        # untuk nyimpan kumpulan produk menggunakan Python List
        self.data: list[Produk] = []

    # INSERT: Menambahkan produk baru
    def tambah(self, produk: Produk):
        if not isinstance(produk, Produk):
            raise TypeError("Data harus berupa objek Produk.")

        # untuk pastikan ID produk tidak duplikat
        if self.cari(produk.id_produk) is not None:
            raise ValueError(
                f"Produk dengan ID {produk.id_produk} sudah terdaftar."
            )

        self.data.append(produk)
        return True

    # SEARCH: untuk cari produk berdasarkan ID
    def cari(self, id_produk: str):
        for produk in self.data:
            if produk.id_produk == id_produk:
                return produk

        return None

    # DELETE: untuk hapus produk berdasarkan ID
    def hapus(self, id_produk: str):
        for indeks, produk in enumerate(self.data):
            if produk.id_produk == id_produk:
                return self.data.pop(indeks)

        return None

    # untuk ambil seluruh data produk
    def semua(self):
        return self.data.copy()

    # untuk hitung jumlah produk
    def __len__(self):
        return len(self.data)

    # untuk periksa apakah inventaris kosong
    def kosong(self):
        return len(self.data) == 0
