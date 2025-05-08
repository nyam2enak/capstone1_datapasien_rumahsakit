# Nama : Novianto Chris
# Email : tom.cris@gmail.com
# PURWADHIKA PROGRAM DATA SCIENCE

#CAPSTONE PROJECT PROGRAM DATA PASIEN DAN REGISTRASI PELAYANAN RUMAH SAKIT SUMBER WARAS 
# ==========================================================


import datetime

# Data awal untuk pasien, jenis klinik, dan registrasi pelayanan

data_pasien = {"RS0001": {"nama": "Ricki Asmoro", "jenis_kelamin": "L", "alamat": "Jl. Merdeka No. 1", "no_telp": "08123456789","tanggal_lahir": "01-05-1970", "status": "Aktif"}, 
                "RS0002": {"nama": "Dewi Indriani", "jenis_kelamin": "P", "alamat": "Jl. Pahlawan No. 2", "no_telp": "08234567890","tanggal_lahir": "05-10-1982", "status": "Aktif"},
                "RS0003": {"nama": "Steven Jayadi", "jenis_kelamin": "P", "alamat": "Jl. Kebangsaan No. 3", "no_telp": "08345678901","tanggal_lahir": "30-05-1992", "status": "Aktif"},
                "RS0004": {"nama": "Adi Wirawan",  "jenis_kelamin": "L", "alamat": "Jl. Kebudayaan No. 4", "no_telp": "08456789012","tanggal_lahir": "04-06-2000", "status": "Aktif"}, 
                "RS0005": {"nama": "Rinaldi Ahmad", "jenis_kelamin": "L", "alamat": "Jl. Kebangkitan No. 5", "no_telp": "08567890123","tanggal_lahir": "14-12-2012", "status": "Aktif"},}

data_jenis_klinik = {"KL0001": {"nama": "Klinik Umum", "spesialis": "Umum", "jadwal": "Senin-Jumat 08:00-16:00"},
                      "KL0002": {"nama": "Klinik Gigi", "spesialis": "Gigi", "jadwal": "Senin-Jumat 08:00-16:00"},
                      "KL0003": {"nama": "Klinik Anak", "spesialis": "Anak", "jadwal": "Senin-Jumat 08:00-16:00"},
                      "KL0004": {"nama": "Klinik Bedah", "spesialis": "Bedah", "jadwal": "Senin-Jumat 08:00-16:00"},
                      "KL0005": {"nama": "Klinik Penyakit Dalam", "spesialis": "Penyakit Dalam", "jadwal": "Senin-Jumat 08:00-16:00"},}

data_registrasi = {"TRS0001": {"tanggal": "2023-10-01", "jenis_klinik": "KL0001", "dokter": "Dr. Suroso", "status": "Aktif","pasien": "RS0001"},
                   "TRS0002": {"tanggal": "2023-10-02", "jenis_klinik": "KL0002", "dokter": "Dr. Siti", "status": "Aktif","pasien": "RS0002"},
                   "TRS0003": {"tanggal": "2023-10-03", "jenis_klinik": "KL0003", "dokter": "Dr. Budi", "status": "Aktif","pasien": "RS0003"},
                   "TRS0004": {"tanggal": "2023-10-04", "jenis_klinik": "KL0004", "dokter": "Dr. Rina", "status": "Aktif","pasien": "RS0004"},
                   "TRS0005": {"tanggal": "2023-10-05", "jenis_klinik": "KL0005", "dokter": "Dr. Andi",  "status": "Aktif","pasien": "RS0005"},}

# Fungsi untuk membersihkan layar
def clear_screen():
    print("\033[H\033[J", end="")

# Fungsi untuk menampilkan menu utama data pasien dan registrasi pelayanan
def menu_utama():
    print("=== Menu Utama ===")
    print("1. Data Pasien")
    print("2. Registrasi Pelayanan")
    print("3. Keluar")
    print("=====================================")
    print("\n")
    pilihan = input("Pilih menu (1/2/3): ")
    return pilihan

# fungsi untuk menampilkan submenu data pasien
def submenu_data_pasien():
    print("=== Submenu Data Pasien ===")
    print("1. Tampilkan Data Pasien")
    print("2. Tambah Data Pasien")
    print("3. Ubah Data Pasien")
    print("4. Hapus Data Pasien")
    print("5. Kembali ke Menu Utama")
    print("=====================================")
    print("\n")
    pilihan = input("Pilih submenu (1/2/3/4/5): ")
    return pilihan

#fungsi untuk menampilkan submenu registrasi pelayanan
def submenu_registrasi_pelayanan():
    print("=== Submenu Registrasi Pelayanan ===")
    print("1. Tampilkan Registrasi Pelayanan")
    print("2. Tambah Registrasi Pelayanan")
    print("3. Ubah Registrasi Pelayanan")
    print("4. Hapus Registrasi Pelayanan")
    print("5. Kembali ke Menu Utama")
    pilihan = input("Pilih submenu (1/2/3/4/5): ")
    return pilihan

# Fungsi utama untuk menjalankan program

def main():
    while True:
        clear_screen()
        print("=== Sistem Informasi Rumah Sakit Sumber Waras ===")
        print("Selamat datang di sistem informasi rumah sakit.")
        print("Silakan pilih menu yang tersedia.")
        print("=====================================")
        print("\n")
        
        pilihan = menu_utama()
        if pilihan == "1":
            # bersihkan layar setiap kali menu utama ditampilkan    
            clear_screen()        
            
            print("=== Submenu Data Pasien ===")
            print("Silakan pilih submenu yang tersedia.")
            print("=====================================")
            print("\n")
            while True:

                submenu = submenu_data_pasien()
                if submenu == "1":
                    clear_screen()
                    tampilkan_data_pasien()
                elif submenu == "2":
                    clear_screen()
                    tambah_data_pasien()
                elif submenu == "3":
                    clear_screen()
                    ubah_data_pasien()
                elif submenu == "4":
                    clear_screen()
                    hapus_data_pasien()
                elif submenu == "5":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan == "2":
            clear_screen()
            print("=== Submenu Registrasi Pelayanan ===")
            print("Silakan pilih submenu yang tersedia.")
            print("=====================================")
            print("\n")
            while True:
                submenu = submenu_registrasi_pelayanan()
                if submenu == "1":
                    clear_screen()
                    tampilkan_data_registrasi()
                elif submenu == "2":
                    clear_screen()
                    tambah_data_registrasi()
                elif submenu == "3":
                    clear_screen()
                    ubah_data_registrasi()
                elif submenu == "4":
                    clear_screen()
                    hapus_data_registrasi()
                elif submenu == "5":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan == "3":
            print("Terima kasih! Program Keluar.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jika jensis_kelamin adalah "L" maka tampilkan "Laki-laki", jika "P" maka tampilkan "Perempuan"
def format_jenis_kelamin(jenis_kelamin):
    if jenis_kelamin == "L":
        return "Laki-laki"
    elif jenis_kelamin == "P":
        return "Perempuan"
    else:
        return "Tidak Diketahui"
    
# tampilkan kolom umur dengan format bulan, tahun
def format_umur(tanggal_lahir):
    try:
        tanggal_lahir = datetime.datetime.strptime(tanggal_lahir, "%d-%m-%Y")
        umur = datetime.datetime.now() - tanggal_lahir
        tahun = umur.days // 365
        bulan = (umur.days % 365) // 30
        return f"{tahun} tahun {bulan} bulan "
    except ValueError:
        return "Tanggal lahir tidak valid"
    
def tampilkan_data_pasien():
    print("\n")
    
    print("=== Data Pasien ===")
    print(f"{'ID Pasien':<10} {'Nama':<20} {'Jenis Kelamin':<15} {'Alamat':<25} {'No. Telepon':<15} {'Tanggal Lahir':<15} {'Umur':<20} {'Status':<10} ")
    print("="*150)
    for id_pasien, data in data_pasien.items():
        print(f"{id_pasien:<10} {data['nama']:<20} {format_jenis_kelamin(data['jenis_kelamin']):<15} {data['alamat']:<25} {data['no_telp']:<15} {data['tanggal_lahir']:<15} {format_umur(data['tanggal_lahir']):<20} {data['status']:<10} ")
    
    print("\n")


#fungsi untuk menambahkan data pasien 
def tambah_data_pasien():
    print("\n")
    print("=== Tambah Data Pasien ===")
    print("\n")
    while True:
        id_pasien = f"RS{str(len(data_pasien) + 1).zfill(4)}"
        print(f"ID Pasien: {id_pasien}")

        nama = input("Masukkan Nama Pasien: ")
        # Validasi jenis kelamin
        while True:
            jenis_kelamin = input("Masukkan Jenis Kelamin Pasien (L/P): ")
            if jenis_kelamin in ["L", "P"]:
                break
            else:
                print("Jenis kelamin tidak valid. Silakan masukkan L atau P.")
        
        alamat = input("Masukkan Alamat Pasien: ")
        no_telp = input("Masukkan No. Telepon Pasien: ")

        # Validasi tanggal lahir
        while True:
            tanggal_lahir = input("Masukkan Tanggal Lahir Pasien (DD-MM-YYYY): ")
            try:
                datetime.datetime.strptime(tanggal_lahir, "%d-%m-%Y")
                break
            except ValueError:
                print("Format tanggal tidak valid. Silakan masukkan ulang.")

        status = "Aktif"

        data_pasien[id_pasien] = {
            "nama": nama,
            "jenis_kelamin": jenis_kelamin,
            "alamat": alamat,
            "no_telp": no_telp,
            "tanggal_lahir": tanggal_lahir,
            "status": status
        }

        print("\n")

        tambah_lagi = input("Tambah data pasien lagi? (y/n): ")
        if tambah_lagi.lower() != 'y':
            break

    print("\n")
    print("Data Pasien Setelah Ditambahkan:")
    tampilkan_data_pasien()

# Fungsi untuk mengubah data pasien
def ubah_data_pasien():
    print("\n")
    print("=== Ubah Data Pasien ===")
    print("\n")
    while True:
        id_pasien = input("Masukkan ID Pasien yang ingin diubah: ")
        if id_pasien not in data_pasien:
            print("ID Pasien tidak ditemukan. Silakan masukkan ID yang valid.")
            continue

        print("\n")
        print("Data Pasien Sebelumnya:")
        # tampilkan data pasien sebelumnya 
        print(f"{'ID Pasien':<10} {'Nama':<20} {'Jenis Kelamin':<15} {'Alamat':<25} {'No. Telepon':<15} {'Tanggal Lahir':<15} {'Status':<10}")
        print("="*150)
        print(f"{id_pasien:<10} {data_pasien[id_pasien]['nama']:<20} {format_jenis_kelamin(data_pasien[id_pasien]['jenis_kelamin']):<15} {data_pasien[id_pasien]['alamat']:<25} {data_pasien[id_pasien]['no_telp']:<15} {data_pasien[id_pasien]['tanggal_lahir']:<15} {data_pasien[id_pasien]['status']:<10}")
        print("\n")
        

        nama = input("Masukkan Nama Pasien Baru (tekan enter untuk tidak mengubah): ")
        # Validasi jenis kelamin
        while True:
            jenis_kelamin = input("Masukkan Jenis Kelamin Baru (L/P, tekan enter untuk tidak mengubah): ")
            if jenis_kelamin == "":
                break
            elif jenis_kelamin in ["L", "P"]:
                break
            else:
                print("Jenis kelamin tidak valid. Silakan masukkan L atau P.")
       
        alamat = input("Masukkan Alamat Pasien Baru (tekan enter untuk tidak mengubah): ")
        no_telp = input("Masukkan No. Telepon Pasien Baru (tekan enter untuk tidak mengubah): ")

        # Validasi tanggal lahir
        while True:
            tanggal_lahir = input("Masukkan Tanggal Lahir Pasien Baru (DD-MM-YYYY, tekan enter untuk tidak mengubah): ")
            if tanggal_lahir == "":
                break
            try:
                datetime.datetime.strptime(tanggal_lahir, "%d-%m-%Y")
                break
            except ValueError:
                print("Format tanggal tidak valid. Silakan masukkan ulang.")

        status = input("Masukkan Status Pasien Baru (Aktif/Tidak Aktif, tekan enter untuk tidak mengubah): ")

        if nama != "":
            data_pasien[id_pasien]["nama"] = nama
        if jenis_kelamin != "":
            data_pasien[id_pasien]["jenis_kelamin"] = jenis_kelamin
        if alamat != "":
            data_pasien[id_pasien]["alamat"] = alamat
        if no_telp != "":
            data_pasien[id_pasien]["no_telp"] = no_telp
        if tanggal_lahir != "":
            data_pasien[id_pasien]["tanggal_lahir"] = tanggal_lahir
        if status != "":
            data_pasien[id_pasien]["status"] = status

        print(f"Data pasien {id_pasien} berhasil diubah.")
        print("\n")
        
        ubah_lagi = input("Ubah data pasien lagi? (y/n): ")
        if ubah_lagi.lower() != 'y':
            break
    
    print("\n")
    print("Data Pasien Setelah Diubah:")
    tampilkan_data_pasien()

#fungsi untuk menghapus data pasien 
def hapus_data_pasien():
    print("\n")
    print("=== Hapus Data Pasien ===")
    print("\n")
    while True:
        id_pasien = input("Masukkan ID Pasien yang ingin dihapus: ")
        if id_pasien not in data_pasien:
            print("ID Pasien tidak ditemukan. Silakan masukkan ID yang valid.")
            continue

        del data_pasien[id_pasien]
        print(f"Data pasien {id_pasien} berhasil dihapus.")

        hapus_lagi = input("Hapus data pasien lagi? (y/n): ")
        if hapus_lagi.lower() != 'y':
            break
    
    print("\n")
    print("Data Pasien Setelah Dihapus:")
    tampilkan_data_pasien()



# Fungsi untuk menampilkan data registrasi pelayanan dengan keterangan jenis klinik
def tampilkan_data_registrasi():
    print("\n")
    print("=== Data Registrasi Pelayanan ===")
    print(f"{'ID Registrasi':<15} {'Nama Pasien':<20} {'Tanggal':<15} {'Jenis Klinik':<25} {'Dokter':<20} {'Status':<10}")
    print("="*150)
    for id_registrasi, data in data_registrasi.items():
        id_pasien = data["pasien"]
        nama_pasien = data_pasien[id_pasien]["nama"]
        print(f"{id_registrasi:<15} {nama_pasien:<20} {data['tanggal']:<15} {data_jenis_klinik[data['jenis_klinik']]['nama']:<25} {data['dokter']:<20} {data['status']:<10}")
    print("\n")
    print("=====================================")
    print("\n")

# Fungsi untuk menambahkan data registrasi pelayanan 
def tambah_data_registrasi():
    print("\n")
    print("=== Tambah Data Registrasi Pelayanan ===")
    print("\n")
    
    while True:
        id_registrasi = f"TRS{str(len(data_registrasi) + 1).zfill(4)}"
        print(f"ID Registrasi: {id_registrasi}")

        # Validasi nama pasien
        while True:
            id_pasien = input("Masukkan ID Pasien: ")
            if id_pasien in data_pasien:
                break
            else:
                print("ID Pasien tidak ditemukan. Silakan masukkan ID yang valid.")

        # Validasi tanggal registrasi
        while True:
            tanggal = input("Masukkan Tanggal Registrasi (DD-MM-YYYY): ")
            try:
                datetime.datetime.strptime(tanggal, "%d-%m-%Y")
                break
            except ValueError:
                print("Format tanggal tidak valid. Silakan masukkan ulang.")

        # Validasi jenis klinik
        print("\n")
        print("=== Jenis Klinik yang Tersedia ===")
        print(f"{'ID Klinik':<10} {'Nama Klinik':<20}")
        print("="*50)
        for id_klinik, data in data_jenis_klinik.items():
            print(f"{id_klinik}: {data['nama']}")
        print("\n")

        while True:
            jenis_klinik = input("Masukkan ID Jenis Klinik: ")
            if jenis_klinik in data_jenis_klinik:
                break
            else:
                print("Jenis klinik tidak valid. Silakan masukkan jenis klinik yang benar.")

        dokter = input("Masukkan Nama Dokter: ")
        status = "Aktif"

        data_registrasi[id_registrasi] = {
            "tanggal": tanggal,
            "jenis_klinik": jenis_klinik,
            "dokter": dokter,
            "status": status,
            "pasien": id_pasien
        }

        print("\n")
        
        tambah_lagi = input("Tambah data registrasi lagi? (y/n): ")
        if tambah_lagi.lower() != 'y':
            break

    print("\n")
    print("Data Registrasi Setelah Ditambahkan:")
    tampilkan_data_registrasi() 

# Fungsi untuk mengubah data registrasi pelayanan 
def ubah_data_registrasi():
    print("\n")
    print("=== Ubah Data Registrasi Pelayanan ===")
    print("\n")
    while True:
        id_registrasi = input("Masukkan ID Registrasi yang ingin diubah: ")
        if id_registrasi not in data_registrasi:
            print("ID Registrasi tidak ditemukan. Silakan masukkan ID yang valid.")
            continue

        print("Data Registrasi Sebelumnya:")
        # tampilkan data registrasi sebelumnya  dengan nama pasien
        print(f"{'ID Registrasi':<15}  {'Nama Pasien':<20} {'Tanggal':<15} {'Jenis Klinik':<25} {'Dokter':<20} {'Status':<10}")
        print("="*150)
        id_pasien = data_registrasi[id_registrasi]["pasien"]
        nama_pasien = data_pasien[id_pasien]["nama"]
        print(f"{id_registrasi:<15} {nama_pasien:<20} {data_registrasi[id_registrasi]['tanggal']:<15} {data_jenis_klinik[data_registrasi[id_registrasi]['jenis_klinik']]['nama']:<25} {data_registrasi[id_registrasi]['dokter']:<20} {data_registrasi[id_registrasi]['status']:<10}")
        print("\n")

        # Validasi nama pasien
        while True:
            id_pasien = input("Masukkan ID Pasien Baru (tekan enter untuk tidak mengubah): ")
            if id_pasien == "":
                break
            elif id_pasien in data_pasien:
                break
            else:
                print("ID Pasien tidak ditemukan. Silakan masukkan ID yang valid.")

        # Validasi tanggal registrasi
        while True:
            tanggal = input("Masukkan Tanggal Registrasi Baru (DD-MM-YYYY, tekan enter untuk tidak mengubah): ")
            if tanggal == "":
                break
            try:
                datetime.datetime.strptime(tanggal, "%d-%m-%Y")
                break
            except ValueError:
                print("Format tanggal tidak valid. Silakan masukkan ulang.")

        # Validasi jenis klinik
        print("\n")
        print("=== Jenis Klinik yang Tersedia ===")
        print(f"{'ID Klinik':<10} {'Nama Klinik':<20}")
        print("="*50)
        for id_klinik, data in data_jenis_klinik.items():
            print(f"{id_klinik}: {data['nama']}")
        print("\n")

        while True:
            jenis_klinik = input("Masukkan ID Jenis Klinik Baru (tekan enter untuk tidak mengubah): ")
            if jenis_klinik == "":
                break
            elif jenis_klinik in data_jenis_klinik:
                break
            else:
                print("Jenis klinik tidak valid. Silakan masukkan jenis klinik yang benar.")

        dokter = input("Masukkan Nama Dokter Baru (tekan enter untuk tidak mengubah): ")
        status = input("Masukkan Status Baru (Aktif/Tidak Aktif, tekan enter untuk tidak mengubah): ")

        if id_pasien != "":
            data_registrasi[id_registrasi]["pasien"] = id_pasien
        if tanggal != "":
            data_registrasi[id_registrasi]["tanggal"] = tanggal
        if jenis_klinik != "":
            data_registrasi[id_registrasi]["jenis_klinik"] = jenis_klinik
        if dokter != "":
            data_registrasi[id_registrasi]["dokter"] = dokter
        if status != "":
            data_registrasi[id_registrasi]["status"] = status
        print(f"Data registrasi {id_registrasi} berhasil diubah.")
        print("\n")
        ubah_lagi = input("Ubah data registrasi lagi? (y/n): ")
        if ubah_lagi.lower() != 'y':
            clear_screen()
            break
    print("\n")
    print("Data Registrasi Setelah Diubah:")
    tampilkan_data_registrasi()

# Fungsi untuk menghapus data registrasi pelayanan 
def hapus_data_registrasi():
    print("\n")
    print("=== Hapus Data Registrasi Pelayanan ===")
    print("\n")

    while True:
        id_registrasi = input("Masukkan ID Registrasi yang ingin dihapus: ")
        if id_registrasi not in data_registrasi:
            print("ID Registrasi tidak ditemukan. Silakan masukkan ID yang valid.")
            continue

        del data_registrasi[id_registrasi]

        print("\n")
        print(f"Data registrasi {id_registrasi} berhasil dihapus.")

        hapus_lagi = input("Hapus data registrasi lagi? (y/n): ")
        if hapus_lagi.lower() != 'y':
            break
    
    print("\n")
    print("Data Registrasi Setelah Dihapus:")
    tampilkan_data_registrasi()



if __name__ == "__main__":
    main()
    

