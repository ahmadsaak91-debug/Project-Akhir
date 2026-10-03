import os
from datetime import datetime

FILE_PENGGUNA = "pengguna.txt"
FILE_BARANG = "barang.txt"
FILE_TRANSAKSI = "transaksi.txt"
FILE_GUDANG = "gudang.txt"

import os

FILE_BARANG = "barang.txt"


def baca_file(nama_file):
    if not os.path.exists(nama_file):
        return []

    with open(nama_file, "r") as file:
        return [baris.strip() for baris in file if baris.strip()]


def tambah_ke_file(nama_file, data):
    with open(nama_file, "a") as file:
        file.write(data + "\n")


def ubah_file(nama_file, data):
    with open(nama_file, "w") as file:
        for baris in data:
            file.write(baris + "\n")


def cari_barang(kode):
    data_barang = baca_file(FILE_BARANG)

    for i, baris in enumerate(data_barang):
        data = baris.split("|")

        if data[0].lower() == kode.lower():
            return i, data

    return -1, None


def tampilkan_barang():
    data_barang = baca_file(FILE_BARANG)

    print("\n========== DATA BARANG ==========")

    if not data_barang:
        print("Data barang belum ada.")
        return

    print(f"{'Kode':<10}{'Nama':<20}{'Harga':<15}{'Stok':<10}")
    print("-" * 55)

    for baris in data_barang:
        data = baris.split("|")

        kode = data[0]
        nama = data[1]
        harga = int(data[2])
        stok = int(data[3])

        print(f"{kode:<10}{nama:<20}Rp{harga:<12}{stok:<10}")


def tambah_barang():
    print("\n========== TAMBAH BARANG ==========")

    kode = input("Masukkan kode barang : ")
    nama = input("Masukkan nama barang : ")

    try:
        harga = int(input("Harga       : "))
        stok = int(input("Stok awal   : "))
    except ValueError:
        print("Harga dan stok harus berupa angka!")
        return

    index, barang = cari_barang(kode)

    if barang is not None:
        print("Kode barang sudah digunakan!")
        return

    data = f"{kode}|{nama}|{harga}|{stok}"
    tambah_ke_file(FILE_BARANG, data)

    print("Barang berhasil ditambahkan.")


def hapus_barang():
    print("\n========== HAPUS BARANG ==========")

    kode = input("Masukkan kode barang: ")

    data_barang = baca_file(FILE_BARANG)
    index, barang = cari_barang(kode)

    if barang is None:
        print("Barang tidak ditemukan.")
        return

    del data_barang[index]

    ubah_file(FILE_BARANG, data_barang)

    print("Barang berhasil dihapus.")

# DATA PENGGUNA

def tambah_pengguna():
    print("\n========== TAMBAH PENGGUNA ==========")

    id_pengguna = input("ID pengguna : ")
    nama = input("Masukkan nama : ")
    jabatan = input("Jabatan     : ")

    data = f"{id_pengguna}|{nama}|{jabatan}"

    tambah_ke_file(FILE_PENGGUNA, data)

    print("Pengguna berhasil ditambahkan.")


def tampilkan_pengguna():
    data_pengguna = baca_file(FILE_PENGGUNA)

    print("\n========== DATA PENGGUNA ==========")

    if not data_pengguna:
        print("Belum ada data pengguna.")
        return

    print(f"{'ID':<10}{'Nama':<20}{'Jabatan':<10}")
    print("-" * 40)

    for baris in data_pengguna:
        data = baris.split("|")

        id_pengguna = data[0]
        nama = data[1]
        jabatan = data[2]

        print(f"{id_pengguna:<10}{nama:<20}{jabatan:<10}")


def menu_pengguna():
    while True:
        print("\n========== MENU PENGGUNA ==========")
        print("1. Tambah Pengguna")
        print("2. Tampilkan Pengguna")
        print("0. Kembali")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            tambah_pengguna()

        elif pilihan == "2":
            tampilkan_pengguna()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

      def transaksi_penjualan():
    print("\n========== TRANSAKSI PENJUALAN ==========")

    id_pengguna = input("ID pengguna : ")
    kode = input("Kode barang : ")

    data_barang = baca_file(FILE_BARANG)

    index, barang = cari_barang(kode)

    if barang is None:
        print("Barang tidak ditemukan!")
        return

    nama = barang[1]
    harga = int(barang[2])
    stok = int(barang[3])

    print(f"Nama  : {nama}")
    print(f"Harga : Rp{harga}")
    print(f"Stok  : {stok}")

    try:
        jumlah = int(input("Jumlah beli : "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0!")
        return

    if jumlah > stok:
        print("Stok tidak mencukupi!")
        return

    total = harga * jumlah

    print("\n========== TOTAL PEMBAYARAN ==========")
    print(f"Barang       : {nama}")
    print(f"Harga        : Rp{harga}")
    print(f"Jumlah       : {jumlah}")
    print(f"Total        : Rp{total}")

    try:
        bayar = int(input("Uang bayar   : Rp"))
    except ValueError:
        print("Uang bayar harus berupa angka!")
        return

    if bayar < total:
        print("Uang bayar kurang!")
        return

    kembalian = bayar - total


    stok_baru = stok - jumlah

    data_barang[index] = (
        f"{barang[0]}|{barang[1]}|{barang[2]}|{stok_baru}"
    )

    ubah_file(FILE_BARANG, data_barang)


    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data_transaksi = (
        f"{tanggal}|{id_pengguna}|{kode}|{nama}|{jumlah}|{total}"
    )

    tambah_ke_file(FILE_TRANSAKSI, data_transaksi)

    data_gudang = (
        f"{tanggal}|{id_pengguna}|{kode}|{nama}|{jumlah}"
    )

    tambah_ke_file(FILE_GUDANG, data_gudang)

    print(f"Transaksi berhasil.")
    print(f"Uang kembalian: Rp{kembalian}")

    if stok_baru <= 5:
        print("PERINGATAN: Stok barang sudah mencapai batas minimum!")

def barang_masuk():
    print("\n========== BARANG MASUK ==========")

    kode = input("Kode barang : ")

    data_barang = baca_file(FILE_BARANG)
    index, barang = cari_barang(kode)

    if barang is None:
        print("Barang tidak ditemukan.")
        return

    try:
        jumlah = int(input("Jumlah masuk : "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        return

    stok_lama = int(barang[3])
    stok_baru = stok_lama + jumlah



    data_barang[index] = (
        f"{barang[0]}|{barang[1]}|{barang[2]}|{stok_baru}"
    )

    ubah_file(FILE_BARANG, data_barang)

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data_gudang = (
        f"{tanggal}|MASUK|{barang[0]}|{barang[1]}|{jumlah}"
    )

    tambah_ke_file(FILE_GUDANG, data_gudang)

    print("Barang masuk berhasil dicatat.")
    print(f"Stok sekarang: {stok_baru}")

def barang_keluar():
    print("\n========== BARANG KELUAR ==========")

    kode = input("Kode barang : ")

    data_barang = baca_file(FILE_BARANG)
    index, barang = cari_barang(kode)

    if barang is None:
        print("Barang tidak ditemukan.")
        return

    stok = int(barang[3])

    try:
        jumlah = int(input("Jumlah keluar : "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        return

    if jumlah > stok:
        print("Stok tidak mencukupi!")
        return

    stok_baru = stok - jumlah

    data_barang[index] = (
        f"{barang[0]}|{barang[1]}|{barang[2]}|{stok_baru}"
    )

    ubah_file(FILE_BARANG, data_barang)

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data_gudang = (
        f"{tanggal}|KELUAR|{barang[0]}|{barang[1]}|{jumlah}"
    )

    tambah_ke_file(FILE_GUDANG, data_gudang)

    print("Barang keluar berhasil dicatat.")
    print(f"Stok sekarang: {stok_baru}")

def cek_stok():
    print("\n========== CEK STOK ==========")

    data_barang = baca_file(FILE_BARANG)

    if not data_barang:
        print("Belum ada data barang.")
        return

    for baris in data_barang:
        data = baris.split("|")

        kode = data[0]
        nama = data[1]
        stok = int(data[3])

        print(f"{kode} | {nama} | Stok: {stok}")

def peringatan_stok():
    print("\n========== PERINGATAN STOCK ==========")

    data_barang = baca_file(FILE_BARANG)

    batas_minimum = 5
    ada_stok_minimum = False

    for baris in data_barang:
        data = baris.split("|")

        kode = data[0]
        nama = data[1]
        stok = int(data[3])

        if stok <= batas_minimum:
            print(
                f"PERINGATAN: {kode} - {nama} "
                f"tersisa {stok} barang."
            )

            ada_stok_minimum = True

    if not ada_stok_minimum:
        print("Tidak ada barang yang mencapai stok minimum.")

def laporan_penjualan():
  print("\n", "========== LAPORAN PENJUALAN ==========")

  data_transaksi = baca_file(FILE_TRANSAKSI)

  if not data_transaksi:
    print("Belum ada transaksi.")
    return

  total_semua = 0

  print(
        f"{'Tanggal':<20}"
        f"{'Kode':<10}"
        f"{'Barang':<20}"
        f"{'Jumlah':<10}"
        f"{'Total':<15}"
    )

  print("-" * 75)

  for baris in data_transaksi:
    data = baris.split("|")

    tanggal = data[0]
    # data[1] adalah id_pengguna
    kode = data[2]
    nama = data[3]
    jumlah = int(data[4])
    total = int(data[5])

    total_semua += total

    print(
            f"{tanggal:<20}"
            f"{kode:<10}"
            f"{nama:<20}"
            f"{jumlah:<10}"
            f"Rp{total:<12}"
        )
  print("-" * 75)
  print(f"Total seluruh penjualan: Rp{total_semua}")

def laporan_stok():
  print("\n========== LAPORAN STOK ==========")

  data_barang = baca_file(FILE_BARANG)

  if not data_barang:
    print("Belum ada data barang.")
    return

  print(f"{'Kode':<10}{'Nama':<20}{'Harga':<15}{'Stok':<10}")
  print("-" * 55)

  for baris in data_barang:
    data = baris.split("|")
    print(
            f"{data[0]:<10}"
            f"{data[1]:<20}"
            f"Rp{int(data[2]):<12}"
            f"{data[3]:<10}"
    )

def laporan_gudang():
    print("\n========== LAPORAN GUDANG ==========")

    data_gudang = baca_file(FILE_GUDANG)

    if not data_gudang:
        print("Belum ada aktivitas gudang.")
        return

    print(
        f"{'Tanggal':<20}"
        f"{'Jenis':<10}"
        f"{'Kode':<10}"
        f"{'Barang':<20}"
        f"{'Jumlah':<10}"
    )

    print("-" * 75)

    for baris in data_gudang:
        data = baris.split("|")

        print(
            f"{data[0]:<20}"
            f"{data[1]:<10}"
            f"{data[2]:<10}"
            f"{data[3]:<20}"
            f"{data[4]:<10}"
        )

def menu_barang():

    print("\n========== KELOLA BARANG ==========")
    print("1. Tampilkan barang")
    print("2. Tambah barang")
    print("3. Ubah barang")
    print("4. Hapus barang")
    print("0. Kembali")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        tampilkan_barang()

    elif pilihan == "2":
        tambah_barang()

    elif pilihan == "3":
        ubah_barang()

    elif pilihan == "4":
        hapus_barang()

    elif pilihan == "0":
        return

    else:
        print("Pilihan tidak tersedia!")

def menu_gudang():

    print("\n========== ADMINISTRASI GUDANG ==========")
    print("1. Laporan gudang")
    print("2. Barang masuk")
    print("3. Barang keluar")
    print("0. Kembali")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        laporan_gudang()
    elif pilihan == "2":
        barang_masuk()
    elif pilihan == "3":
        barang_keluar()
    elif pilihan == "0":
        return
    else:
        print("Pilihan tidak tersedia!")

def menu_laporan():
  while True:
    print("\n========== KELOLA LAPORAN ==========")
    print("1. Laporan Penjualan")
    print("2. Laporan Stok")
    print("3. Laporan Aktivitas Gudang")
    print("0. Kembali")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
      laporan_penjualan()

    elif pilihan == "2":
      laporan_stok()

    elif pilihan == "3":
      laporan_gudang()
    elif pilihan =="0":
      break
    else:
      print("Pilihan tidak tersedia")

def main():

    while True:

        print("\n")
        print("=" * 45)
        print("             SMK MART")
        print("=" * 45)
        print("1. Kelola Data Pengguna")
        print("2. Transaksi Penjualan")
        print("3. Kelola Data Barang")
        print("4. Administrasi Gudang")
        print("5. Cek Stok")
        print("6. Peringatan Stok Minimum")
        print("7. Laporan")
        print("0. Keluar")
        print("=" * 45)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_pengguna()

        elif pilihan == "2":
            transaksi_penjualan()

        elif pilihan == "3":
            menu_barang()

        elif pilihan == "4":
            menu_gudang()

        elif pilihan == "5":
            cek_stok()

        elif pilihan == "6":
            peringatan_stok()

        elif pilihan == "7":
            menu_laporan()

        elif pilihan == "0":
            print("Terima kasih telah menggunakan SMK MART.")
            break

        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")
