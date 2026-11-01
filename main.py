
from product import Produk
from struktur.hash_table import HashTableProduk


# membuat inventaris produk
inventaris = HashTableProduk()


# input harga produk
def input_harga():
    while True:
        try:
            harga = float(input("Harga produk  : Rp"))

            if harga < 0:
                print("Harga tidak boleh negatif.")
                continue

            return harga

        except ValueError:
            print("Masukkan harga dalam bentuk angka.")


# input stok produk
def input_stok():
    while True:
        try:
            stok = int(input("Stok produk   : "))

            if stok < 0:
                print("Stok tidak boleh negatif.")
                continue

            return stok

        except ValueError:
            print("Stok harus berupa bilangan bulat.")


# menambahkan produk baru
def tambah_produk():
    print("\nPendaftaran produk baru")

    try:
        id_produk = input("ID produk     : ").strip().upper()
        nama_produk = input("Nama produk   : ").strip()
        harga = input_harga()
        stok = input_stok()
        kategori = input("Kategori      : ").strip()

        # membuat objek produk
        produk = Produk(
            id_produk=id_produk,
            nama_produk=nama_produk,
            harga=harga,
            stok=stok,
            kategori=kategori
        )

        # menambahkan produk ke hash table
        inventaris.tambah(produk)

        print("\nProduk berhasil didaftarkan.")

    except (ValueError, TypeError) as error:
        print(f"\nGagal menambahkan produk: {error}")


# mencari produk berdasarkan ID
def cari_produk():
    print("\nPencarian produk")

    id_produk = input("Masukkan ID produk: ").strip().upper()

    # mencari produk menggunakan key
    produk = inventaris.cari(id_produk)

    if produk is None:
        print("\nProduk tidak ditemukan.")
        return

    print("\nProduk berhasil ditemukan.")
    print("-" * 35)
    print(produk)
    print("-" * 35)


# menghapus produk
def hapus_produk():
    print("\nPenghapusan produk")

    id_produk = input("Masukkan ID produk: ").strip().upper()

    # menghapus produk berdasarkan ID
    produk = inventaris.hapus(id_produk)

    if produk is None:
        print("\nProduk tidak ditemukan.")
        return

    print("\nProduk berhasil dihapus.")
    print("ID Produk :", produk.id_produk)
    print("Nama      :", produk.nama_produk)


# menampilkan seluruh produk
def tampilkan_produk():
    print("\nDaftar inventaris produk")

    daftar_produk = inventaris.semua()

    if not daftar_produk:
        print("Inventaris masih kosong.")
        return

    print("-" * 85)
    print(
        f"{'ID PRODUK':<13}"
        f"{'NAMA PRODUK':<25}"
        f"{'HARGA':<17}"
        f"{'STOK':<8}"
        f"{'KATEGORI'}"
    )
    print("-" * 85)

    for produk in daftar_produk:
        print(
            f"{produk.id_produk:<13}"
            f"{produk.nama_produk:<25}"
            f"Rp{produk.harga:,.0f}   "
            f"{produk.stok:<8}"
            f"{produk.kategori}"
        )

    print("-" * 85)
    print("Total produk:", len(inventaris))


# menu utama
def main():
    while True:
        print("\nSistem Manajemen Inventaris Produk E-Commerce")
        print("---------------------------------------------")
        print("1. Mendaftarkan produk baru")
        print("2. Mencari produk berdasarkan ID")
        print("3. Menghapus produk")
        print("4. Menampilkan seluruh produk")
        print("5. Keluar")
        print("---------------------------------------------")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_produk()

        elif pilihan == "2":
            cari_produk()

        elif pilihan == "3":
            hapus_produk()

        elif pilihan == "4":
            tampilkan_produk()

        elif pilihan == "5":
            print("\nProgram selesai. Terima kasih.")
            break

        else:
            print("\nPilihan tidak tersedia. Silakan coba lagi.")


# menjalankan program
if __name__ == "__main__":
    main()
