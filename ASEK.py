# File : ASEK.py
# Penulis :
#   Khresna Mulia Putra
#   Steven Evan Winardi
#   Adrian El Mahalli
# Tujuan : Membuat aplikasi untuk mempermudah layanan laundry ASEK

# Kamus Data Global:
#	database_laundry : dictionary of dictionary (Penyimpanan utama data transaksi laundry)
#	urutan           : integer (Penyetel nomor urut pembuatan ID Transaksi otomatis
database_laundry = {}
urutan = 1

# Input Order
def input_orderan():
    # Kamus Data Lokal:
    #	global urutan    : integer (Menggunakan variabel urutan dari scope global)
    #	menu_lagi        : string (Kontrol perulangan untuk tambah antrean nota baru)
    #	nama             : string (Nama dari pelanggan laundry)
    #	no_hp            : string (Nomor telepon pelanggan laundry)
    #	total_harga      : real/float (Akumulasi total tagihan dalam satu nota)
    #	tambah_layanan   : string (Kontrol perulangan untuk tambah layanan per pelanggan)
    #	pilihan_layanan  : integer (Menu pilihan kategori jenis layanan 1-4)
    #	berat            : real/float (Berat pakaian kotor kiloan dalam satuan Kg)
    #	pilihan_jenis    : integer (Menu pilihan jenis pakaian satuan 1-4)
    #	harga            : integer (Harga dasar per item pakaian satuan)
    #	banyakpcs        : integer (Jumlah kuantitas pakaian satuan yang dimasukkan)
    #	id_transaksi     : string (ID unik penanda transaksi, contoh: TRX-001)
    global urutan
    menu_lagi = "y"
    while menu_lagi == "y" or menu_lagi == "Y":
        print("\n========================================")
        print("     PENERIMAAN LAUNDRY BARU (INPUT)    ")
        print("========================================")
        nama = str(input("Masukkan Nama: "))
        no_hp = str(input("Masukkan Nomor Telepon: "))
        total_harga = 0
        tambah_layanan = "y"
        while tambah_layanan == "y" or tambah_layanan == "Y":
            print("\n--- PILIHAN LAYANAN ---")
            print("1. Cuci Kering Setrika/Rp.7000 (per Kg)")
            print("2. Cuci Kering Lipat/Rp.5000 (per Kg)")
            print("3. Setrika saja/Rp.4000 (per Kg)")
            print("4. Laundry Satuan")
            pilihan_layanan = 0
            while pilihan_layanan < 1 or pilihan_layanan > 4:
                pilihan_layanan = int(input("Layanan berapa (1-4): "))
                if pilihan_layanan < 1 or pilihan_layanan > 4:
                    print("Pilihan tidak valid! Masukkan angka 1 sampai 4.")
            if pilihan_layanan == 1:
                berat = float(input("Masukkan Berat (Kg): "))
                total_harga += (berat * 7000)
            if pilihan_layanan == 2:
                berat = float(input("Masukkan Berat (Kg): "))
                total_harga += (berat * 5000)
            if pilihan_layanan == 3:
                berat = float(input("Masukkan Berat (Kg): "))
                total_harga += (berat * 4000)
            if pilihan_layanan == 4:
                print("\nPilih jenis satuan:")
                print("1. Jas/Rp.25000")
                print("2. Gaun/Rp.35000")
                print("3. Selimut/Rp.20000")
                print("4. Tas/Rp.30000")
                pilihan_jenis = 0
                while pilihan_jenis < 1 or pilihan_jenis > 4:
                    pilihan_jenis = int(input("Jenis berapa (1-4): "))
                    if pilihan_jenis < 1 or pilihan_jenis > 4:
                        print("Pilihan jenis tidak valid! Masukkan angka 1 sampai 4.")
                harga = 0
                if pilihan_jenis == 1:
                    harga = 25000
                if pilihan_jenis == 2:
                    harga = 35000
                if pilihan_jenis == 3:
                    harga = 20000
                if pilihan_jenis == 4:
                    harga = 30000 
                banyakpcs = int(input("Berapa Banyak (Pcs): "))
                total_harga += (banyakpcs * harga)
            tambah_layanan = str(input("Mau tambah layanan lain untuk pelanggan ini? (y/n): "))
        id_transaksi = f"TRX-{000+urutan}"
        urutan += 1
        database_laundry[id_transaksi] = {
            "nama": nama,
            "no_hp": no_hp,
            "total_harga": total_harga,
            "status": "Antrean",
            "pembayaran": "Belum Bayar",
        }
        print("----------------------------------------")
        print(f"Sukses! Orderan disimpan dengan ID: {id_transaksi}")
        print(f"Total Gabungan Tagihan: Rp. {total_harga}")
        print("----------------------------------------")
        menu_lagi = str(input("Apakah ingin menginput orderan baru yang lain? (y/n): "))

# Mengubah Status
def monitoring_status():
    # Kamus Data Lokal:
    #	menu_lagi        : string (Kontrol perulangan untuk menu monitoring status)
    #	id_valid         : boolean (Flag penanda validasi keberadaan ID transaksi)
    #	cari_id          : string (ID transaksi target yang akan diubah statusnya)
    #	pilihan_status   : integer (Angka pilihan status pengerjaan baru 1-3)
    menu_lagi = "y"
    while menu_lagi == "y" or menu_lagi == "Y":
        print("\n========================================")
        print("    CEK / UBAH STATUS CUCIAN (MONITOR)  ")
        print("========================================")
        id_valid = False
        while id_valid == False:
            cari_id = str(input("Masukkan ID Transaksi (misal: TRX-001) atau ketik 'keluar': "))
            if cari_id == "keluar" or cari_id == "Keluar":
                return 
            if cari_id in database_laundry:
                id_valid = True
            if cari_id not in database_laundry:
                print("ID Transaksi tidak ditemukan! Coba periksa kembali typo kalian.")
        print(f"\nNama Pelanggan : {database_laundry[cari_id]['nama']}")
        print(f"Status Saat Ini: {database_laundry[cari_id]['status']}")
        print("----------------------------------------")
        print("Pilih Status Baru:")
        print("1. Antrean")
        print("2. Sedang Dicuci")
        print("3. Siap Diambil")
        pilihan_status = 0
        while pilihan_status < 1 or pilihan_status > 3:
            pilihan_status = int(input("Pilih (1-3): "))
            if pilihan_status < 1 or pilihan_status > 3:
                print("Pilihan status salah! Masukkan angka 1 sampai 3.")
        if pilihan_status == 1:
            database_laundry[cari_id]['status'] = "Antrean"
        if pilihan_status == 2:
            database_laundry[cari_id]['status'] = "Sedang Dicuci"
        if pilihan_status == 3:
            database_laundry[cari_id]['status'] = "Siap Diambil"
            print(f"[NOTIFIKASI] SMS dikirim ke {database_laundry[cari_id]['no_hp']}: Halo {database_laundry[cari_id]['nama']}, cucian Anda dengan ID {cari_id} sudah SIAP DIAMBIL!")
        print("Status berhasil diperbarui!")
        print("----------------------------------------")
        menu_lagi = str(input("Apakah ingin mengecek / mengubah status transaksi lain? (y/n): "))

# Proses Pembayaran
def pembayaran_laundry():
    # Kamus Data Lokal:
    #	menu_lagi         : string (Kontrol perulangan untuk transaksi pembayaran)
    #	id_valid          : boolean (Flag penanda validasi keberadaan ID transaksi)
    #	cari_id           : string (ID transaksi target pembayaran pelanggan)
    #	tagihan           : real/float (Besaran biaya yang wajib dibayarkan)
    #	pembayaran_sukses : boolean (Flag penghenti loop pengerjaan nominal bayar)
    #	bayar             : integer (Nominal nominal uang tunai dari konsumen)
    #	kembalian         : real/float (Sisa kelebihan uang pembayaran)
    menu_lagi = "y"
    while menu_lagi == "y" or menu_lagi == "Y":
        print("\n========================================")
        print("      PENGAMBILAN & PEMBAYARAN          ")
        print("========================================")
        id_valid = False
        while id_valid == False:
            cari_id = str(input("Masukkan ID Transaksi (misal: TRX-001) atau ketik 'keluar': "))
            if cari_id == "keluar" or cari_id == "Keluar":
                return   
            if cari_id in database_laundry:
                id_valid = True
            if cari_id not in database_laundry:
                print("ID Transaksi tidak ditemukan! Coba cek huruf kapital atau angkanya.")           
        if database_laundry[cari_id]['status'] == "Selesai/Diambil":
            print("Transaksi ini sudah selesai dikerjakan dan sudah diambil.")  
        if database_laundry[cari_id]['status'] == "Antrean" or database_laundry[cari_id]['status'] == "Sedang Dicuci":
            print(f"Maaf, cucian atas nama {database_laundry[cari_id]['nama']} MASIH DALAM PROSES ({database_laundry[cari_id]['status']}).")
            print("Pembayaran belum bisa dilakukan sampai status menjadi 'Siap Diambil'.")
        if database_laundry[cari_id]['status'] == "Siap Diambil":
            print(f"Nama Pelanggan : {database_laundry[cari_id]['nama']}")
            print(f"Status Cucian  : {database_laundry[cari_id]['status']}")
            print(f"Total Tagihan  : Rp. {database_laundry[cari_id]['total_harga']}")
            tagihan = database_laundry[cari_id]['total_harga']
            pembayaran_sukses = False
            while pembayaran_sukses == False:
                bayar = int(input("Masukkan Jumlah Uang Pembayaran: Rp. "))
                if bayar >= tagihan:
                    kembalian = bayar - tagihan
                    print(f"Kembalian: Rp. {kembalian}")
                    database_laundry[cari_id]['status'] = "Selesai/Diambil"
                    database_laundry[cari_id]['pembayaran'] = "Lunas"
                    print("Transaksi Sukses! Pakaian telah diserahkan.")
                    pembayaran_sukses = True
                if bayar < tagihan:
                    print(f"Maaf, uang yang dibayarkan kurang Rp. {tagihan - bayar}! Coba ulangi.")    
        print("----------------------------------------")
        menu_lagi = str(input("Apakah ingin memproses pembayaran nota lain? (y/n): "))

# Output Laporan
def laporan_keuangan():
    # Kamus Data Lokal:
    #	total_pendapatan : real/float (Akumulasi keuangan terkumpul dari nota Lunas)
    #	baju_sukses      : integer (Total frekuensi cucian berstatus Selesai/Diambil)
    #	id_trx           : string (Variabel iterasi / key pembongkar dictionary)
    #	nama_cust        : string (Menampung sementara nama pembacaan database)
    #	no_hp_cust       : string (Menampung sementara data nomor telepon)
    #	harga_cust       : real/float (Menampung nilai sementara tagihan)
    #	status_cuci      : string (Menampung nilai sementara pengerjaan pakaian)
    #	status_bayar     : string (Menampung status penyelesaian administrasi kasir)
    print("\n==========================================================================")
    print("                      LAPORAN DATA & KEUANGAN TOKO LAUNDRY                ")
    print("==========================================================================")
    
    total_pendapatan = 0
    baju_sukses = 0
    
    print(f"{'ID':<10} | {'Nama Pelanggan':<18} | {'No HP':<14} | {'Total Harga':<12} | {'Status Cuci':<15} | {'Bayar':<10}")
    print("-" * 90)
    for id_trx in database_laundry:
        nama_cust = database_laundry[id_trx]['nama']
        no_hp_cust = database_laundry[id_trx]['no_hp']
        harga_cust = database_laundry[id_trx]['total_harga']
        status_cuci = database_laundry[id_trx]['status']
        status_bayar = database_laundry[id_trx]['pembayaran']
        
        print(f"{id_trx:<10} | {nama_cust:<18} | {no_hp_cust:<14} | Rp.{harga_cust:<9} | {status_cuci:<15} | {status_bayar:<10}")
        
        if status_bayar == "Lunas":
            total_pendapatan += harga_cust
        if status_cuci == "Selesai/Diambil":
            baju_sukses += 1
    print("-" * 90)
    print(f"Jumlah Transaksi Sukses/Selesai Diambil : {baju_sukses} orderan")
    print(f"Total Uang Pendapatan di Laci Kasir     : Rp. {total_pendapatan}")
    print("==========================================================================")


# Menu Utama Program
def main():
    # Kamus Data Lokal:
    #	pilihan_menu : integer (Variabel navigasi memilih menu utama aplikasi 1-5)
    pilihan_menu = 0
    while pilihan_menu != 5:
        print("\n=== APLIKASI MANAGEMEN LAUNDRY ASEK ===")
        print("1. Penerimaan Laundry Baru (Input Data)")
        print("2. Cek / Ubah Status Cucian (Monitoring)")
        print("3. Pengambilan & Pembayaran (Transaksi Selesai)")
        print("4. Laporan Keuangan Toko (Rekap Data Lengkap)")
        print("5. Keluar Aplikasi")
        
        pilihan_menu = 0
        while pilihan_menu < 1 or pilihan_menu > 5:
            pilihan_menu = int(input("Masukkan pilihan menu (1-5): "))
            if pilihan_menu < 1 or pilihan_menu > 5:
                print("Pilihan menu salah! Gunakan angka 1 sampai 5.")
                
        print("----------------------------------------")

        if pilihan_menu == 1:
            input_orderan()
        if pilihan_menu == 2:
            monitoring_status()
        if pilihan_menu == 3:
            pembayaran_laundry()
        if pilihan_menu == 4:
            laporan_keuangan()

    print("Terima kasih telah menggunakan aplikasi laundry ASEK!")
    return 0

if __name__ == '__main__':  
    main()