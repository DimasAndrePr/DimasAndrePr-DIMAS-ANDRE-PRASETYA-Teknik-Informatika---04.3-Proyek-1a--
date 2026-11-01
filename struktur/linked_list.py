from product import Produk

# NODE
class Node:
    def __init__(self, produk: Produk):
        self.produk = produk
        self.next = None



# CUSTOM LINKED LIST
class LinkedListProduk:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # INSERT: untuk tambahkan produk baru
    def tambah(self, produk: Produk):
        if not isinstance(produk, Produk):
            raise TypeError("Data harus berupa objek Produk.")

        # untuk memeriksa ID agar tidak duplikat
        if self.cari(produk.id_produk) is not None:
            raise ValueError(
                f"Produk dengan ID {produk.id_produk} sudah terdaftar."
            )

        node_baru = Node(produk)

        # Jika Linked List masih kosong
        if self.kosong():
            self.head = node_baru
            self.tail = node_baru

        else:
            # Menghubungkan node terakhir dengan node baru
            self.tail.next = node_baru
            self.tail = node_baru

        self.size += 1
        return True

    # SEARCH:untuk cari produk berdasarkan ID
    def cari(self, id_produk: str):
        current = self.head

        while current is not None:
            if current.produk.id_produk == id_produk:
                return current.produk

            current = current.next

        return None

    # DELETE:untuk hapus produk berdasarkan ID
    def hapus(self, id_produk: str):
        current = self.head
        previous = None

        while current is not None:

            if current.produk.id_produk == id_produk:

                # Jika node yang dihapus adalah Head
                if previous is None:
                    self.head = current.next

                else:
                    previous.next = current.next

                # Jika node yang dihapus adalah Tail
                if current is self.tail:
                    self.tail = previous

                self.size -= 1

                # Jika Linked List menjadi kosong
                if self.head is None:
                    self.tail = None

                return current.produk

            previous = current
            current = current.next

        return None

    # untuk ambil seluruh data produk
    def semua(self):
        hasil = []
        current = self.head

        while current is not None:
            hasil.append(current.produk)
            current = current.next

        return hasil

    # untuk hitung jumlah produk
    def __len__(self):
        return self.size

    #untuk periksa apakah Linked List kosong
    def kosong(self):
        return self.head is None