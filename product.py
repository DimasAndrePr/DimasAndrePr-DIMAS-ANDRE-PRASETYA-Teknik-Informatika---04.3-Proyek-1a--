
from dataclasses import dataclass
import math


@dataclass
class Produk:
    # Atribut data produk
    id_produk: str
    nama_produk: str
    harga: float
    stok: int
    kategori: str

    def __post_init__(self):
        # Memastikan atribut teks tidak kosong
        self.id_produk = self.id_produk.strip()
        self.nama_produk = self.nama_produk.strip()
        self.kategori = self.kategori.strip()

        if not self.id_produk:
            raise ValueError("ID produk tidak boleh kosong.")

        if not self.nama_produk:
            raise ValueError("Nama produk tidak boleh kosong.")

        if not self.kategori:
            raise ValueError("Kategori produk tidak boleh kosong.")

        # pastikan harga berupa angka yang valid
        if (
            isinstance(self.harga, bool)
            or not isinstance(self.harga, (int, float))
            or not math.isfinite(self.harga)
            or self.harga < 0
        ):
            raise ValueError("Harga harus berupa angka positif atau nol.")

        self.harga = float(self.harga)

        # pastikan stok berupa bilangan bulat nonnegatif
        if (
            isinstance(self.stok, bool)
            or not isinstance(self.stok, int)
            or self.stok < 0
        ):
            raise ValueError("Stok harus berupa bilangan bulat positif atau nol.")

    def __str__(self):
        return (
            f"ID Produk : {self.id_produk}\n"
            f"Nama      : {self.nama_produk}\n"
            f"Harga     : Rp{self.harga:,.2f}\n"
            f"Stok      : {self.stok}\n"
            f"Kategori  : {self.kategori}"
        )
