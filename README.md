# Aplikasi Kasir Laundry ASEK 

Aplikasi internal manajemen kasir berbasis Command Line Interface (CLI) menggunakan **Python 3**. Program ini dirancang khusus untuk mempermudah pekerjaan **Kasir Laundry** dalam menangani seluruh alur operasional toko, mulai dari pendaftaran orderan, pemantauan proses di belakang layar, hingga pembukuan keuangan harian.

## Anggota Kelompok (Penulis)
1. **Khresna Mulia Putra**
2. **Steven Evan Winardi**
3. **Adrian El Mahalli**

## Alur Kerja Kasir di Aplikasi (Fitur Utama)

Aplikasi ini mencakup seluruh tugas harian kasir yang dibagi menjadi 4 menu utama:

1. **Menu 1: Penerimaan Laundry Baru (Input Data)**
   * Kasir menginput nama dan nomor HP pelanggan.
   * Kasir bisa memasukkan **lebih dari satu jenis layanan sekaligus** ke dalam satu nota (misal: pelanggan bawa cucian kiloan sekaligus nitip jas satuan).
   * Sistem otomatis menerbitkan ID Nota unik berurutan (`TRX-001`, `TRX-002`, dst.) dengan status awal `"Antrean"`.

2. **Menu 2: Cek / Ubah Status Cucian (Monitoring Kerja)**
   * Kasir menerima laporan perkembangan dari ruang produksi belakang, lalu memperbarui status nota di komputer menjadi `"Sedang Dicuci"` atau `"Siap Diambil"`.
   * Saat kasir mengubah status ke `"Siap Diambil"`, sistem otomatis menampilkan simulasi notifikasi SMS untuk pelanggan.

3. **Menu 3: Pengambilan & Pembayaran (Closing Order)**
   * Saat pelanggan datang membawa nota, kasir mengetikkan ID Transaksi.
   * **Sistem Pengaman Kasir**: Program akan menolak pembayaran jika status cucian masih `"Antrean"` atau `"Sedang Dicuci"`. Uang hanya bisa diinput jika baju sudah `"Siap Diambil"`.
   * Kasir memasukkan nominal pembayaran, dan sistem otomatis menghitung kembalian uang. Jika uang kurang, kasir diminta menginput ulang sampai nominalnya pas/lebih.

4. **Menu 4: Laporan Keuangan Toko (Rekap Data Kasir)**
   * Menu khusus untuk kasir melakukan *closing* toko atau saat pemilik laundry ingin melihat rekap.
   * Menampilkan tabel data lengkap seluruh pelanggan, status pengerjaan, total pendapatan bersih yang ada di laci kasir (hanya menghitung yang sudah `"Lunas"`), dan jumlah orderan yang sukses selesai.

## Keunggulan Sistem (Anti-Crash)
* **Validasi Input Berlapis**: Kasir tidak akan membuat program *error* atau keluar mendadak jika salah ketik angka menu, salah ketik huruf, atau salah ketik ID Transaksi (Typo). Program akan meminta input ulang secara aman.
* **Fitur Menyerah (`keluar`)**: Jika kasir lupa ID Transaksi pelanggan saat ingin mengubah status atau memproses pembayaran, kasir cukup mengetik `'keluar'` untuk kembali ke menu utama tanpa merusak data.

## Cara Menjalankan Aplikasi
Buka Terminal / Command Prompt pada folder tempat file `nyobain.py` berada, lalu jalankan perintah:
```bash
python nyobain.py