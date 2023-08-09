import json
import random
import string
import datetime
def pembatas():
    print("-" * 70)
    
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)
def generate_item_code():
    item_code =  ''.join(random.choices(string.digits, k=12))
    return item_code
def generate_date_code():
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return date
tampungBarang = load_data()


def menu():
    while True:
        print("=" * 70)
        print("APLIKASI STOCK INVENTORY".center(70, " "))
        print("=" * 70)
        pembatas()
        lihatDaftarBarang()
        pembatas()
        print(" AKSI ITEM ".center(70, "-"))
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Edit Item")
        print("4. Cari Item")
        print("5. Simpan Item")
        print("6. Keluar")
        pembatas()
        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            tambahBarang()
        elif pilihan == "2":
            hapusBarang()
        elif pilihan == "3":
            editBarang()
        elif pilihan == "4":
            cariBarang()
        elif pilihan == "5":
            save_data(tampungBarang)
            print("Data Anda Berhasil Disimpan! ")
            return menu()
        elif pilihan == "6":
            save_data(tampungBarang)
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
        pembatas()


def tambahBarang():
    pembatas()
    print("PENAMBAHAN ITEM".center(70, " "))
    pembatas()
    while True:
        item_code = input("masukan Item code (kosong akan random)")
        if not item_code:
            item_code = generate_item_code()
        barang = input("Masukkan Nama Item: ")
        jumlah = input("Masukkan Jumlah Item: ")
        try:
            jumlah = int(jumlah)
        except ValueError:
            print("Masukkan angka yang benar!")
            return tambahBarang()
        keterangan = input("Masukkan Keterangan Item: ")
        date = generate_date_code()
        tampungBarang[item_code] = {
            "nama": barang,
            "jumlah": jumlah,
            "keterangan": keterangan,
            "tanggal": date,
            "tanggal_diubah": date
        }
        
        print("Barang", barang, "ditambahkan dengan Item Code:", item_code)
        pilihan = input("Tambahkan Item lagi? (y/n): ")
        if pilihan == "n":
            menu()
        elif pilihan == "y":
            return tambahBarang()
        else:
            print("Kata yang Anda masukkan salah")
            return tambahBarang()

def lihatDaftarBarang():
    pembatas()
    print("DAFTAR ITEM".center(70, " "))
    pembatas()
    print("No".center(5, " "),"|","Code Item".center(15, " "),"|", "Nama Item".center(20, " "),"|", "Jumlah".center(10, " "),"|", "Keterangan".center(10, " "))
    no = 1
    for item_code, data in tampungBarang.items():
        print(
            str(no).center(5, " "),"|",
            item_code.center(15, " "),"|",
            data["nama"].center(20, " "),"|",          
            str(data["jumlah"]).center(10, " "),"|",
            data["keterangan"].center(10, " ")
        )
        no += 1
    
def hapusBarang():
    pembatas()
    print("HAPUS ITEM".center(70, " "))
    pembatas()
    lihatDaftarBarang()
    no_barang = (input("Masukkan nomor Item yang akan dihapus: "))
    try:
        no_barang = int(no_barang)
    except ValueError:
        print("Masukkan angka yang benar!")
        return hapusBarang()
    if no_barang <= len(tampungBarang):
        barang_yang_dihapus = list(tampungBarang.keys())[no_barang - 1]
        del tampungBarang[barang_yang_dihapus]
        print("Item", barang_yang_dihapus, "telah dihapus.")
        pilihan = input("apakah anda ingin kembali ke menu? y/n :")
        if pilihan == "y":
            menu()
        elif pilihan == "n":
            return hapusBarang()
        else:
            print("kata yang anda masukan salah")
            return hapusBarang()
    else:
        print("Item yang anda cari tidak ada")
        pilihan = input("apakah anda ingin kembali ke menu? y/n :")
        if pilihan == "y":
            menu()
        elif pilihan == "n":
            return hapusBarang()
        else:
            print("kata yang anda masukan salah")
            return hapusBarang()



def editBarang():
    pembatas()
    print("EDIT ITEM".center(70, " "))
    pembatas()
    lihatDaftarBarang()
    no_barang = int(input("Masukkan nomor Item yang akan diedit: "))
    if no_barang <= len(tampungBarang):
        item_code_list = list(tampungBarang.keys())
        barang_yang_diedit = item_code_list[no_barang - 1]
        print("Code Item:", barang_yang_diedit)
        print("Nama Item:", tampungBarang[barang_yang_diedit]["nama"])
        print("Jumlah Item:", tampungBarang[barang_yang_diedit]["jumlah"])
        print("Keterangan Item:", tampungBarang[barang_yang_diedit]["keterangan"])
        pilihan_edit = input("Pilih data Item yang akan diedit (1:Nama / 2:Jumlah / 3:Keterangan): ")
        if pilihan_edit == "1":
            nama_baru = input("Masukkan Item Barang Baru: ")
            tampungBarang[barang_yang_diedit]["nama"] = nama_baru
            tampungBarang[barang_yang_diedit]["tanggal_diubah"] = generate_date_code()
            print("Nama Item berhasil diubah.")
        elif pilihan_edit == "2":
            jumlah_baru = input("Masukkan Jumlah Item Baru: ")
            try:
                jumlah_baru = int(jumlah_baru)
                if jumlah_baru >= 0:
                    tampungBarang[barang_yang_diedit]["jumlah"] = jumlah_baru
                    tampungBarang[barang_yang_diedit]["tanggal_diubah"] = generate_date_code()
                    print("Jumlah Item berhasil diubah.")
                else:
                    print("Masukkan angka yang tidak negatif!")
            except ValueError:
                print("Masukkan angka yang benar!")
        elif pilihan_edit == "3":
            keterangan_baru = input("Masukkan Keterangan Item Baru: ")
            tampungBarang[barang_yang_diedit]["keterangan"] = keterangan_baru
            tampungBarang[barang_yang_diedit]["tanggal_diubah"] = generate_date_code()
            print("Keterangan Item berhasil diubah.")
        pilihan = input("Apakah Anda ingin kembali ke menu? y/n :")
        if pilihan == "y":
            menu()
        elif pilihan == "n":
            return editBarang()
    else:
        print("Item yang anda cari tidak ada")
        pilihan = input("Apakah Anda ingin kembali ke menu? y/n :")
        if pilihan == "y":
            menu()
        elif pilihan == "n":
            return editBarang()
        else:
            print("Kata yang anda masukkan salah")
            return editBarang()

def cariBarang():
    pembatas()
    print("CARI ITEM".center(70, " "))
    pembatas()
    keyword = input("Masukkan Nama Item atau Item Code yang ingin dicari: ")
    found = False
    for item_code, data in tampungBarang.items():
        if keyword == item_code or keyword == data["nama"]:
            print(
                "Code Item:", item_code,
                "\nNama Item:", data["nama"],
                "\nJumlah Item:", data["jumlah"],
                "\nKeterangan Item:", data["keterangan"],
                "\nTanggal Masuk:", data["tanggal"],
                "Terakhir diubah:", data.get("tanggal_diubah", "N/A")
            )
            found = True
    if not found:
        print("Item tidak ditemukan.")
    pilihan = input("Apakah Anda ingin kembali ke menu? (y/n): ")
    if pilihan == "y":
        menu()
    elif pilihan == "n":
        return cariBarang()


menu()