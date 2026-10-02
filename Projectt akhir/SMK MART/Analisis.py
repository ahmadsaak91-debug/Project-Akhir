import json
import os
from datetime import datetime



FILE_PENGGUNA = "pengguna.json"
FILE_BARANG = "barang.json"
FILE_TRANSAKSI = "transaksi.json"
FILE_GUDANG = "gudang.json"




def baca_data(nama_file):
    if not os.path.exists(nama_file):
        return []

    try:
        with open(nama_file, "r") as file:
            return json.load(file)
    except:
        return []


def simpan_data(nama_file, data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)




pengguna = baca_data(FILE_PENGGUNA)
barang = baca_data(FILE_BARANG)
transaksi = baca_data(FILE_TRANSAKSI)
gudang = baca_data(FILE_GUDANG)



def kelola_pengguna():

    while True:

        print("\n========================================")
        print("       DATA PENGGUNA SMK MART")
        print("========================================")
        print("1. Lihat Data Pengguna")
        print("2. Tambah Pengguna")
        print("3. Ubah Pengguna")
        print("4. Hapus Pengguna")
        print("5. Kembali")

        pilihan = input("Pilih menu : ")

      

        if pilihan == "1":

            print("\n----------- DATA PENGGUNA -----------")

            if len(pengguna) == 0:
                print("Belum ada data pengguna.")
            else:

                for i, user in enumerate(pengguna, 1):

                    print(
                        f"{i}. Nama   : {user['nama']}"
                    )
                    print(
                        f"   Kelas  : {user['kelas']}"
                    )
                    print(
                        f"   Status : {user['status']}"
                    )
                    print("------------------------------------")

       

        elif pilihan == "2":

            nama = input("Nama : ")
            kelas = input("Kelas : ")
            status = input(
                "Status (Guru/Staff/Karyawan/Siswa) : "
            )

            pengguna.append({
                "nama": nama,
                "kelas": kelas,
                "status": status
            })

            simpan_data(FILE_PENGGUNA, pengguna)

            print("Data pengguna berhasil ditambahkan.")

       
        elif pilihan == "3":

            nama_lama = input(
                "Masukkan nama pengguna yang akan diubah : "
            )

            ditemukan = False

            for user in pengguna:

                if user["nama"].lower() == nama_lama.lower():

                    user["nama"] = input("Nama baru : ")
                    user["kelas"] = input("Kelas baru : ")
                    user["status"] = input("Status baru : ")

                    ditemukan = True
                    break

            if ditemukan:

                simpan_data(FILE_PENGGUNA, pengguna)
                print("Data pengguna berhasil diubah.")

            else:

                print("Pengguna tidak ditemukan.")

     

        elif pilihan == "4":

            nama = input(
                "Nama pengguna yang akan dihapus : "
            )

            ditemukan = False

            for user in pengguna:

                if user["nama"].lower() == nama.lower():

                    pengguna.remove(user)
                    ditemukan = True
                    break

            if ditemukan:

                simpan_data(FILE_PENGGUNA, pengguna)
                print("Pengguna berhasil dihapus.")

            else:

                print("Pengguna tidak ditemukan.")

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak tersedia.")




def kelola_barang():

    while True:

        print("\n========================================")
        print("          DATA BARANG SMK MART")
        print("========================================")
        print("1. Lihat Barang")
        print("2. Tambah Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Kembali")

        pilihan = input("Pilih menu : ")

    

        if pilihan == "1":

            tampilkan_barang()

      
        elif pilihan == "2":

            kode = input("Kode Barang : ")
            nama = input("Nama Barang : ")
            harga = int(input("Harga Barang : "))
            stok = int(input("Stok Barang : "))
            minimum = int(input("Stok Minimum : "))
            kategori = input("Kategori Barang : ")
            satuan = input("Satuan Barang : ")

            barang.append({
                "kode": kode,
                "nama": nama,
                "harga": harga,
                "stok": stok,
                "minimum": minimum,
                "kategori": kategori,
                "satuan": satuan
            })

            simpan_data(FILE_BARANG, barang)

            print("Data barang berhasil ditambahkan.")

   

        elif pilihan == "3":

            kode = input(
                "Kode barang yang akan diubah : "
            )

            ditemukan = False

            for item in barang:

                if item["kode"] == kode:

                    item["nama"] = input(
                        "Nama Barang : "
                    )

                    item["harga"] = int(
                        input("Harga Barang : ")
                    )

                    item["minimum"] = int(
                        input("Stok Minimum : ")
                    )

                    item["kategori"] = input(
                        "Kategori Barang : "
                    )

                    item["satuan"] = input(
                        "Satuan Barang : "
                    )

                    ditemukan = True
                    break

            if ditemukan:

                simpan_data(FILE_BARANG, barang)
                print("Data barang berhasil diubah.")

            else:

                print("Barang tidak ditemukan.")

  
        elif pilihan == "4":

            kode = input(
                "Kode barang yang akan dihapus : "
            )

            ditemukan = False

            for item in barang:

                if item["kode"] == kode:

                    barang.remove(item)
                    ditemukan = True
                    break

            if ditemukan:

                simpan_data(FILE_BARANG, barang)
                print("Barang berhasil dihapus.")

            else:

                print("Barang tidak ditemukan.")

        elif pilihan == "5":

            break

        else:

            print("Pilihan tidak tersedia.")




def tampilkan_barang():

    print("\n================ DATA BARANG ================")

    if len(barang) == 0:

        print("Belum ada data barang.")
        return

    print(
        f"{'Kode':<10}"
        f"{'Nama':<20}"
        f"{'Harga':<12}"
        f"{'Stok':<8}"
        f"{'Min':<8}"
        f"{'Kategori':<15}"
        f"{'Satuan':<10}"
    )

    print("-" * 83)

    for item in barang:

        print(
            f"{item['kode']:<10}"
            f"{item['nama']:<20}"
            f"{item['harga']:<12}"
            f"{item['stok']:<8}"
            f"{item['minimum']:<8}"
            f"{item['kategori']:<15}"
            f"{item['satuan']:<10}"
        )




def barang_masuk():

    tampilkan_barang()

    kode = input(
        "\nMasukkan kode barang : "
    )

    ditemukan = False

    for item in barang:

        if item["kode"] == kode:

            jumlah = int(
                input("Banyak barang masuk : ")
            )

            asal = input("Asal barang : ")

            keterangan = input(
                "Keterangan barang : "
            )

            stok_sebelum = item["stok"]

            item["stok"] += jumlah

            stok_sesudah = item["stok"]

            gudang.append({

                "tanggal":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "kode": item["kode"],

                "nama": item["nama"],

                "jenis": "Barang Masuk",

                "jumlah": jumlah,

                "keterangan":
                    keterangan +
                    " | Asal: " +
                    asal,

                "stok_sebelum":
                    stok_sebelum,

                "stok_sesudah":
                    stok_sesudah
            })

            simpan_data(FILE_BARANG, barang)
            simpan_data(FILE_GUDANG, gudang)

            print("\nBarang masuk berhasil dicatat.")

            ditemukan = True
            break

    if not ditemukan:

        print("Barang tidak ditemukan.")




def barang_keluar():

    tampilkan_barang()

    kode = input(
        "\nMasukkan kode barang : "
    )

    ditemukan = False

    for item in barang:

        if item["kode"] == kode:

            jumlah = int(
                input("Banyak barang keluar : ")
            )

            if jumlah > item["stok"]:

                print(
                    "Stok tidak mencukupi!"
                )

                return

            keterangan = input(
                "Keterangan barang : "
            )

            stok_sebelum = item["stok"]

            item["stok"] -= jumlah

            stok_sesudah = item["stok"]

            gudang.append({

                "tanggal":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),

                "kode": item["kode"],

                "nama": item["nama"],

                "jenis": "Barang Keluar",

                "jumlah": jumlah,

                "keterangan":
                    keterangan,

                "stok_sebelum":
                    stok_sebelum,

                "stok_sesudah":
                    stok_sesudah
            })

            simpan_data(FILE_BARANG, barang)
            simpan_data(FILE_GUDANG, gudang)

            print(
                "\nBarang keluar berhasil dicatat."
            )

            ditemukan = True
            break

    if not ditemukan:

        print("Barang tidak ditemukan.")




def kelola_stok():

    print("\n================ DATA STOK ================")

    if len(barang) == 0:

        print("Belum ada data barang.")
        return

    for item in barang:

        print(
            f"Kode         : {item['kode']}"
        )

        print(
            f"Nama         : {item['nama']}"
        )

        print(
            f"Kategori     : {item['kategori']}"
        )

        print(
            f"Stok Saat Ini: {item['stok']} "
            f"{item['satuan']}"
        )

        print(
            f"Stok Minimum : {item['minimum']} "
            f"{item['satuan']}"
        )

        print("----------------------------------------")




def cek_stok_minimum():

    print(
        "\n========== PERINGATAN STOK MINIMUM =========="
    )

    ditemukan = False

    for item in barang:

        if item["stok"] <= item["minimum"]:

            print(
                "⚠ PERINGATAN STOK MINIMUM"
            )

            print(
                f"Kode        : {item['kode']}"
            )

            print(
                f"Nama        : {item['nama']}"
            )

            print(
                f"Stok saat ini : {item['stok']}"
            )

            print(
                f"Batas minimum: {item['minimum']}"
            )

            print("--------------------------------------")

            ditemukan = True

    if not ditemukan:

        print(
            "Semua stok barang masih di atas "
            "batas minimum."
        )




def transaksi_penjualan():

    keranjang = []

    print(
        "\n========== TRANSAKSI PENJUALAN =========="
    )



    nama_pembeli = input(
        "Nama pengguna/pembeli : "
    )

    while True:

        kode = input(
            "\nKode barang "
            "(ketik 'selesai' untuk selesai): "
        )

        if kode.lower() == "selesai":

            break

        barang_ditemukan = None

        for item in barang:

            if item["kode"] == kode:

                barang_ditemukan = item
                break

        if barang_ditemukan is None:

            print(
                "Barang tidak ditemukan."
            )

            continue

        print(
            "Nama Barang :",
            barang_ditemukan["nama"]
        )

        print(
            "Harga       :",
            barang_ditemukan["harga"]
        )

        print(
            "Stok        :",
            barang_ditemukan["stok"]
        )

        jumlah = int(
            input("Jumlah Barang : ")
        )

        if jumlah <= 0:

            print(
                "Jumlah barang harus lebih dari 0."
            )

            continue

        if jumlah > barang_ditemukan["stok"]:

            print(
                "Stok barang tidak mencukupi!"
            )

            continue

        subtotal = (
            barang_ditemukan["harga"]
            * jumlah
        )

        keranjang.append({

            "kode": barang_ditemukan["kode"],

            "nama": barang_ditemukan["nama"],

            "jumlah": jumlah,

            "harga":
                barang_ditemukan["harga"],

            "subtotal": subtotal
        })

        print(
            "Barang berhasil ditambahkan."
        )

 
    if len(keranjang) == 0:

        print(
            "Tidak ada barang yang dibeli."
        )

        return


    total = 0

    print(
        "\n=============== STRUK ==============="
    )

    for item in keranjang:

        print(
            f"{item['nama']} x "
            f"{item['jumlah']} = "
            f"Rp{item['subtotal']:,}"
        )

        total += item["subtotal"]

    print("--------------------------------------")

    print(
        f"Total Harga : Rp{total:,}"
    )



    while True:

        bayar = int(
            input("Bayar : Rp")
        )

        if bayar >= total:

            break

        print(
            "Uang pembayaran kurang!"
        )

    kembalian = bayar - total

    print(
        f"Kembalian : Rp{kembalian:,}"
    )



    nomor_transaksi = (
        "TRX" +
        datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )
    )

    tanggal = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    for pembelian in keranjang:

        for item in barang:

            if (
                item["kode"]
                == pembelian["kode"]
            ):

                stok_sebelum = item["stok"]

                item["stok"] -= (
                    pembelian["jumlah"]
                )

                stok_sesudah = item["stok"]

                # Catat aktivitas gudang
                gudang.append({

                    "tanggal": tanggal,

                    "kode": item["kode"],

                    "nama": item["nama"],

                    "jenis":
                        "Barang Keluar",

                    "jumlah":
                        pembelian["jumlah"],

                    "keterangan":
                        "Barang keluar karena penjualan",

                    "stok_sebelum":
                        stok_sebelum,

                    "stok_sesudah":
                        stok_sesudah
                })

  

    data_transaksi = {

        "nomor_transaksi":
            nomor_transaksi,

        "tanggal":
            tanggal,

        "kasir":
            nama_pembeli,

        "items":
            keranjang,

        "total_transaksi":
            total,

        "bayar":
            bayar,

        "kembalian":
            kembalian
    }

    transaksi.append(
        data_transaksi
    )

    simpan_data(
        FILE_BARANG,
        barang
    )

    simpan_data(
        FILE_TRANSAKSI,
        transaksi
    )

    simpan_data(
        FILE_GUDANG,
        gudang
    )

    print(
        "\nTransaksi berhasil disimpan!"
    )




def laporan_penjualan():

    print(
        "\n================ LAPORAN PENJUALAN ================"
    )

    if len(transaksi) == 0:

        print(
            "Belum ada transaksi."
        )

        return

    total_semua = 0

    for trx in transaksi:

        print(
            f"\nNomor Transaksi : "
            f"{trx['nomor_transaksi']}"
        )

        print(
            f"Tanggal         : "
            f"{trx['tanggal']}"
        )

        print(
            f"Kasir/Pengguna  : "
            f"{trx['kasir']}"
        )

        print(
            "------------------------------------------------"
        )

        for item in trx["items"]:

            print(
                f"Kode Barang : {item['kode']}"
            )

            print(
                f"Nama Barang : {item['nama']}"
            )

            print(
                f"Jumlah      : {item['jumlah']}"
            )

            print(
                f"Harga       : Rp{item['harga']:,}"
            )

            print(
                f"Subtotal    : Rp{item['subtotal']:,}"
            )

            print(
                "------------------------------------------------"
            )

        print(
            f"Total Transaksi : "
            f"Rp{trx['total_transaksi']:,}"
        )

        total_semua += trx[
            "total_transaksi"
        ]

    print(
        "\nTOTAL SELURUH PENJUALAN : "
        f"Rp{total_semua:,}"
    )




def laporan_stok():

    print(
        "\n================ LAPORAN STOK ================"
    )

    if len(barang) == 0:

        print(
            "Belum ada data barang."
        )

        return

    for item in barang:

        if item["stok"] <= item["minimum"]:

            status = "STOK MINIMUM"

        else:

            status = "AMAN"

        print(
            f"Kode     : {item['kode']}"
        )

        print(
            f"Nama     : {item['nama']}"
        )

        print(
            f"Kategori : {item['kategori']}"
        )

        print(
            f"Stok     : {item['stok']} "
            f"{item['satuan']}"
        )

        print(
            f"Minimum  : {item['minimum']} "
            f"{item['satuan']}"
        )

        print(
            f"Status   : {status}"
        )

        print(
            "-----------------------------------------"
        )




def laporan_gudang():

    print(
        "\n================ AKTIVITAS GUDANG ================"
    )

    if len(gudang) == 0:

        print(
            "Belum ada aktivitas gudang."
        )

        return

    for aktivitas in gudang:

        print(
            f"Tanggal        : "
            f"{aktivitas['tanggal']}"
        )

        print(
            f"Kode Barang    : "
            f"{aktivitas['kode']}"
        )

        print(
            f"Nama Barang    : "
            f"{aktivitas['nama']}"
        )

        print(
            f"Jenis Aktivitas: "
            f"{aktivitas['jenis']}"
        )

        print(
            f"Jumlah         : "
            f"{aktivitas['jumlah']}"
        )

        print(
            f"Keterangan     : "
            f"{aktivitas['keterangan']}"
        )

        print(
            f"Stok Sebelum   : "
            f"{aktivitas['stok_sebelum']}"
        )

        print(
            f"Stok Sesudah   : "
            f"{aktivitas['stok_sesudah']}"
        )

        print(
            "-----------------------------------------"
        )




def menu_utama():

    while True:

        print("\n")
        print("================================================")
        print("              S M K   M A R T")
        print("          SISTEM INFORMASI KASIR")
        print("================================================")

        print("1. Mengelola Data Pengguna")
        print("2. Melakukan Transaksi Penjualan")
        print("3. Mengelola Data Barang")
        print("4. Mengelola Administrasi Gudang")
        print("5. Mencatat Barang Masuk")
        print("6. Mencatat Barang Keluar")
        print("7. Mengelola Stok Barang")
        print("8. Peringatan Stok Minimum")
        print("9. Laporan Penjualan")
        print("10. Laporan Stok")
        print("11. Laporan Aktivitas Gudang")
        print("0. Keluar")
        print("================================================")

        pilihan = input(
            "Pilih menu : "
        )

        if pilihan == "1":

            kelola_pengguna()

        elif pilihan == "2":

            transaksi_penjualan()

        elif pilihan == "3":

            kelola_barang()

        elif pilihan == "4":

            # Administrasi gudang
            laporan_gudang()

        elif pilihan == "5":

            barang_masuk()

        elif pilihan == "6":

            barang_keluar()

        elif pilihan == "7":

            kelola_stok()

        elif pilihan == "8":

            cek_stok_minimum()

        elif pilihan == "9":

            laporan_penjualan()

        elif pilihan == "10":

            laporan_stok()

        elif pilihan == "11":

            laporan_gudang()

        elif pilihan == "0":

            print(
                "\nTerima kasih telah menggunakan "
                "SMK MART."
            )

            break

        else:

            print(
                "Menu tidak tersedia."
            )



menu_utama()