
from product import Produk


class HashTableProduk:
    def __init__(self):
        # dictionary sebagai implementasi Hash Table
        self.data: dict[str, Produk] = {}

    # INSERT:untuk tambahkan produk baru
    def tambah(self, produk: Produk):
        if not isinstance(produk, Produk):
            raise TypeError("Data harus berupa objek Produk.")

        # untuk pastikan ID produk tidak duplikat
        if produk.id_produk in self.data:
            raise ValueError(
                f"Produk dengan ID {produk.id_produk} sudah terdaftar."
            )

        # ID produk menjadi key dan objek Produk menjadi value
        self.data[produk.id_produk] = produk

        return True

    # SEARCH:untuk cari produk berdasarkan ID
    def cari(self, id_produk: str):
        return self.data.get(id_produk)

    # DELETE:untuk hapus produk berdasarkan ID
    def hapus(self, id_produk: str):
        return self.data.pop(id_produk, None)

    # untuk hapus seluruh data produk
    def semua(self):
        return list(self.data.values())

    # untuk hitung jumlah produk
    def __len__(self):
        return len(self.data)

    # untuk periksa apakah Hash Table kosong
    def kosong(self):
        return len(self.data) == 0
