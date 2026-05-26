# File : nyobain.py 
# Penulis :
# Khresna Mulia Putra
# Steven Evan Winardi
# Adrian El Mahalli
# Program pengatur layanan laundry ASEK
# Kamus Data


masukan = 0

def input():
    total=0
    harga=0
    nama=str(input("Masukkan Nama: "))
    no_hp=int(input("Masukkan Nomor Telepon: "))
    berat=float(input("Masukan Berat: "))
    
    print("Pilihan Layanan") 
    print("1. Cuci Kering Setrika/Rp.7000")
    print("2. Cuci Kering Lipat/Rp.5000")
    print("3. Setrika saja/Rp.4000")
    print("4. Laundry Satuan")
    pilihan_layanan=str(input("Layanan berapa: "))
    if pilihan_layanan==4:
        print("Pilih jenis ")
        print("1. jas/Rp.25000")
        print("2. Gaun/Rp.35000")
        print("3. Selimut/Rp.20000")
        print("4. tas/Rp.30000")
        pilihan_jenis=int(input("Jenis berapa: "))
        if pilihan_jenis==1:
            harga=25000
        if pilihan_jenis==2:
            harga=35000
        if pilihan_jenis==3:
            harga=20000
        if pilihan_jenis==4:
            harga=30000
        banyakpcs=int(input("berapa Banyak"))
        total=banyakpcs*harga
        
        
    

def main():
    pilihan_menu=0
    while pilihan_menu != 5:
        print("1. Penerimaan Laundry Baru (Input Data)")
        print("2. Cek / Ubah Status Cucian (Monitoring)")
        print("3. Pengambilan & Pembayaran (Transaksi Selesai)")
        print("4. Laporan Keuangan Toko (Rekap Data)")
        print("5. Keluar Aplikasi")
        pilihan_menu = int(input("Masukkan pilihan menu (1-5): "))
        if pilihan_menu==1:
            input()


    return 0

if __name__ == '__main__':    
    main()