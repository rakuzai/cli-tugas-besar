# KELOMPOK 5

# ANGGOTA KELOMPOK:
# 1. AGUNG WIDIYANTO - 2211110001
# 2. ADHYSTIRA RAIHAN - 2211110007
# 3. ARVINANTO BAHTIAR - 2211110014
# 4. MAYESQ PRAMESWARI - 2211110002
# 5. SRI NAMIRA PUTRI HARNOKO - 2211110020

# LINK GITHUB CLI: https://github.com/rakuzai/cli-tugas-besar
# LINK GITHUB WEBSITE: https://github.com/rakuzai/django-tugas-besar 

import pandas as pd
import matplotlib.pyplot as plt

users = [['admin','password']]
data_transaksi = pd.DataFrame(columns=['Username','Total jumlah pembelian'])

def register(users):
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    print('Pembuatan akun berhasil!, anda bisa langsung masuk')
    users.append([username, password])
    main(users)

def login(users):
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    found = False
    for user in users:
        if username == "admin" and password == "password" :
            print("Login admin berhasil!")
            adminMenu(users, data_transaksi)
            found = True
            break
        elif user[0] == username and user[1] == password :
            print("Login berhasil!")
            customerMenu(users, data_transaksi)
            found = True
            break
    if not found:
        print("Username atau password salah")
        main(users)

def adminMenu(users, df):
    while True:
        print("Menu Utama Admin:")
        print("1. Lihat Grafik Transaksi")
        print("2. Logout")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1 :
            if data_transaksi.empty :
                print("Belum ada transaksi")
            else :
                data_transaksi.plot(kind = 'bar', x = "Username",y = "Total jumlah pembelian")
                plt.ylabel("Total jumlah pembelian (Rupiah)")
                plt.show()
        elif pilihan == 2 :
            print("Anda berhasil logout.")
            main(users)
        else :
            print("pilihan tidak tersedia")
            adminMenu(users, df)

def customerMenu(users, df):
    global data_transaksi
    data_transaksi = df.copy()
    if data_transaksi[data_transaksi['Username'] == username].empty:
        data_transaksi = data_transaksi.append({'Username':username, 'Total jumlah pembelian':0}, ignore_index=True)
    while True:
        print("Halaman Utama:")
        print("1. Pesan")
        print("2. List Menu")
        print("3. Logout")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            print("Menu Makanan & Minuman:")
            print("1. Milkshake - Rp. 10.000")
            print("2. Nasi Padang - Rp. 15.000")
            print("3. Rice Bowl - Rp. 20.000")
            pesan = []
            total_harga = 0
            pilihan = "y"
            while pilihan == "y":
                pemesanan = int(input("Masukkan pesanan: "))
                if pemesanan == 1:
                    pesan.append("Milkshake")
                    total_harga += 10000
                elif pemesanan == 2:
                    pesan.append("Nasi Padang")
                    total_harga += 15000
                elif pemesanan == 3:
                    pesan.append("Rice Bowl")
                    total_harga += 20000
                else:
                    print("Pilihan tidak tersedia.")
                    customerMenu(users, df)
                pilihan = input("Apakah ingin memesan lagi? (y/n): ")
            print("Total yang harus dibayar : Rp. {}".format( total_harga))
            bayar = int(input("Masukkan jumlah pembayaran: "))
            if bayar < total_harga:
                kurang = total_harga - bayar
                print("Maaf, pesanan anda gagal..")
                print("Uang yang anda berikan kurang sebanyak: Rp. {}".format(kurang))
            else:
                kembalian = bayar - total_harga      
                print("Struk Pemesanan:")
                print("Pesanan: {}".format(pesan))
                print("Total Harga: Rp. {}".format(total_harga))
                print("Pembayaran: Rp. {}".format(bayar))
                print("Kembalian: Rp. {}".format(kembalian))
                data_transaksi.loc[data_transaksi['Username'] == username, 'Total jumlah pembelian'] += total_harga
        elif pilihan == 2:
            print("Menu Makanan & Minuman:")
            print("1. Milkshake - Rp. 10.000")
            print("2. Nasi Padang - Rp. 15.000")
            print("3. Rice Bowl - Rp. 20.000")
        elif pilihan == 3 :
            print("Anda berhasil logout.")
            main(users)                      
        else:
            print("Pilihan tidak tersedia.")
            customerMenu(users, df)

def main(users):
    print("Halaman Daftar & Masuk:")
    print("1. Daftar")
    print("2. Masuk")

    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:
        register(users)
    elif pilihan == 2:
        login(users)
    else:
        print('Pilihan tidak tersedia')
        main(users)
                
main(users)
