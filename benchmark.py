
import csv
import statistics
import time

from pathlib import Path

from product import Produk
from struktur.array_list import ArrayListProduk
from struktur.linked_list import LinkedListProduk, Node
from struktur.hash_table import HashTableProduk



#konfigurasi benchmark
UKURAN_DATA = [1_000, 10_000, 100_000]

JUMLAH_SAMPEL = 7
PENGULANGAN_CARI = 100

LOKASI_PROYEK = Path(__file__).resolve().parent
FOLDER_HASIL = LOKASI_PROYEK / "hasil"
FILE_HASIL = FOLDER_HASIL / "hasil_benchmark.csv"



#membuat data produk
def buat_data_produk(jumlah):
    """
    Membuat data produk dengan ID yang unik.
    Dataset dibuat sebelum pengukuran dimulai.
    """

    return [
        Produk(
            id_produk=f"PRD{i:06d}",
            nama_produk=f"Produk {i}",
            harga=float(10000 + i),
            stok=100,
            kategori="Elektronik"
        )
        for i in range(1, jumlah + 1)
    ]



# membangun data set array-based list
def buat_array_list(data_produk):
    inventaris = ArrayListProduk()

    # Menyalin data awal tanpa menghitung waktu setup
    inventaris.data = data_produk.copy()

    return inventaris



# membangun dataset linked list
def buat_linked_list(data_produk):
    inventaris = LinkedListProduk()

    # Membuat node satu per satu
    for produk in data_produk:

        node_baru = Node(produk)

        if inventaris.head is None:
            inventaris.head = node_baru
            inventaris.tail = node_baru

        else:
            inventaris.tail.next = node_baru
            inventaris.tail = node_baru

        inventaris.size += 1

    return inventaris



# membangun dataset hash table
def buat_hash_table(data_produk):
    inventaris = HashTableProduk()

    # ID produk menjadi key
    inventaris.data = {
        produk.id_produk: produk
        for produk in data_produk
    }

    return inventaris



# fungsi pengukuran waktu
def ukur_operasi(pembuat_struktur, fungsi_operasi, pengulangan=1):
    """
    Mengukur waktu eksekusi sebuah operasi.

    Persiapan struktur data dilakukan di luar timer.
    Setiap pengujian dilakukan sebanyak 7 sampel.
    Hasil pengukuran menggunakan satuan mikrodetik.
    """

    hasil_sampel = []

    for _ in range(JUMLAH_SAMPEL):

        # Membangun struktur data sebelum pengukuran
        struktur_data = pembuat_struktur()

        waktu_awal = time.perf_counter_ns()

        for _ in range(pengulangan):

            hasil = fungsi_operasi(struktur_data)

            # Memastikan operasi berhasil
            if hasil is None or hasil is False:
                raise RuntimeError(
                    "Operasi benchmark gagal. "
                    "Periksa implementasi dan data."
                )

        waktu_akhir = time.perf_counter_ns()

        # Konversi nanodetik ke mikrodetik
        # Hasil dibagi jumlah pengulangan
        waktu_us = (
            (waktu_akhir - waktu_awal)
            / pengulangan
            / 1_000
        )

        hasil_sampel.append(waktu_us)

    return {
        "rata_rata": statistics.mean(hasil_sampel),
        "median": statistics.median(hasil_sampel),
        "minimum": min(hasil_sampel),
        "maksimum": max(hasil_sampel)
    }



# menampilkan hasil pengukuran
def tampilkan_hasil(hasil):

    print(
        f"\n{'Struktur Data':<22}"
        f"{'Rata-rata (us)':>18}"
        f"{'Median (us)':>18}"
        f"{'Minimum (us)':>18}"
    )

    print("-" * 76)

    for data in hasil:

        print(
            f"{data['struktur_data']:<22}"
            f"{data['rata_rata_us']:>18.3f}"
            f"{data['median_us']:>18.3f}"
            f"{data['minimum_us']:>18.3f}"
        )



# menjalankan perbandingan dua struktur data
def bandingkan(
    jumlah,
    nama_operasi,
    id_diuji,
    kandidat,
    pengulangan=1,
    catatan=""
):
    semua_hasil = []

    print(f"\nJumlah data: {jumlah:,} produk")
    print(f"ID yang diuji: {id_diuji}")
    print(f"Operasi: {nama_operasi}")

    for nama, pembuat, operasi in kandidat:

        pengukuran = ukur_operasi(
            pembuat,
            operasi,
            pengulangan
        )

        data_hasil = {
            "jumlah_produk": jumlah,
            "operasi": nama_operasi,
            "struktur_data": nama,
            "id_diuji": id_diuji,
            "jumlah_sampel": JUMLAH_SAMPEL,
            "pengulangan_per_sampel": pengulangan,
            "rata_rata_us": round(pengukuran["rata_rata"], 6),
            "median_us": round(pengukuran["median"], 6),
            "minimum_us": round(pengukuran["minimum"], 6),
            "maksimum_us": round(pengukuran["maksimum"], 6),
            "catatan": catatan
        }

        semua_hasil.append(data_hasil)

    tampilkan_hasil(semua_hasil)

    return semua_hasil



# benchmark 1 : pencarian produk
# array list dengan linked list
def benchmark_pencarian(jumlah, produk):

    # ID terakhir digunakan untuk menguji pencarian linear
    target_id = produk[-1].id_produk

    print("\n[ PENCARIAN PRODUK ]")

    kandidat = [
        (
            "Array-based List",
            lambda: buat_array_list(produk),
            lambda struktur: struktur.cari(target_id)
        ),
        (
            "Hash Table",
            lambda: buat_hash_table(produk),
            lambda struktur: struktur.cari(target_id)
        )
    ]

    return bandingkan(
        jumlah=jumlah,
        nama_operasi="Pencarian produk",
        id_diuji=target_id,
        kandidat=kandidat,
        pengulangan=PENGULANGAN_CARI,
        catatan=(
            "Mencari ID produk terakhir; "
            "setiap sampel menjalankan 100 pencarian."
        )
    )



# benchmark 2 : pendaftaran produk
# array list dengan linked list
def benchmark_penambahan(jumlah, produk):

    # Produk baru dengan ID yang belum tersedia
    produk_baru = Produk(
        id_produk=f"PRD{jumlah + 1:06d}",
        nama_produk="Produk Baru",
        harga=250000.0,
        stok=50,
        kategori="Aksesori"
    )

    print("\n[ PENDAFTARAN PRODUK ]")

    kandidat = [
        (
            "Array-based List",
            lambda: buat_array_list(produk),
            lambda struktur: struktur.tambah(produk_baru)
        ),
        (
            "Linked List",
            lambda: buat_linked_list(produk),
            lambda struktur: struktur.tambah(produk_baru)
        )
    ]

    return bandingkan(
        jumlah=jumlah,
        nama_operasi="Pendaftaran produk",
        id_diuji=produk_baru.id_produk,
        kandidat=kandidat,
        pengulangan=1,
        catatan=(
            "Mengukur penambahan produk baru "
            "termasuk pemeriksaan ID duplikat."
        )
    )



# benchmark 3 : penghapusan produk
# array list dengan hash table
def benchmark_penghapusan(jumlah, produk):

    # ID pertama digunakan agar List harus menggeser
    # seluruh elemen setelah proses penghapusan.
    target_id = produk[0].id_produk

    print("\n[ PENGHAPUSAN PRODUK ]")

    kandidat = [
        (
            "Array-based List",
            lambda: buat_array_list(produk),
            lambda struktur: struktur.hapus(target_id)
        ),
        (
            "Hash Table",
            lambda: buat_hash_table(produk),
            lambda struktur: struktur.hapus(target_id)
        )
    ]

    return bandingkan(
        jumlah=jumlah,
        nama_operasi="Penghapusan produk",
        id_diuji=target_id,
        kandidat=kandidat,
        pengulangan=1,
        catatan=(
            "Menghapus ID produk pertama; "
            "List harus menggeser elemen setelahnya."
        )
    )



# menyimpan hasil ke csv
def simpan_hasil(semua_hasil):

    FOLDER_HASIL.mkdir(
        parents=True,
        exist_ok=True
    )

    kolom = [
        "jumlah_produk",
        "operasi",
        "struktur_data",
        "id_diuji",
        "jumlah_sampel",
        "pengulangan_per_sampel",
        "rata_rata_us",
        "median_us",
        "minimum_us",
        "maksimum_us",
        "catatan"
    ]

    with open(
        FILE_HASIL,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=kolom
        )

        writer.writeheader()
        writer.writerows(semua_hasil)

    print("\nHasil benchmark berhasil disimpan:")
    print(FILE_HASIL)



# program utama benchmark
def main():

    print("=" * 65)
    print("      BENCHMARK STRUKTUR DATA INVENTARIS PRODUK")
    print("=" * 65)

    print("\nStruktur data yang dibandingkan:")
    print("- Array-based List")
    print("- Linked List")
    print("- Hash Table")

    print("\nUkuran dataset:")
    for jumlah in UKURAN_DATA:
        print(f"- {jumlah:,} produk")

    print(f"\nJumlah sampel: {JUMLAH_SAMPEL}")
    print(f"Pengulangan pencarian per sampel: {PENGULANGAN_CARI}")

    semua_hasil = []

    for jumlah in UKURAN_DATA:

        print("\n" + "=" * 65)
        print(f"MEMULAI PENGUJIAN {jumlah:,} PRODUK")
        print("=" * 65)

        # Dataset dibuat di luar proses pengukuran
        produk = buat_data_produk(jumlah)

        # Eksperimen No. 4: pencarian
        semua_hasil.extend(
            benchmark_pencarian(jumlah, produk)
        )

        # Eksperimen No. 5: pendaftaran
        semua_hasil.extend(
            benchmark_penambahan(jumlah, produk)
        )

        # Eksperimen No. 5: penghapusan
        semua_hasil.extend(
            benchmark_penghapusan(jumlah, produk)
        )

    # Simpan seluruh hasil pengukuran
    simpan_hasil(semua_hasil)

    print("\n" + "=" * 65)
    print("SELURUH BENCHMARK BERHASIL DIJALANKAN")
    print(f"Total baris pengukuran: {len(semua_hasil)}")
    print("=" * 65)


if __name__ == "__main__":
    main()
