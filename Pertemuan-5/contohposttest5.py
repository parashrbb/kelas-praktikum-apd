akuns = []

while True:
    print("__________________________________________________________________________________________")
    print("HALO! Selamat datang di aplikasi Catatan")
    print("Silahkan 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan login")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("__________________________________________________________________________________________")
    opsi = input("Pilih opsi : ")
    print(" ")

    if opsi == "1":
        print("__________________________")
        print("Halo Pengguna Baru :)")
        print("Ayo buat Akun dulu!")
        Username = input("Username : ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username: #memeriksa apakahusername sudah ada
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai untuk Registrasi Silahkan Coba lagi")
        else:
            Password = input("Password : ")
            akuns.append({Username, Password, []}) #simpan username, password, dan catatan (sebagai list kosong)
            print(f"Akun anda Berhasil Terdaftar dengan ID: {Username}")