
# Proyek 1A — Sistem Manajemen Inventaris Produk

Implementasi dan analisis perbandingan struktur data linear untuk sistem manajemen inventaris produk pada perusahaan e-commerce menggunakan Python.

## 1. Identitas Proyek

| Keterangan | Informasi |
|---|---|
| Nama | Dimas Andre Prasetya |
| Program Studi | Teknik Informatika |
| Mata Kuliah | Struktur Data |
| Proyek | Proyek 1A |
| Studi Kasus | Sistem Manajemen Inventaris Produk |

## 2. Deskripsi Proyek

Proyek ini membahas penerapan dan perbandingan beberapa struktur data dalam sistem manajemen inventaris produk.

Sistem dirancang untuk menangani tiga operasi utama:

1. **Pendaftaran produk** untuk menambahkan produk baru ke inventaris.
2. **Pencarian produk berdasarkan ID** untuk menemukan dan menampilkan informasi produk.
3. **Penghapusan produk berdasarkan ID** untuk menghapus produk yang sudah tidak tersedia atau ditarik dari peredaran.

Untuk menentukan struktur data yang paling sesuai, dilakukan perbandingan terhadap tiga kandidat, yaitu Array-based List, Custom Linked List, dan Hash Table.

## 3. Data Produk

Setiap produk memiliki atribut sebagai berikut:

| Atribut | Tipe Data | Keterangan |
|---|---|---|
| id_produk | String | Identitas unik produk |
| nama_produk | String | Nama produk |
| harga | Float | Harga produk |
| stok | Integer | Jumlah persediaan produk |
| kategori | String | Kategori produk |

Contoh data:

```python
produk = {
    "id_produk": "PRD001",
    "nama_produk": "Mouse Wireless",
    "harga": 150000.0,
    "stok": 25,
    "kategori": "Aksesori Komputer"
}
```

## 4. Struktur Data yang Dibandingkan

Proyek ini menggunakan tiga kandidat struktur data.

### A. Array-based List

Menggunakan Python `list` untuk menyimpan kumpulan objek produk secara berurutan.

Karakteristik:
- Data disimpan dalam urutan indeks.
- Penambahan di akhir list memiliki kompleksitas O(1) secara amortisasi.
- Pencarian berdasarkan ID membutuhkan pemeriksaan data secara berurutan.
- Penghapusan berdasarkan ID dapat memerlukan pergeseran elemen.

### B. Custom Linked List

Menggunakan implementasi Linked List sendiri dengan komponen Node, Head, dan Tail.

Karakteristik:
- Setiap node menyimpan data produk dan referensi ke node berikutnya.
- Penambahan node di bagian akhir dapat dilakukan dalam O(1) dengan pointer Tail.
- Pencarian berdasarkan ID membutuhkan penelusuran node.
- Penghapusan dilakukan dengan mengubah hubungan antar-node.

### C. Hash Table

Menggunakan Python Dictionary (`dict`) dengan ID produk sebagai key dan objek Produk sebagai value.

Karakteristik:
- Produk dapat diakses berdasarkan ID.
- Pencarian berdasarkan key memiliki kompleksitas rata-rata O(1).
- Penambahan dan penghapusan berdasarkan key juga memiliki kompleksitas rata-rata O(1).
- Dalam kondisi terburuk, operasi dapat mencapai O(n).

## 5. Struktur Folder Proyek

```text
Proyek 1A/
│
├── hasil/
│   └── hasil_benchmark.csv
│
├── struktur/
│   ├── __init__.py
│   ├── array_list.py
│   ├── hash_table.py
│   └── linked_list.py
│
├── benchmark.py
├── main.py
├── product.py
└── README.md
```

### Penjelasan File

| File | Fungsi |
|---|---|
| product.py | Mendefinisikan model dan atribut produk |
| struktur/array_list.py | Implementasi Array-based List |
| struktur/linked_list.py | Implementasi Custom Linked List |
| struktur/hash_table.py | Implementasi Hash Table |
| struktur/__init__.py | Mengatur package struktur data |
| benchmark.py | Mengukur dan membandingkan performa struktur data |
| main.py | Program utama inventaris produk |
| hasil/hasil_benchmark.csv | Menyimpan hasil pengukuran benchmark |
| README.md | Dokumentasi proyek |

## 6. Implementasi Program

Pada program utama, Hash Table digunakan sebagai struktur data utama untuk mengelola inventaris produk.

Operasi yang tersedia:

| Menu | Operasi | Fungsi |
|---|---|---|
| 1 | Tambah Produk | Mendaftarkan produk baru |
| 2 | Cari Produk | Mencari produk berdasarkan ID |
| 3 | Hapus Produk | Menghapus produk berdasarkan ID |
| 4 | Tampilkan Produk | Menampilkan seluruh produk |
| 5 | Keluar | Mengakhiri program |

Hash Table dipilih sebagai struktur data utama karena sistem memerlukan pencarian dan penghapusan produk berdasarkan ID secara efisien.

Sementara itu, Array-based List dan Custom Linked List tetap diimplementasikan sebagai kandidat pembanding dalam eksperimen.

## 7. Metodologi Benchmark

Benchmark dilakukan untuk membandingkan waktu eksekusi operasi pada struktur data yang berbeda.

### Ukuran Dataset

Pengujian dilakukan dengan tiga ukuran dataset:

- 1.000 produk
- 10.000 produk
- 100.000 produk

### Operasi yang Diuji

| No. | Operasi | Perbandingan |
|---|---|---|
| 1 | Pencarian produk berdasarkan ID | Array-based List vs Hash Table |
| 2 | Pendaftaran produk baru | Array-based List vs Linked List |
| 3 | Penghapusan produk berdasarkan ID | Array-based List vs Hash Table |

### Metode Pengukuran

- Menggunakan fungsi `time.perf_counter_ns()` untuk mengukur waktu eksekusi.
- Setiap pengujian dilakukan sebanyak 7 sampel.
- Pencarian dilakukan sebanyak 100 kali dalam setiap sampel.
- Dataset disiapkan sebelum waktu operasi diukur.
- Hasil pengukuran mencatat rata-rata, median, minimum, dan maksimum.
- Median digunakan sebagai nilai utama dalam analisis perbandingan.

Pengukuran pendaftaran produk mencakup pemeriksaan ID duplikat sebelum data ditambahkan. Dengan demikian, waktu yang dicatat merupakan waktu keseluruhan method `tambah()` pada masing-masing struktur data.

## 8. Hasil Benchmark

Berdasarkan pengujian yang dilakukan, diperoleh hasil median waktu eksekusi sebagai berikut.

Satuan waktu yang digunakan adalah mikrodetik (µs).

### A. Pencarian Produk Berdasarkan ID

| Jumlah Produk | Array-based List | Hash Table |
|---:|---:|---:|
| 1.000 | 30,612 | 0,110 |
| 10.000 | 306,061 | 0,111 |
| 100.000 | 4.090,033 | 0,252 |

Hash Table menunjukkan waktu pencarian yang jauh lebih rendah dibandingkan Array-based List, terutama ketika jumlah produk semakin besar.

### B. Pendaftaran Produk Baru

| Jumlah Produk | Array-based List | Linked List |
|---:|---:|---:|
| 1.000 | 35,200 | 45,900 |
| 10.000 | 295,600 | 434,400 |
| 100.000 | 3.527,800 | 4.871,200 |

Array-based List menunjukkan waktu pendaftaran yang lebih rendah pada pengujian ini. Hal tersebut dipengaruhi oleh proses pemeriksaan ID duplikat yang harus dilakukan sebelum produk dimasukkan.

### C. Penghapusan Produk Berdasarkan ID

| Jumlah Produk | Array-based List | Hash Table |
|---:|---:|---:|
| 1.000 | 0,800 | 0,700 |
| 10.000 | 6,100 | 4,200 |
| 100.000 | 53,200 | 14,900 |

Hash Table menunjukkan waktu penghapusan yang lebih rendah dibandingkan Array-based List. Perbedaannya semakin terlihat ketika jumlah produk meningkat.

**Catatan:** Hasil benchmark merupakan pengukuran pada perangkat dan kondisi pengujian yang digunakan. Waktu aktual dapat berbeda pada perangkat lain.

## 9. Analisis Kompleksitas Waktu

Berikut perbandingan kompleksitas keseluruhan operasi berdasarkan implementasi program.

| Operasi | Array-based List | Linked List | Hash Table |
|---|---|---|---|
| Pendaftaran produk | O(n) | O(n) | O(1) rata-rata |
| Pencarian berdasarkan ID | O(n) | O(n) | O(1) rata-rata |
| Penghapusan berdasarkan ID | O(n) | O(n) | O(1) rata-rata |

Pada Array-based List dan Linked List, proses pemeriksaan ID unik menyebabkan operasi pendaftaran memiliki kompleksitas O(n).

Hash Table dapat melakukan pemeriksaan key, pencarian, dan penghapusan dengan kompleksitas rata-rata O(1).

## 10. Struktur Data yang Dipilih

Berdasarkan karakteristik sistem, analisis kompleksitas, dan hasil pengukuran, Hash Table dipilih sebagai struktur data utama dalam program inventaris produk.

Pertimbangannya:

1. ID produk dapat digunakan sebagai key untuk mengidentifikasi setiap produk secara unik.
2. Pencarian produk berdasarkan ID lebih efisien dibandingkan penelusuran linear.
3. Penghapusan produk berdasarkan ID dapat dilakukan dengan kompleksitas rata-rata O(1).
4. Struktur key-value sesuai dengan kebutuhan pengelolaan inventaris berdasarkan identitas produk.

Meskipun Array-based List menunjukkan performa lebih baik pada pengujian pendaftaran dibandingkan Linked List, Hash Table lebih sesuai untuk kebutuhan pencarian dan penghapusan berdasarkan ID dalam studi kasus ini.

## 11. Cara Menjalankan Program

Pastikan Python sudah terpasang.

Buka terminal pada folder utama proyek.

### Menjalankan program inventaris

```bash
python main.py
```

### Menjalankan benchmark

```bash
python benchmark.py
```

Hasil benchmark akan disimpan secara otomatis ke:

```text
hasil/hasil_benchmark.csv
```

## 12. Teknologi yang Digunakan

- Python 3
- Python List
- Custom Linked List
- Python Dictionary
- `dataclasses`
- `time`
- `csv`
- `statistics`
- GitHub

Tidak diperlukan library eksternal untuk menjalankan proyek ini.

## 13. Keterbatasan Program

Program menggunakan penyimpanan data di memori (RAM). Oleh karena itu, produk yang dimasukkan akan hilang ketika program ditutup.

Benchmark juga merupakan pengukuran eksperimental yang dipengaruhi oleh spesifikasi perangkat, kondisi sistem, dan implementasi program.

## 14. Tujuan Proyek

Proyek ini dibuat untuk memahami bagaimana pemilihan struktur data memengaruhi efisiensi operasi dalam suatu sistem.

Melalui implementasi dan pengujian Array-based List, Custom Linked List, dan Hash Table, diharapkan dapat terlihat perbedaan karakteristik, kompleksitas, dan performa masing-masing struktur data dalam pengelolaan inventaris produk.
