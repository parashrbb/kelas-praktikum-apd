cuaca = int(input("Masukkan cuaca hari ini : "))

if cuaca == "cerah":
    print("kamu pergi keluar rumah")
else:
    print("diam di rumah")


Umur = int(input("Masukkan umur Anda : "))
if Umur > 0:
    if Umur <=10:
        print( " Umur Anda termasuk kategori anak-anak")
    elif Umur <=18:
        print( " Umur Anda termasuk kategori remaja")
    elif Umur <=35:
        print( " Umur Anda termasuk kategori dewasa")
    elif Umur <=65:
        print( " Umur Anda termasuk kategori lansia")
    else:
        print(" Umur Anda termasuk kategori Tua")
else:
    print("Input usia Harus Bilangan Positif")


nim = int(input("masukkan NIM : "))

if nim >= 1 and nim <= 45 :
    if nim >= 1 and nim <= 22 :
        print("Kelas A'1")
    else :
        print("kelas A'2")
elif nim >= 46 and nim <= 90:
    if nim >= 46 and nim <= 68 :
        print("Kelas B'1")
    else :
        print("kelas B'2")
elif nim >= 91 and nim <= 123 :
    if nim >= 91 and nim <= 123 :
        print("Kelas C'1")
    else :
        print("Kelas C'2")
else :
    print("Anda Bukan Anak Informatika UNMUL 2024")


# angka = int(input("Masukkan angka: "))
# result = "Genap" if angka % 2 == 0 else "Ganjil"
# print(angka, "adalah angka",result)


nim = int(input("masukkan nim anda : "))
hasil = "kelas A" if nim >= 1 and nim <= 45 else "kelas B" if nim >= 46 and nim <= 90 else "kelas C" if nim >= 91 and nim <= 123 else ("mahasiswa siluman")
print("NIM", nim, "anda anak", hasil)